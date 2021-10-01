"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что  часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums_list_1000 = [i for i in range(1000)]

print(f'func_1: ', timeit("func_1(nums_list_1000)", globals=globals(), number=1000))
print(f'func_2: ', timeit("func_2(nums_list_1000)", globals=globals(), number=1000))

nums_list_10000 = [i for i in range(10000)]

print(f'func_1: ', timeit("func_1(nums_list_10000)", globals=globals(), number=1000))
print(f'func_2: ', timeit("func_2(nums_list_10000)", globals=globals(), number=1000))

nums_list_100000 = [i for i in range(100000)]

print(f'func_1: ', timeit("func_1(nums_list_100000)", globals=globals(), number=1000))
print(f'func_2: ', timeit("func_2(nums_list_100000)", globals=globals(), number=1000))

'''
func_1:  0.131239027
func_2:  0.114249716
func_1:  1.264128542
func_2:  1.104775328
func_1:  12.522361082
func_2:  11.800733613000002'''

""" Лучший результат с использованием функции list comprehension т. к. list comprehension быстрее цикла"""
