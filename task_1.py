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
from copy import deepcopy
from timeit import default_timer
import memory_profiler


#===========================================

def create_dict_1():
    """Через цикл"""
    classic_dict = {}
    for i in range(10000):
        classic_dict[i] = i
    return classic_dict


def create_dict_2():
    """Однострочное"""
    classic_dict = {i: i for i in range(10000)}
    #classic_dict = None
    return classic_dict

print('Создание словаря')
start = default_timer()
before  = memory_profiler.memory_usage()
create_dict_1()
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

print('Оптимизированное оздание словаря')
start = default_timer()
before  = memory_profiler.memory_usage()
create_dict_2()
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

"""
Оба словаря создаются одинаковое количество времени однако 
однострочный вариант занимает намного меньше места

Создание словаря
	Используемая память - 0.11328125 MiB
	Время выполнения - 0.21866030000000003 cек

Оптимизированное оздание словаря
	Используемая память - 0.0 MiB
	Время выполнения - 0.21802669999999996 cек
"""


#===========================================

from collections import deque

def create_deque_1():
    """Не освобождаем"""
    dq = deque(a for a in range(100000))
    return dq


def create_deque_2():
    """Освобождаем"""
    dq = deque(a for a in range(100000))
    cop = deepcopy(dq)
    del dq
    cop = None
    return cop

#===========================================

from random import random
array = [int(random()*5) for i in range(10000)]
def func_1():
    """Медленный поиск самого частого числа"""
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    new_array = None
    return elem

def func_2():
    """Оптимизированный поиск самого частого числа"""
    a_set = set(array)

    most_common = None
    qty_most_common = 0

    for item in a_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    return most_common

print('Не оптимизированный поиск самого частого числа в словаре')
start = default_timer()
before  = memory_profiler.memory_usage()
func_1()
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

print('Оптимизированный поиск самого частого числа в словаре')
start = default_timer()
before  = memory_profiler.memory_usage()
func_2()
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

"""
Данным методом получилось оптимизировать время выполнения с 2 сек до 0,2 сек
также оптимизировать память 

Не оптимизированный поиск самого частого числа в словаре
	Используемая память - 0.078125 MiB
	Время выполнения - 2.0499289999999997 cек

Оптимизированный поиск самого частого числа в словаре
	Используемая память - 0.0 MiB
	Время выполнения - 0.21597869999999997 cек
"""

#===========================================


def revers_base(m):
    def nums(user_number):

        while user_number != 0:
            numbers = user_number % 10
            user_number = user_number // 10
            #print(numbers, end = '')
            return nums(user_number)
    return nums(m)


def revers_optimaze(n):     # оптимизирванный метод "переворота" числа
    return ''.join([i for i in str(n)[::-1]])


print('Рекурсивный переворот числа')
start = default_timer()
before  = memory_profiler.memory_usage()
revers_base(123456789012345678901234567890123456789012345678901234567890)
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

print('Оптимизированый переворот числа')
start = default_timer()
before  = memory_profiler.memory_usage()
revers_optimaze(123456789012345678901234567890123456789012345678901234567890)
after  = memory_profiler.memory_usage()
end = default_timer()
print(f'\tИспользуемая память - {after[0] - before[0]} MiB')
print(f'\tВремя выполнения - {end - start} cек')
print()

"""
Скорости выполнения у обоих методов одинаковые одинаковые 
но срез занимает памятив разы меньше

Рекурсивный переворот числа
	Используемая память - 0.00390625 MiB
	Время выполнения - 0.21850619999999976 cек

Оптимизированый переворот числа
	Используемая память - 0.0 MiB
	Время выполнения - 0.2158547000000004 cек
"""
