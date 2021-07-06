"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами
списков, на самом деле к генераторам отношения не имеет. Это называется
"списковое включение" - list comprehension.
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    yield (i for i in nums if i % 2 == 0)

def func_3(nums):
    return [i for i in nums if i % 2 == 0]


arr_basic = [i for i in range(100000)]

print(timeit('func_1(arr_basic)', globals=globals(), number=1000))
print(timeit('func_2(arr_basic)', globals=globals(), number=1000))
print(timeit('func_3(arr_basic)', globals=globals(), number=1000))

