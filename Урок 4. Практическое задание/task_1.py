"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# list comprehension
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# filter(function, iterable)
def func_3(nums):
    return filter(lambda i: nums[i] % 2 == 0, range(len(nums)))


n = [i for i in range(100000)]

print(timeit("func_1(n)", globals=globals(), number=10000))
print(timeit("func_2(n)", globals=globals(), number=10000))
print(timeit("func_3(n)", globals=globals(), number=10000))

'''
96.1870244 классический for
73.78999460000001 - list comprehension
0.005230399999987867 - функция filter

Было испробовано два других способа для выполнения задачи.

Явно list comprehension справляется лучше чем просто цикл for с условием.
НО вот filter бьет все рекорды. Единственное что непонятно что в документации написано:

Note that filter(function, iterable) is equivalent to the 
generator expression (item for item in iterable if function(item)) if function is not None 
and (item for item in iterable if item) if function is None.

Вот только цифры показывают что эквивалентного в них маловато, так как скорость обработки filter
заметно выше.
'''
