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
from timeit import timeit
array = [0,1,2,3,4,5,6,7,8,9]
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr2 = [el for el in range(len(nums)) if el % 2 == 0]
    return new_arr2

def func_3(nums):
    new_arr3 = list(filter(lambda x: not nums[x] % 2, range(len(nums))))
    return new_arr3

print(func_1(array))
print(func_2(array))
print(func_3(array))
print(timeit("func_1", globals=globals()))
print(timeit("func_2", globals=globals()))
print(timeit("func_3", globals=globals()))

""" 
  func_1  0.025647400000000004
  func_2  0.0232681
  func_3  0.019780300000000015
  
  Для оптимизации были использованы варианты: list comprehension и встроенные функции. list comprehension быстрее 
  append, но встроенные функции, а в особенности lambda еще быстрее, что и следует из замеров.
"""