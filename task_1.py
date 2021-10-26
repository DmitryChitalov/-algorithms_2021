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
from timeit import Timer

def func_1(nums):
    new_arr = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    my_lst = [i for i in range(len(nums)) if i % 2 == 0]
    return my_lst

nums = [n for n in range(1000)]

print('-' * 20, '1000 - запусков')
#0.18646940001053736
#0.0786041000392288


print(
    timeit.timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000))

print('-' * 20, '10000 - запусков')
#1.2108843000023626
#0.7641952999983914


nums = [n for n in range(10000)]

print(
    timeit.timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000))

print('-' * 20, '100000 - запусков')
#11.715144099958707
#7.621133599954192


nums = [n for n in range(100000)]

print(
    timeit.timeit(
        "func_1(nums)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(nums)",
        globals=globals(),
        number=1000))

"""
Оптимизировал алгоритм с помощью спискового включения рассмотренного на уроке, так как оно
выполняются быстрее и выглядет лаконичнее занимая меньше строк кода, 
"""