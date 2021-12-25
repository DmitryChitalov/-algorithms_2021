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

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
import timeit

nums = [el for el in range(50)]
new_arr = []


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print('func_1', timeit.timeit('func_1(nums)', globals=globals()))


def func_2(nums):
    new_arr = [nums.index(el) for el in nums if el % 2 == 0]


print('func_2', timeit.timeit('func_2(nums)', globals=globals()))


def func3(nums):
    new_arr = (i for i in nums if i % 2 == 0)
    return new_arr


print('func3', timeit.timeit('func3(nums)', globals=globals()))


''''Самый быстрый способ это через func3 так как не используются  индексы и метод append'''

# range(50)
# func_1 3.6089214
# func_2 8.5285425

# range(100)
# func_1 6.8979052
# func_2 27.2357068

# range(20)
# func_1 1.6543335
# func_2 2.347499
