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
    new_arr = []
    i = 0
    for el in nums:
        if el % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr

NUMS = [el for el in range(10000)]


print(f'func_1 {min(timeit.repeat("func_1(NUMS)", globals=globals(),number = 1000))}')
print(f'func_2 {min(timeit.repeat("func_2(NUMS)", globals=globals(),number = 1000))}')

""" Перебор элементов в списке происходит быстрее, чем перебор индексов и в последующем обращение по индексу"""