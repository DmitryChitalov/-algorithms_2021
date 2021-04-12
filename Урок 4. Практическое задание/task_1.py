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
from timeit import Timer
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


#  альтернативный вариант c использованием генератора c range
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


#  альтернативный вариант c использованием цикла и enumerate
def func_3(nums):
    new_arr = []
    for i, x in enumerate(nums):
        if x % 2 == 0:
            new_arr.append(i)
    return new_arr


#  альтернативный вариант c использованием генератора c enumerate
def func_4(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


nums = [randint(1, 4) for _ in range(1, 100)]

t1 = Timer("func_1(nums)", globals=globals())
print("func_1(nums)", t1.timeit(number=2000000), "seconds")

t2 = Timer("func_2(nums)", globals=globals())
print("func_2(nums)", t2.timeit(number=2000000), "seconds")

t3 = Timer("func_3(nums)", globals=globals())
print("func_3(nums)", t3.timeit(number=2000000), "seconds")

t4 = Timer("func_4(nums)", globals=globals())
print("func_3(nums)", t4.timeit(number=2000000), "seconds")

"""
func_1(nums) 18.2194417 seconds
func_2(nums) 15.795209100000001 seconds
func_3(nums) 18.703642800000004 seconds
func_3(nums) 14.591228199999996 seconds

ВЫВОД:
Самый быстрый вариант - вариант 4 - генератор списка с использованием функции enumerate.
Генератор позволяет нам формировать новый список сразу при последовательном чтении элементов входящего списка без 
использования промежуточных присваиваний и/или дополнительных обращений к входящему списку.
"""
