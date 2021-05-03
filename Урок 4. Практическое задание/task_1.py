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

from timeit import Timer
import random


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)

    return new_arr


def func_2(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)

    return new_arr


def func_3(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if el & 1 == 0:
            new_arr.append(i)

    return new_arr


def func_4(nums):

    return [i for i, el in enumerate(nums) if el % 2 == 0]


lst_to_func = [random.randint(0, i) for i in (range(1000))]
# Исходный вариант
t1 = Timer("func_1(lst_to_func)", "from __main__ import func_1, lst_to_func")
print('t1', t1.timeit(number=100000))

# При использовании enumerate очень небольшой прирост производительности, либо его нет совсем
t2 = Timer("func_2(lst_to_func)", "from __main__ import func_2, lst_to_func")
print('t2', t2.timeit(number=100000))

# Использование двоичного представления числа прироста не дало
t3 = Timer("func_3(lst_to_func)", "from __main__ import func_3, lst_to_func")
print('t3', t3.timeit(number=100000))

# Использование генератора списка - прирост производительности примерно на 20% от исходного варианта
t4 = Timer("func_4(lst_to_func)", "from __main__ import func_4, lst_to_func")
print('t4', t4.timeit(number=100000))

# Вывод: необходимо использовать генераторы списков

# t1 10.234653216
# t2 9.665983459000001
# t3 12.530917842000004
# t4 8.179271434999997

# t1 10.526913093000001
# t2 10.694684525
# t3 12.204086298999997
# t4 8.058193519999996

# t1 10.34976222
# t2 9.959199259
# t3 11.869916353000004
# t4 7.919031464

# t1 10.349993749000001
# t2 10.657073914
# t3 12.153155914000003
# t4 8.262752485
