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
import random

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_gen(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

def func_gen_enum(nums):
    return [i for i, n in enumerate(nums) if n % 2 == 0]

test_arr = [random.randint(1, 100) for i in range(10000)]

print('Функция из задания:', timeit("func_1(test_arr)", globals=globals(), number=1000))
print('Функция c генератором:', timeit("func_gen_enum(test_arr)", globals=globals(), number=1000))
print('Функция c генератором и счетчиком:', timeit("func_gen_enum(test_arr)", globals=globals(), number=1000))

"""
Функция из задания: 0.826497
Функция c генератором: 0.6844592
Функция c генератором и enumerate: 0.7028129000000001

Если заменить обход списка в цикле на генератор, то получается быстрее.
Вероятно из-за особенностей вызова в цикле append против заточенной под это структуры генератора списков

Если к генератору добавить enumerate, то время чуть увеличивается. 
Предполагаю из-за времени создания кортежа счетчиком
"""