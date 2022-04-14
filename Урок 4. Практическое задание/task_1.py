"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(func_1(my_array))
print(
    timeit(
        "func_1(my_array)",
        globals=globals(),
        number=1000))


def func_2(nums):
    new_arr = []
    index = 0
    while len(nums) != 0:
        el = nums.pop(0)
        if el % 2 == 0:
            new_arr.append(index)
        index += 1
    return new_arr


print(func_2(my_array))
print(
    timeit(
        "func_2(my_array)",
        globals=globals(),
        number=1000))

"""
0.0016161999999999982 время func_1
0.00022669999999999635 время func_2

Стало быстрее потому что на вход цикла подается массив уменьшающийся
с каждой итерацией. 
"""