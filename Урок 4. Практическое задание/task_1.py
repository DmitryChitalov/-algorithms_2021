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

numbers = [i for i in range(100)]  # list comprehension для заполнения словаря


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_l_c(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_gen(nums):
    new_arr = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return new_arr


print(timeit("func_1(numbers)", globals=globals(), number=100000))
print(timeit("func_l_c(numbers)", globals=globals(), number=100000))
print(timeit("func_gen(numbers)", globals=globals(), number=100000))

'''
Использовал заполнение списка, помимо основной функции, с помощью LC и 
генераторного выражения. Осн. функция и LC показали примерно одинаковый 
результат, ввиду того, что по-сути они являются одним и тем же, только LC 
это "синтаксический сахар". А генераторное выражение оказалось на порядок 
быстрее остальных, т.к. перебирает только по 1 элементу, не работая со всем 
массивом сразу.  
'''
