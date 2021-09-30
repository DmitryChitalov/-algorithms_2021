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

setup = 'numbers = [i for i in range(100)]'
# numbers = [i for i in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]  # <range_iterator object at 0x00...>
    return new_arr


def func_3(nums):
    new_arr = []
    gen = (i for i in range(0, len(nums)) if nums[i] % 2 == 0)  # <generator object func_3.<locals>.<genexpr> at 0x0..>
    while True:
        try:
            new_arr.append(next(gen))
        except StopIteration:
            break
    return new_arr


# print(func_1(numbers))
print(timeit('func_1(numbers)', globals=globals(), setup=setup))
# print(func_2(numbers))
print(timeit('func_2(numbers)', globals=globals(), setup=setup))
# print(func_3(numbers))
print(timeit('func_3(numbers)', globals=globals(), setup=setup))
