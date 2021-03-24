"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
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
    new_arr = [i for i in range(len(nums)) if nums[i] %2 == 0]
    return new_arr

def func_3(nums):
    i = 1
    while i<len(nums):
        if nums[i] % 2 == 0:
            yield i
        i += 1

test_list = [randint(0, 10) for i in range(100)]

print(f'func_1 (append): {timeit("func_1(test_list)", globals=globals())} sec')
# 8.086010339000001 sec
print(f'func_2 (LC): {timeit("func_2(test_list)", globals=globals())} sec')
# 6.844087231 sec
print(f'func_3 (gen): {timeit("func_3(test_list)", globals=globals())} sec')
# 0.2247257059999992 sec

# оптимизовароли путем использования list comprehension.
# скорость выполнения уменьшилась на 15%
# при использовании генератора время уменьшается на порядок, т.к. не создаются никакие ообъекты,
# но использование генератора в данном случае нецелесообразно, ибо по нему можно пройтись только 1 раз