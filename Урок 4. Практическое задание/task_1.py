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


def func_2(nums):
    """
    Для оптимизации кода, как визуально так и технически, убрал append и заменил цикл на List comprehension.
    Выиграл около 3-х сотых секунды.
    """
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    ls = [i for i in range(0, 1000)]
    print(timeit('func_1(ls)', number=1000, globals=globals()))  # 0.1516096
    print(timeit('func_2(ls)', number=1000, globals=globals()))  # 0.1297608
