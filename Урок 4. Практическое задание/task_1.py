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

nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_lc(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_1_enum(nums):
    # new_arr = []
    # for ind, item in enumerate(nums):
    #     if item % 2 == 0:
    #         new_arr.append(ind)
    new_arr = [ind for ind, num in enumerate(nums) if num % 2 == 0]
    return new_arr


print(func_1(nums_list))
print(timeit("func_1(nums_list)", globals=globals()))
print(func_1_lc(nums_list))
print(timeit("func_1_lc(nums_list)", globals=globals()))
print(func_1_enum(nums_list))
print(timeit("func_1_enum(nums_list)", globals=globals()))


"""
Аналитика:

Функция с list comprehensions работает быстрей так как результат генерируется налету без складывания значений в массив 
и использования append. Функция с lc и enumerate еще быстрей из-за отсутствия необходимости обращаться к элементам 
по индексам.

"""