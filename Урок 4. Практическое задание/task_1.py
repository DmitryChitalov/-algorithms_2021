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
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" -
list comprehension.
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_optimized(nums):
    """List comprehensions быстрее заполнения через цикл,
    предполагаю это потому что не вызывается метод append()
    как в цикле на каждой итерации, поэтому func_optimized_1
    в целом быстрее."""
    return [i for i in range(len(nums)) if not nums[i] % 2]


MY_LIST = list(range(50))

print(timeit('func_1(MY_LIST)', globals=globals()))             # 5.252438682000502
print(timeit('func_1_optimized(MY_LIST)', globals=globals()))   # 3.744981834999635
