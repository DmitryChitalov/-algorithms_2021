"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""


from timeit import default_timer, timeit
from random import randint


def decor(n):
    def time_it(func):
        def wrapper(numb):
            res = 0
            for el in range(n):
                start_time = default_timer()
                func(numb)
                delta = default_timer() - start_time
                res += delta
            return res
        return wrapper
    return time_it


@decor(100000)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor(100000)
def func_2(nums):
    new_arr = [el for el in range(len(nums)) if nums[el] % 2 == 0]
    return new_arr


@decor(100000)
def func_3(nums):
    new_arr = [el for el, num in enumerate(nums) if num % 2 == 0]
    return new_arr


lst = [randint(0, 100) for el in range(100)]
print(f'Время выполнения функуии №1 - {func_1(lst)}')
print(f'Время выполнения функуии №2 - {func_2(lst)}')
print(f'Время выполнения функуии №3 - {func_3(lst)}')

'''
Функция 2 - list comprehension лучше, так как не надо создавать пустой массив и постоянно добавлять новые элементы с помощью append
Функция 3 - enumerate еще лучше, так как enumerate сразу возвращает элемент и индекс первичного массива 
'''