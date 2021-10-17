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
from numpy import number

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


var_10 = [i for i in range(10)]
var_100 = [i for i in range(100)]
var_1000 = [i for i in range(1000)]

print('func_1(var_10): ')
print(timeit("func_1(var_10)", setup="from __main__ import func_1, var_10", number=100000))

print('func_1(var_100): ')
print(timeit("func_1(var_100)", setup="from __main__ import func_1, var_100", number=100000))

print('func_1(var_1000): ')
print(timeit("func_1(var_1000)", setup="from __main__ import func_1, var_1000", number=100000))

print('func_2(var_10): ')
print(timeit("func_2(var_10)", setup="from __main__ import func_2, var_10", number=100000))

print('func_2(var_100): ')
print(timeit("func_2(var_100)", setup="from __main__ import func_2, var_100", number=100000))

print('func_2(var_1000): ')
print(timeit("func_2(var_1000)", setup="from __main__ import func_2, var_1000", number=100000))

'''
оптимизация через list comprehensionЖ func_1.
Время исполнения на 100 000 вызовах функции: 
func_1(var_10): 
0.1458657
func_1(var_100): 
1.002916
func_1(var_1000): 
10.8262853
func_2(var_10): 
0.15093350000000072
func_2(var_100): 
0.9348941999999987
func_2(var_1000): 
10.130414099999998

List comprehension оптимально использовать при большем количестве элементов
       Цикл работает немного быстрее чем List comprehension.
'''