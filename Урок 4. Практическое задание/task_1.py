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


def func_1(nums):  # O(n)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # O(n)
    return [i for i, el in enumerate(nums) if el % 2 == 0]


my_nums = [el for el in range(1000)]
print("Количество запусков - 1 000:")
print("func_1:", timeit("func_1(my_nums)", globals=globals(), number=1000))
print("func_2:", timeit("func_2(my_nums)", globals=globals(), number=1000))
print("\nКоличество запусков - 10 000:")
print("func_1:", timeit("func_1(my_nums)", globals=globals(), number=10000))
print("func_2:", timeit("func_2(my_nums)", globals=globals(), number=10000))
print("\nКоличество запусков - 100 000:")
print("func_1:", timeit("func_1(my_nums)", globals=globals(), number=100000))
print("func_2:", timeit("func_2(my_nums)", globals=globals(), number=100000))

"""
Количество запусков - 1 000:
func_1: 0.169084162
func_2: 0.109573213

Количество запусков - 10 000:
func_1: 1.462735754
func_2: 1.136822446

Количество запусков - 100 000:
func_1: 14.851849260999998
func_2: 11.134291457

Во втором варианте функции применен итератор списка, что позволило сократить время выполнения.
"""
