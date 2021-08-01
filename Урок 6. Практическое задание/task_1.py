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
import gc
import memory_profiler
from numpy import array

list_obj = [el for el in range(1000000)]
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
def list_get_sum(lst):
    total = 0
    for el in lst:
        total += el
    return total


@decor
def list_get_sum_cllect(lst):
    lst_obj_2 = lst
    res_1 = 0
    for el in lst_obj_2:
        res_1 += el
    gc.collect()
    return res_1


@decor
def info_person():
    namedtuple_ = namedtuple('test', 'name surname numbers address')
    state_info = namedtuple_(name='Pavel', surname='Rachmanov', numbers=[el for el in range(10000)], address='Krasnaya 55')
    return state_info


@decor
def info_person_rec_class():
    recordclass_ = recordclass('test_2', ('name', 'surname', 'numbers', 'address'))
    state_info = recordclass_(name='Nikita', surname='Pogromov', numbers=[el for el in range(10000)], address='Pobedy 11')
    return state_info


@decor
def array_numpy():
    test_array = array([el for el in range(1000000)])
    return test_array


@decor
def array_simple():
    test_array = list(el for el in range(1000000))
    return test_array


print(list_get_sum(list_obj))
print(list_get_sum_cllect(list_obj))
'''Использование модуля gc.collector экономит память. Также если заменить списка на кортеж уменьшает кольчество 
используемой паняти. '''

info_person()
info_person_rec_class()
'''Переменные recordclass используют меньше места по сравнению с namedtuple, 
особенно это заметно при работе с большими объемами данных '''


array_numpy()
array_simple()
'''Модуль NumPy array хорошо оптимизирован и использует меньше памяти, чем обычный список'''