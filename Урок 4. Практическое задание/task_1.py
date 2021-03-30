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

nums = [i for i in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            #  Итератор с функцией append
            new_arr.append(i)
    return new_arr


def func_2(nums):
    #  Списковое включение (list comprehension) работает быстрее, чем итератор с функцией append
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

def func_3(nums):
    #  Списковое включение (list comprehension) перебор по массиву работает быстрее, чем используя функцию range()
    return [i for i in nums if i % 2 == 0]

print('Время выполнения func_1:')
print(timeit(stmt="func_1(nums)",
             setup="from __main__ import func_1, nums",
             number=1000))

print('Время выполнения func_2:')
print(timeit(stmt="func_2(nums)",
             setup="from __main__ import func_2, nums",
             number=1000))

print('Время выполнения func_3:')
print(timeit(stmt="func_3(nums)",
             setup="from __main__ import func_3, nums",
             number=1000))

'''
Время выполнения func_1:
1.0070794369999998
Время выполнения func_2:
0.7838160270000001
Время выполнения func_3:
0.5019385249999999

По результатам выполнения видно что list comprehension работает быстрее простого итератора, плюс в данном случае
можно ускорить list comprehension за счет избавления от функции range и len, выполнив перебор сразу по элементам, 
а не по полученым из range индексам
'''