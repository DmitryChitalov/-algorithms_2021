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

from timeit import default_timer
from memory_profiler import memory_usage
import numpy as np
from pympler import asizeof
from recordclass import recordclass
from collections import namedtuple
from functools import reduce


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        fin_time = default_timer()
        print(f"\nФункция: {func.__name__}")
        print(f"Memory: {m2[0] - m1[0]:0.5f} ")
        print(f"Time: {fin_time - start_time:0.5f} ")
        return res
    return wrapper


# Скрипт_1
print(f'{"*" * 25} Первый вариант "map" {"*" * 25}')


@decor
def example_1_map(data):
    return map(lambda x: x ** 2, data)


@decor
def example_1(data):
    return [i ** 2 for i in data]


example_1_map(list(range(100000)))
example_1(list(range(100000)))


"""
Встроенная функции map() достаточно сильно снижает расход памяти

Функция: func_1
Memory: 3.8632812500
Time: 0.2087600750

Функция: func_2
Memory: 5.0507812500
Time: 0.2066453440
"""


# Скрипт_2
print(f'{"*" * 25} Второй вариант "numpy" {"*" * 25}')


@decor
def example_2_numpy(data):
    return np.array(data)


@decor
def example_2(data):
    return list(data)


example_2_numpy(list(el for el in range(1000000)))
example_2(list(el for el in range(1000000)))

"""
Сторонний модуль NumPy очень хорошо оптимизирован для работы с большими массивами, и на этом примере
фун-и array видно насколько меньше требуется памяти.

Функция: example_2_numpy
Memory: 3.82031
Time: 0.25851

Функция: example_2
Memory: 7.63281
Time: 0.21243

"""


# Скрипт_3
print(f'{"*" * 25} Третий вариант "__slots__" {"*" * 25}')


class CalcHex:
    def __init__(self, number):
        self.number = number

    def __add__(self, second):
        return list(hex(int(self.number, 16) + int(second.number, 16)).upper()[2:])

    def __mul__(self, second):
        return list(hex(int(self.number, 16) * int(second.number, 16)).upper()[2:])


class CalcHexSlot:
    __slots__ = ["number"]

    def __init__(self, number):
        self.number = number

    def __add__(self, second):
        return list(hex(int(self.number, 16) + int(second.number, 16)).upper()[2:])

    def __mul__(self, second):
        return list(hex(int(self.number, 16) * int(second.number, 16)).upper()[2:])


# print(CalcHex('A2') + CalcHex('C4F'))
# print(CalcHex('A2') * CalcHex('C4F'))
print(f'Slot {asizeof.asizeof(CalcHexSlot("A2").__slots__)} байт')
print(f'без Slot {asizeof.asizeof(CalcHex("A2").__dict__)} байт')


"""
Slot 120 байт
без Slot 216 байт

Взял с урока №5
Магический атрибут Slot освобождает часть памяти при хранении данных
за счет ухода хранения в словаре на список, в данном примере.
"""


# Скрипт_4
print(f'{"*" * 25} Четвертый  вариант "recordclass" {"*" * 25}')


@decor
def average_1(num):
    all_firms = namedtuple('firms', 'comp_name revenue')
    all_firms_list = []
    numb_of_firm = num
    for i in range(numb_of_firm):
        name_firm = f'company_{i}'
        income = '545484545 858889999 2255588877 444455552'
        all_firms_list.append(all_firms(name_firm, sum(map(int, income.split()))))
    return sum(int(c.revenue) for c in all_firms_list) / numb_of_firm


@decor
def average_2(num):
    all_firms = recordclass('firms', 'comp_name revenue')
    all_firms_list = []
    numb_of_firm = num
    for i in range(numb_of_firm):
        name_firm = f'company_{i}'
        income = '545484545 858889999 2255588877 444455552'
        all_firms_list.append(all_firms(name_firm, sum(map(int, income.split()))))
    return sum(int(c.revenue) for c in all_firms_list) / numb_of_firm


average_1(1000000)
average_2(1000000)

"""
Функция: average_1 <- namedtuple
Memory: 0.7304687500
Time: 0.3728033530


Функция: average_2 <- recordclass
Memory: 0.0585937500
Time: 1.4922118840

Сторонний модуль "recordclass" обеспечивает большую экономию памяти, хорошо видно на примере
сравнения и namedtuple

"""


# Скрипт_5
print(f'{"*" * 25} Пятый вариант "reduce" {"*" * 25}')


@decor
def example_2(number):
    result = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)


@decor
def example_2_reduce(number):
    return reduce(lambda x, y: x + y, (i for i in range(number) if i % 3 == 0 or i % 5 == 0))


example_2(100000)
example_2_reduce(100000)


"""
Еще один пример с "ленивыми" операторами (итераторами) на примере фун-и reduce
с её помощью не надо хранить в память список, а сразу итерироваться.

Функция: example_2
Memory: 0.71484 
Time: 0.22111 

Функция: example_2_reduce
Memory: 0.00391 
Time: 0.21138
"""