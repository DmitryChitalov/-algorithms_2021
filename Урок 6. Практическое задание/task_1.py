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

import time
import memory_profiler
from random import randint
from memory_profiler import profile
from pympler import asizeof
import numpy


def time_memory_tracker(func):
    def time_memory_tracker_wrapper(*args, **kwargs):
        start_val = time.time()
        m1 = memory_profiler.memory_usage()
        func_res = func(*args, **kwargs)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib, {time.time() - start_val} sec")
        return func_res
    return time_memory_tracker_wrapper


'''
First function
Вывод: Функция с использованием генератора занимает меньше памяти, потому что генератор выдаёт значения по запросу, 
в отличии от первой реализации, которая хранит массив в памяти.
Время выполнения функции практически не отличается.
'''
print('First Function', '\n')


@time_memory_tracker
def list_odds1(playlist):

    list_odd = []
    for i in range(len(playlist)):
        if playlist[i] % 2 != 0:
            list_odd.append(playlist[i])
    return list_odd
# Выполнение заняло 0.0234375 Mib, 0.20978236198425293 sec


@time_memory_tracker
def list_odds2(playlist):

    for i in range(len(playlist)):
        if playlist[i] % 2 != 0:
            yield playlist[i]
# Выполнение заняло 0.0 Mib, 0.20178842544555664 sec


@profile
def list_odds3(playlist):

    list_odd = []
    for i in range(len(playlist)):
        if playlist[i] % 2 != 0:
            list_odd.append(playlist[i])
    return list_odd


@profile
def list_odds4(playlist):

    for i in range(len(playlist)):
        if playlist[i] % 2 != 0:
            yield playlist[i]


test_list = [randint(-100, 100) for _ in range(100000)]
list_odds1(test_list)
list_odds2(test_list)
list_odds3(test_list)
list_odds4(test_list)

'''
Second function
Вывод: Использование слотов сокращает объём занимаемой памяти в 3 раза.
'''

print('\n', 'Second Function')


class Character:

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character("Elf", damage=20, armor=40)

print(f'{unit.race} size {asizeof.asizeof(unit)}')


class Character:
    __slots__ = ('race', 'damage', 'armor')

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character("Orc", damage=30, armor=30)
print(f'{unit.race} size {asizeof.asizeof(unit)}')


'''
Third function
Вывод: Profiler не дал видимых результатов, но asizeof показывает, что библиотека numpy сокращает 
использование памяти третьей функции в 5 раз.
'''

print('\n', 'Third Function')


@time_memory_tracker
def lower_upper1(alph):
    upper_keys = [i.lower() for i in alph if i.isupper()]
    return upper_keys


@time_memory_tracker
def lower_upper_numpy1(alph):
    upper_keys = numpy.array([i.lower() for i in alph if i.isupper()])
    return upper_keys


@profile
def lower_upper2(alph):
    upper_keys = [i.lower() for i in alph if i.isupper()]
    return upper_keys


@profile
def lower_upper_numpy2(alph):
    upper_keys = numpy.array([i.lower() for i in alph if i.isupper()])
    return upper_keys


alph1 = 'agdgAFDSFdahdadgaAGGDFSFShhadhadha'

upper_keys1 = [i.lower() for i in alph1 if i.isupper()]
upper_keys2 = numpy.array([i.lower() for i in alph1 if i.isupper()])

print(lower_upper1(alph1))
print(lower_upper2(alph1))
print(lower_upper_numpy1(alph1))
print(lower_upper_numpy2(alph1))
print(f'Без numpy {asizeof.asizeof(upper_keys1)} байт')
print(f'С использованием numpy {asizeof.asizeof(upper_keys2)} байт')
