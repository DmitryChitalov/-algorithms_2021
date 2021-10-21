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
    new_arr = [i for i in nums if i%2 == 1]
    return new_arr


def func_3(nums):
    new_arr = list(map(lambda i: i % 2, nums))
    return new_arr


lst1 = range(10000)
print(timeit.repeat('func_1(lst1)', repeat=3, number=1000, globals=globals()))
print(timeit.repeat('func_2(lst1)', repeat=3, number=1000, globals=globals()))
print(timeit.repeat('func_3(lst1)', repeat=3, number=1000, globals=globals()))

"""
Лучший способ из приведённых выше это "списковые включения". Они работают быстрее чем добавлять по одному значению.
Чуть медленее работает через лямбду функцию.
"""

