"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
"""

import memory_profiler
import numpy as np


def decor(func):
    def wrapper():
        m1 = memory_profiler.memory_usage()
        res = func()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def func_1():
    nums = [el for el in range(1000)]
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def func_2():
    nums_array = np.array([el for el in range(1000)])
    new_arr = np.array([])
    for i in range(len(nums_array)):
        if nums_array[i] % 2 == 0:
            np.append(new_arr, i)
    return new_arr


print(f' Память при использовании обычного списка: {func_1()[1]}')
print(f' Память с использованием быблиотеки numpy: {func_2()[1]}')

""" По замерам видно, что при использовании библиотеки NumPy памяти задействуется 
гораздо меньше, чем при использовании обычного списка. Чем больше объём массива, тем 
эффективнее использование NumPy"""