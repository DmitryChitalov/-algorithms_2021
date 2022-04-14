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


# Исходная функция
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Доработанная функция
def func_2(nums):
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr


my_list = [1, 2, 3, 4, 5]

print(f'Время выполнения исходной функции: {timeit("func_1(my_list)", setup="from __main__ import func_1, my_list", number=1000000)}')
print(f'Время выполнения доработанной функции: {timeit("func_2(my_list)", setup="from __main__ import func_2, my_list", number=1000000)}')



"""
В исходной функции на каждой итерации осуществлялся поиск элемента по индексу.
В моем варианте скорость возросла за счет того, что мы только перебирали значения 
вместо поиска элемента по индексу, а для подсчета индекса был использован счетчик (пронумеровали элементы).

"""

