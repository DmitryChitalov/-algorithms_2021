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
from collections import namedtuple
from recordclass import recordclass
import gc
import memory_profiler
from numpy import array
lst_obj = [el for el in range(1000000)]
obj = tuple(el for el in range(1000000))


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло: {mem_diff} Mib')
        return res
    return wrapper


@decor
def get_sum_1(lst_obj_1):
    res_1 = 0
    for el in lst_obj_1:
        res_1 += el
    return res_1


print(get_sum_1(lst_obj))


@decor
def get_sum_2(lst_obj_2):
    lst_obj_2 = lst_obj_2
    res_1 = 0
    for el in lst_obj_2:
        res_1 += el
    gc.collect()
    return res_1


print(get_sum_2(lst_obj))

'''Использование модуля gc.collector сильно экономит память. Также замена списка на кортеж уменьшает количество 
используемой паняти. '''


@decor
def pers_info_1():
    namedtuple_ = namedtuple('test_1', 'name surname numbers address')
    info_1 = namedtuple_(name='Pavel', surname='Rachmanov', numbers=[el for el in range(10000)], address='Krasnaya 55')
    return info_1


@decor
def pers_info_2():
    recordclass_ = recordclass('test_2', ('name', 'surname', 'numbers', 'address'))
    info_2 = recordclass_(name='Nikita', surname='Pogromov', numbers=[el for el in range(10000)], address='Pobedy 11')
    return info_2


pers_info_1()
pers_info_2()
'''Переменные recordclass действительно используют меньше места по сравнению с namedtuple, 
особенно при работе с большими объемами данных '''


@decor
def numpy_array():
    test_1 = array([el for el in range(1000000)])
    return test_1


@decor
def arr_():
    test_2 = list(el for el in range(1000000))
    return test_2


numpy_array()
arr_()
'''Модуль NumPy array хорошо оптимизирован и использует меньше памяти, чем обычный список'''
