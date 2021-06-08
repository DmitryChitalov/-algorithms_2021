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

my_list = list(range(50))


def func_1(nums):  # О(n) - линейная сложность
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# переписываем функцию с ипользованием list comprehensions
# сложность одна, но list comprehensions определяет список и его содержимое одновременно, не вызывает append, => быстрее


def func_2(nums):  # О(n) - линейная сложность
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


print(timeit("func_1(my_list)", globals=globals()))  # 14.6468001
print(timeit("func_2(my_list)", globals=globals()))  # 8.010286200000001
