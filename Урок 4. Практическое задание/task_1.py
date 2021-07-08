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

import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    t = [i for i, el in enumerate(nums) if el % 2 == 0]
    return t

nums = [i for i in range(10000)]

t = (timeit.timeit("func_1(nums)", globals=globals(), number=1000))
print(f'Результат func_1 при 10000: {t}')

t2 = (timeit.timeit("func_2(nums)", globals=globals(), number=1000))
print(f'Результат func_2 при 10000: {t2}')

nums2 = [i for i in range(1000)]

t = (timeit.timeit("func_1(nums2)", globals=globals(), number=1000))
print(f'Результат func_1 при 1000: {t}')

t2 = (timeit.timeit("func_2(nums2)", globals=globals(), number=1000))
print(f'Результат func_2 при 1000: {t2}')

#Результат func_1 при 10000: 0.8869057
#Результат func_2 при 10000: 0.6062344000000001
#Результат func_1 при 1000: 0.07803819999999995
#Результат func_2 при 1000: 0.06003230000000004
