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
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


numbers = [i for i in range(1, 100)]
print(timeit('func_1(numbers)', number=1000, globals=globals()))


def update_func_1(nums):
    lister = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return lister


print(timeit('update_func_1(numbers)', number=1000, globals=globals()))

# Время стало меньше , так как во второй функции мы не использовали 'append' , а сразу создавали список