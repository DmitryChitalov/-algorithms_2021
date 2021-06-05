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
from random import randint


"""
Исходная функция:  1.2637626000000002
Comprehension, enumerate:  0.9208752999999998
Comprehension, range(len()):  0.9807106999999999
Исходная с enumerate:  1.2022678000000004
Выделение памяти заранее, append 1.0754155
Выделение памяти заранее, обращение по индексу 1.2878393
Генератор:  1.1742811999999994
"""

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Написала comprehension с функцией enumerate. Алгоритм сильно ускорился - на 0.3
# (для 1000 запусков на 10000 значений массива)
def func_2(nums):
    return [i for i, n in enumerate(nums) if n % 2 == 0]


# Проверяю, что быстрее работает enumerate или range(len()) и обращение по индексу.
# В целом, кажется, что разницы нет, то одно быстрее, то другое. В этом конкретном замере enumerate быстрее.
def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Проверяю скорость работы enumerate в исходном варианте алгоритма.
# Здесь, почему-то c enumerate быстрее работает, а при некоторых запусках - исходная.
def func_4(nums):
    new_arr = []
    for i, n in enumerate(nums):
        if n % 2 == 0:
            new_arr.append(i)
    return new_arr


# Экспериментирую с preallocation, но существенного выигрыша во времени получить не получается.
# Получается только большой перерасход пямяти. Вариант с append работает быстрее, чем с обращением по индексу
# (скорее всего причина в том, что во втором варианте список нужно предварительно заполнить значениями).
def func_5(nums):
    new_arr = [] * len(nums)
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_6(nums):
    new_arr = [None] * len(nums)
    new_ind = 0
    for i, n in enumerate(nums):
        if n % 2 == 0:
            new_arr[new_ind] = i
            new_ind += 1
    return new_arr


# Использование генератора выигрыша во времени почти не дает или совсем не дает.
def get_ind_even(nums):
    for i, n in enumerate(nums):
        if n % 2 == 0:
            yield i


def func_7(nums):
    return [n for n in get_ind_even(nums)]


num_list = [randint(0, 100) for _ in range(10000)]
print('Исходная функция: ', timeit("func_1(num_list)", globals=globals(), number=1000))
print('Comprehension, enumerate: ', timeit("func_2(num_list)", globals=globals(), number=1000))
print('Comprehension, range(len()): ', timeit("func_3(num_list)", globals=globals(), number=1000))
print('Исходная с enumerate: ', timeit("func_4(num_list)", globals=globals(), number=1000))
print('Выделение памяти заранее, append', timeit("func_5(num_list)", globals=globals(), number=1000))
print('Выделение памяти заранее, обращение по индексу', timeit("func_6(num_list)", globals=globals(), number=1000))
print('Генератор: ', timeit("func_7(num_list)", globals=globals(), number=1000))

