from memory_profiler import memory_usage
from timeit import default_timer
from random import randint
from pympler import asizeof
import json


def memory_time_profiler(func):
    def wraper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Время выполнения: {timer}\nИспользуемая память: {memory}')
        return result
    return wraper


'''Вариант скрипта №1'''


def fact_1(n):
    if n == 0:
        return 1
    return fact_1(n-1) * n


def fact_2(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


@memory_time_profiler
def recurs_fact(function, n):
    return function(n)


n = 600
recurs_fact(fact_1, n)
recurs_fact(fact_2, n)

'''При использовании генератора, вместо рекурсии использование памяти уменьшилось, а время
выполнения осталось прежним, чем больше значении n, тем больше это заметно
Время выполнения: 0.107549215
Используемая память: 0.4912785
Время выполнения: 0.10937197799999998
Используемая память: 0.0
'''


'''Вариант скрипта №2'''


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


@memory_time
def only_el(list_in):
    result_list = []
    for el in list_in:
        if list_in.count(el) == 1:
            result_list.append(el)
    return result_list


@memory_time
def only_el1(list_in):
    for el in list_in:
        if list_in.count(el) == 1:
            yield el


print(only_el(my_list))
print(only_el1(my_list))

'''При использовании генератора уменьшается использование памяти
# и происходит огромный прирост производительности
# (0.2734375, 100.85386588800066)
# (0.0, 0.10067939900000056)'''


'''Вариант скрипта №3'''


my_dict = {el: el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0}

my_dict1 = {el: el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0}
dumped_dict = json.dumps(my_dict1)

print(asizeof.asizeof(my_dict))
print(asizeof.asizeof(dumped_dict))

'''При использование сериализации, размер хранимого объекта уменьшается в несколько раз, но данный
способ подходит лишь для хранения, т.к. для дальнейшего использования необходимо декодировать
объект используя json.loads'''


'''Варинт скрипта №4'''


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def roadbed_weight(self):
        rb_weight = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Вам понадобится {rb_weight:.0f} тон асфальта')


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

'''Использование __slots__ существенно уменьшает размер экземпляра класса, но при
этом в дальнейшем динамически добавлять новые атрибуты в класс будет невозможно.
# 512
# 192'''