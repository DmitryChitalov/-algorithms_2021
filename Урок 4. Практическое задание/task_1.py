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
from timeit import repeat


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_list_comp(nums):
    return [i for i in nums if i % 2 == 0]


def func_set_comp(nums):
    return tuple(i for i in nums if i % 2 == 0)


def func_gen_comp(nums):
    return (i for i in nums if i % 2 == 0)


def func_dict_comp(nums):
    return {i for i in nums if i % 2 == 0}


nums = [i for i in range(1000)]
print(f"Функция func_1, время {repeat('func_1(nums)', 'from __main__ import func_1, nums', repeat=3, number=10000)}")
print(f"Функция func_list_comp, время {repeat('func_list_comp(nums)', 'from __main__ import func_list_comp, nums', repeat=3, number=10000)}")
print(f"Функция func_set_comp, время {repeat('func_set_comp(nums)', 'from __main__ import func_set_comp, nums', repeat=3, number=10000)}")
print(f"Функция func_gen_comp, время {repeat('func_gen_comp(nums)', 'from __main__ import func_gen_comp, nums', repeat=3, number=10000)}")
print(f"Функция func_dict_comp, время {repeat('func_dict_comp(nums)', 'from __main__ import func_dict_comp, nums', repeat=3, number=10000)}")

'''
Стартовая функция и ее результаты:
Функция func_1, время [1.2471133, 1.0971981000000002, 1.1107927999999996]
Функция с использованием спискового включения:
Функция func_list_comp, время [0.5831778999999999, 0.6235343000000002, 0.5941419999999997]
Функция с использованием кортежного включения:
Функция func_set_comp, время [0.7774116000000006, 0.7077258999999998, 0.7944626000000001]
Функция с использованием генераторного включения:
Функция func_gen_comp, время [0.003441700000000658, 0.003303300000000675, 0.0033007999999998816]
Функция с использованием словарного включения:
Функция func_dict_comp, время [0.7152289999999999, 0.5828351999999999, 0.6737114999999996]
Кортежное включение и генераторное похожи, но когда не указываешь явно Tuple, 
то происходит возврат Генераторного включения.
Если опустить момент с явным указанием Кортежа, то Кортежное/Генераторное включения являются неоспоримыми победителями.
Кортеж быстрее списка так, как он неизменяемый и легче списка. 
'''