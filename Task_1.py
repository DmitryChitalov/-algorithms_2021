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


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

x = [i for i in range(100000)]
print(f'func_1(x): {timeit("func_1(x)", globals=globals(), number=1000)}')
print(f'func_2(x): {timeit("func_2(x)", globals=globals(), number=1000)}')

"""func_1(x): 29.1545175
func_2(x): 27.2405294
Для оптимизации использовал list comprehension, который работает быстрее, чем append"""