"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import repeat, default_timer

# до запуска замеров выполняем построение массива
setup = """
from __main__ import func_1, func_2, nums
"""

nums=range(2000)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


print(f'Test for same result: func_1(nums) == func_2(nums) # {func_1(nums) == func_2(nums)}')

# [0.411483314, 0.39288760799999994, 0.4017827290000001]
print(repeat("func_1(nums)", setup, default_timer, 3, 1000))
# [0.24859392800000002, 0.2452237180000001, 0.24673148900000008]
print(repeat("func_2(nums)", setup, default_timer, 3, 1000))

# Вывод: func_2 быстрее, потому что используется встроенная функция filter
