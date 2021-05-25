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
    new_arr = [el for el in nums if el % 2 == 0]
    return new_arr

if __name__ == '__main__':
    nums = [el for el in range(100)]
    print(timeit("func_1(nums)", globals=globals())) # 9.0366333
    print(timeit("func_2(nums)", globals=globals())) # 5.5534806

# Генератор массива работает быстрее, нежели создание пустого массива и наполнение его через цикл.
