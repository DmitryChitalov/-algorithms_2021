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


import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


NUMS = [el for el in range(1000)]

print(
    timeit.timeit(
        "func_1(NUMS)[:]",
        globals=globals(),
        number=1000
    )
)

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000
    )
)

NUMS = [el for el in range(10000)]

print(
    timeit.timeit(
        "func_1(NUMS)[:]",
        globals=globals(),
        number=1000
    )
)

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000
    )
)


"""
Result of 1000:
0.06270379999999999
0.0562391

Result of 10000:
0.6045868
0.536832

"""
