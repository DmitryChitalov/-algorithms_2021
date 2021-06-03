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

"""
Вывод: несмотря на то что по О-нотации все три функции линейные, использование функции enumerate итерируется 
по и ндексу и по значению одновременно, и за счёт этого функия выполняется быстрее
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = [i for i, v in enumerate(nums) if v % 2 == 0]
    return new_arr


lst_nums = [-10, 20, 3, 4, 5, 6, 7]
print(timeit('func_1(lst_nums)', globals=globals()))
print(timeit('func_2(lst_nums)', globals=globals()))
print(timeit('func_3(lst_nums)', globals=globals()))
