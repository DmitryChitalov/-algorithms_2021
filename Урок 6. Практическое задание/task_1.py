"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from functools import wraps
from memory_profiler import memory_usage, profile
from pympler import asizeof
import copy


def mem_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper


@mem_decorator
def work_list(a):
    my_list = [item ** 2 for item in a]
    return my_list


@mem_decorator
def work_generator(a):
    for item in a:
        yield item ** 2


data_list = list(range(10000000))
print(work_list(data_list))
print(work_generator(data_list))

#1.0546875
#0.0

#Декоратор  отображает количество памяти которую использует функция
#По результатам видно что функция которая использует занимает определенный объем памяти.
#Функция которая генерирует список занимает определенное размер.
#при использовании ренегатора , памяти хватает выделеной при старте


class Road1:
    weight_per_m2 = 2550005

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calculation(self, thickness):
        weight = self._width * self._length * (Road1.weight_per_m2**2) * thickness **2
        print(f"Масса асфальта равна: {round(weight,5)} тонн.")


class Road2:
    __slots__ = ['_length', '_width']
    weight_per_m2 = 2550005

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calculation(self, thickness):
        weight = self._width * self._length * (Road2.weight_per_m2**2) * thickness **  2
        print(f"Масса асфальта равна: {round(weight,5)} тонн.")


r1 = Road1(2000000, 1)
r2 = Road2(2000000, 1)



print(f"R1 Memory Usage (bytes): {asizeof.asizeof(r1)}")
print(f"R2 Memory Usage (bytes): {asizeof.asizeof(r2)}")

#R1 Memory Usage (bytes): 328
#R2 Memory Usage (bytes): 112
#При использования хэш таблиц для хранения атрибутов класса использование памяти больше чем при использование slot.


