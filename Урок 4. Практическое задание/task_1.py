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


my_list = [i for i in range(100, 200)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit('func_1(my_list)', globals=globals(), number=100000))    # 2.7371083339999998


def func_2(nums):
    new_arr = [nums[i] % 2 == 0 for i in range(len(nums))]
    return new_arr


print(timeit('func_2(my_list)', globals=globals(), number=100000))    # 2.7464031899999997


# Код сделан более лаконичным и читабельным, но время выполнения осталось тем же
# поскольку не изменилась сложность (O(n))