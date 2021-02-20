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
import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

list1 = [1,2,3,4,5,6,7,8,9,10]

print(timeit.repeat("func_1(list1)", globals=globals(), repeat=3))

#сменили всю функцию на списковое включение. Быстрее потчи в два раза, так как не требуется вызовы метода append
def func2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr

print(timeit.repeat("func2(list1)", globals=globals(), repeat=3))

#сменили списковое включение на генераторное выражение,
#выражение оказалось быстрее, так как оно не строит весь список сразу и не хранит его в памяти

def func3(nums):
    new_arr =(i for i in nums if i % 2 == 0)
    return new_arr

print(timeit.repeat("func3(list1)", globals=globals(), repeat=3))
