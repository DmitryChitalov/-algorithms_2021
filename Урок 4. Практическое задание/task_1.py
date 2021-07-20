"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
from timeit import timeit

m_num = [x + 1 for x in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for i in nums:
        if i % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_3(nums):
    return [x for x in nums if x % 2 == 0]


def func_4(nums):
    for x in nums:
        if x % 2 == 0:
            yield x


print("func_1: ", timeit(stmt="func_1(m_num)", globals=globals()))
print("func_2: ", timeit(stmt="func_2(m_num)", globals=globals()))
print("func_3: ", timeit(stmt="func_3(m_num)", globals=globals()))
print("func_4: ", timeit(stmt="func_4(m_num)", globals=globals()))

"""
Выводы:
func_1:  17.2405951
func_2:  14.595693999999998
func_3:  7.915393699999996
func_4:  3.688588699999997

func_1 и func_2. func_2 работает быстрее чем func_1. В func_1 происходит взятие элемента по индексу, в func_2 
сам элемент.

В func_3 используется list comprehension. Работает быстрее чем func_1 и func_2.

В func_4 используется генератор. Показал самое лучшее время на 100 элементах массива. Если проверять на 10 элементах, 
генератор покажет самое худшее время.  
"""
