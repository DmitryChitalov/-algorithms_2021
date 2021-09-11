"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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

from collections import namedtuple
from recordclass import recordclass
from gc import collect
from memory_profiler import memory_usage
from numpy import array

lst_obj = [el for el in range(1000000)]
obj = tuple(el for el in range(1000000))


def memory_profile(func):
    def wrapper(*args, **kwargs):
        start_memory = memory_usage()
        func(*args, **kwargs)
        end_memory = memory_usage()
        print(f'Выполнение заняло: {end_memory[0] - start_memory[0]} Mib')
        return func(*args, **kwargs)

    return wrapper


@memory_profile
def get_sum_1(lst_obj):
    sum = 0
    for el in lst_obj:
        sum += el
    return sum


print(get_sum_1(lst_obj))


@memory_profile
def get_sum_2(lst_obj):
    sum = 0
    for el in lst_obj:
        sum += el
    collect()
    return sum


print(get_sum_2(lst_obj))

'''
collector сильно экономит память.
Также замена списка на кортеж уменьшает кольчество используемой паняти.
'''


@memory_profile
def inf_1():
    named_tuple = namedtuple('test_1', 'name surname numbers address')
    info_1 = named_tuple(name='Andrey', surname='Novikov', numbers=[el for el in range(10000)], address='Grina 11')
    return info_1


@memory_profile
def inf_2():
    record_class = recordclass('test_2', ('name', 'surname', 'numbers', 'address'))
    info_2 = record_class(name='Andrey', surname='Novikov', numbers=[el for el in range(10000)], address='Grina 11')
    return info_2


inf_1()
inf_2()
'''
Переменные recordclass используют меньше места по сравнению с namedtuple
'''


@memory_profile
def numpy_array():
    test_1 = array([el for el in range(1000000)])
    return test_1


@memory_profile
def arr():
    test_2 = list(el for el in range(1000000))
    return test_2


numpy_array()
arr()
'''
Модуль NumPy array хорошо оптимизирован и использует меньше памяти, чем обычный список
'''
