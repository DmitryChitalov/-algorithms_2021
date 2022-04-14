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

my_setup = 'nums = [n  for n in range(1000)]'

test_code = '''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
'''

test_code_my = '''
def func_1(nums):
    new_arr = []
    for i, v in enumerate(nums):
        if v % 2 == 0:
            new_arr.append(i)
    return new_arr
'''

test_code_my_2 = '''
def func_1(nums):
    new_arr = [i for i  in enumerate(nums) if v & 1 == 0]
    return new_arr
'''

print(timeit(test_code, setup=my_setup, number=1000000))
print(timeit(test_code_my, setup=my_setup, number=1000000))
print(timeit(test_code_my_2, setup=my_setup, number=1000000))

'''АНАЛИТИКА: полученные результаты: 
0.08731704500000001 для исходного кода 
0.07862293500000002 для оптимизированного с enumerate       
0.08214786899999998 для оптимизированного с enumerate и генератором 


Вывод: использование enumerate (прямого перебора) быстрее, не надо формировать массив индексов
использование побитового сравнения  возможно дает небольшой прирост

 
'''
