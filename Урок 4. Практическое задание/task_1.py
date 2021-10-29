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
from timeit import timeit, default_timer, repeat


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = (i for i in range(len(nums)) if not (i % 2))
    return list(new_arr)


def func_3(nums):
    new_arr = []
    for i in range(0, len(nums), 2):
        new_arr.append(i)
    return new_arr


def func_4(nums):
    return [i for i in range(0, len(nums), 2)]


ARRAY_LEN = 200
retries = 10000
arr = [i for i in range(ARRAY_LEN)]

statements = ['func_1(arr)', 'func_2(arr)', 'func_3(arr)', 'func_4(arr)']

for st in statements:
    print(st, min(repeat(stmt=st,
                         globals=globals(),
                         timer=default_timer,
                         repeat=3,
                         number=retries)))

'''
func_1(arr) 0.49355043699324597          # вариант исходный                             
func_2(arr) 0.35017852499731816          # через генератор списка (по всему диапазону)  
func_3(arr) 0.1501412369980244           # цикл только по чётным индексам               
func_4(arr) 0.09148654999444261          # списковое включение по четным индексам       

Лучшие результаты дали два последних варианта за счет более оптимального использования
вызова range. Лучший результат дал вариант спискового включения за счет использования 
внутренних алгоритмов питон, которые, как правило, более оптимальны.
'''
