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


def func_2(nums):
    # list comprehension
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    # list comprehension + enumerate
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(f'{5 * "*"}1000{5 * "*"}')
my_list = [el for el in range(1000)]
func_list = ['func_1', 'func_2', 'func_3']
for func in func_list:
    print(f'Функция {func}:', timeit.timeit(func + '(my_list)', number=1000, globals=globals()))
print(f'{5 * "*"}10000{5 * "*"}')
# 10000
my_list = [el for el in range(10000)]
func_list = ['func_1', 'func_2', 'func_3']
for func in func_list:
    print(f'Функция {func}:', timeit.timeit(func + '(my_list)', number=1000, globals=globals()))
print(f'{5 * "*"}100000{5 * "*"}')
# 100000
my_list = [el for el in range(100000)]
func_list = ['func_1', 'func_2', 'func_3']
for func in func_list:
    print(f'Функция {func}:', timeit.timeit(func + '(my_list)', number=1000, globals=globals()))

"""
*****1000*****
Функция func_1: 0.1058539
Функция func_2: 0.07406679999999999
Функция func_3: 0.09814900000000001
*****10000*****
Функция func_1: 1.2394902
Функция func_2: 0.8881659000000002
Функция func_3: 0.9372547
*****100000*****
Функция func_1: 14.745923699999999
Функция func_2: 11.9250279
Функция func_3: 14.097612299999998

Все функции О(n) - линейная сложность
Списковые включения отрабатывают быстрее, чем привычная реализация итераторов
"""
