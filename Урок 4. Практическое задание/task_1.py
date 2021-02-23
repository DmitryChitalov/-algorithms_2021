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
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


my_list = [i for i in range(1000000)]

t1 = timeit.Timer('func_1(my_list)', 'from __main__ import func_1', globals=globals())
print("func_1 work time", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer('func_2(my_list)', 'from __main__ import func_2', globals=globals())
print("func_2 work time", t2.timeit(number=1000), "milliseconds")


"""
func_1 work time 78.61617981101153 milliseconds
func_2 work time 68.91136887902394 milliseconds

LC - это просто «синтаксический сахар» для обычного for цикла. 
В этом случае причина того, что он работает лучше, заключается в том, что ему не нужно загружать атрибут append списка\
и вызывать его как функцию на каждой итерации. 
Другими словами и в целом составление списка выполняется быстрее, потому что приостановка и возобновление фрейма 
функции или нескольких функций в других случаях происходит медленнее, чем создание списка по запросу.
"""