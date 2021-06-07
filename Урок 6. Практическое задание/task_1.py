"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import memory_profiler
import timeit
from numpy import array
from random import randint
from pympler import asizeof
import json


"""
1
"""


# 1.1
random_num = [el + randint(0, 10) for el in range(10000)]

# 1.2
random_num_array = array([el + randint(0, 10) for el in range(10000)])


print(asizeof.asizeof(random_num))
print(asizeof.asizeof(random_num_array))


# array отлично подходит для снижения объёмов используемой памятии.
# map незначительно, но всё же снижает.
# 1-404928
# 2-40120


# 2.1
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def roadbed_weight(self):
        rb_weight = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Вам понадобится {rb_weight:.0f} тон асфальта')


# 2.2
class Road1:
    __slots__ = ['length', 'width', 'weight', 'thickness']

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.thickness = 5

    def roadbed_weight(self):
        rb_weight = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Вам понадобится {rb_weight:.0f} тон асфальта')


tarmac_weight = Road(5000, 20)
tarmac_weight1 = Road1(5000, 20)
# tarmac_weight.roadbed_weight()
print(asizeof.asizeof(tarmac_weight))
print(asizeof.asizeof(tarmac_weight1))

# Использование __slots__ существенно уменьшает размер экземпляра класса.
# 1-512
# 2-192


def memory_time(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = timeit.default_timer()
        func(*args)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = timeit.default_timer() - start_time
        return mem_diff, time_diff
    return wrapper


my_list = [el + randint(0, 20) for el in range(100000)]


# 3.1
my_dict = {el: el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0}


# 3.2
my_dict1 = {el: el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0}
dumped_dict = json.dumps(my_dict1)


# Если использовать сериализацию, то хранимый обьект займет куда меньше места
# 1-1880
# 2-304

print(asizeof.asizeof(my_dict))
print(asizeof.asizeof(dumped_dict))


# 4.1
@memory_time
def only_el(list_in):
    result_list = []
    for el in list_in:
        if list_in.count(el) == 1:
            result_list.append(el)
    return result_list


# 4.2
@memory_time
def only_el1(list_in):
    for el in list_in:
        if list_in.count(el) == 1:
            yield el


print(only_el(my_list))
print(only_el1(my_list))


# Использование генератора как во втором случае помогло нам сэкономить на ресурах системы
# 1-(0.26171875, 102.6423265)
# 2-(0.0, 0.11048409999999365)
