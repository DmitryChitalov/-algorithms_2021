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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = []
    for id, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(id)
    return new_arr


def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_4(nums):
    return [id for id, val in enumerate(nums) if val % 2 == 0]


num_list = [randint(0, 100) for i in range(30)]
# Функция range() позволяет получить только индексы элементов списка, значение приходится получать отдельной операцией.
print(func_1(num_list))
print(timeit("func_1(num_list)", globals=globals()))

# Функция enumerate() позволяет сразу получить индекс элемента и его значение, поэтому работает немного быстрее.
print(func_2(num_list))
print(timeit("func_2(num_list)", globals=globals()))

# LC выигрывает по времени у цикла, потому что не использует метод append.
print(func_3(num_list))
print(timeit("func_3(num_list)", globals=globals()))

# LC в паре с enumerate() работает быстрее всего.
print(func_4(num_list))
print(timeit("func_4(num_list)", globals=globals()))

"""
range           2.7529065 seconds
enumerate       2.6624682 seconds
range lc        2.3488784 seconds
enumerate lc    2.2723638 seconds
"""
