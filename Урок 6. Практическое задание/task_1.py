"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import copy
from memory_profiler import profile, memory_usage
from sys import getrefcount
from random import randint
from timeit import default_timer


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(args[0])
        t2 = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 -t1
        print("Memory: ", mem_diff)
        print("Time: ", time_diff)
        return res
    return wrapper


# Скрипт из основ Python: заполнить список значениями из диапазона (1; 250), которые кратны 20 или 21
@profile
def multiple_20_21_1():
    return [el for el in range(20, 2410) if el % 20 == 0 or el % 21 == 0]


@profile
def multiple_20_21_2():
    return sorted([*range(20, 2410, 20), *range(21, 2410, 21)])

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     19.2 MiB     19.2 MiB           1   @profile
    32                                         def multiple_20_21_1():
    33     19.2 MiB      0.0 MiB        2393       return [el for el in range(20, 2410) if el % 20 == 0 or el % 21 == 0]
    

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     19.2 MiB     19.2 MiB           1   @profile
    37                                         def multiple_20_21_2():
    38     19.2 MiB      0.0 MiB           1       return sorted([*range(20, 2410, 20), *range(21, 2410, 21)])

Оба решения идентичны с точки зрения использования памяти.
'''

# Скрипт из основ Python: заполнить новый список теми значениями из исходного, которые больше предыдущего элемента.
@decor
def get_list_1(init_list):
    return [el for i, el in enumerate(init_list[1:]) if el > init_list[i]]


@decor
def get_list_2(init_list):
    new_list = []
    for i in range(1, len(init_list)):
        if init_list[i - 1] < init_list[i]:
            new_list.append(init_list[i])
    return new_list

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    49     22.6 MiB     22.6 MiB           1   @profile
    50                                         def get_list_1(init_list):
    51     23.4 MiB     -2.1 MiB      100002       return [el for i, el in enumerate(init_list[1:]) if el > init_list[i]]


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     21.5 MiB     21.5 MiB           1   @profile
    55                                         def get_list_2(init_list):
    56     21.5 MiB      0.0 MiB           1       new_list = []
    57     22.3 MiB      0.0 MiB      100000       for i in range(1, len(init_list)):
    58     22.3 MiB      0.0 MiB       99999           if init_list[i - 1] < init_list[i]:
    59     22.3 MiB      0.8 MiB       49634               new_list.append(init_list[i])
    60     22.3 MiB      0.0 MiB           1       return new_list

Первое решение требует больше памяти (если считать, что ошибка в подсчете инкремента). Думаю, память должна 
тратиться на создание копии init_list, который подается как параметр в enumerate.
Второе решение требует дополнительной памяти для операции append. Однако в целом решение более экономично 
с точки зрения используемой памяти.

Измерения собственным декоратором:
Memory:  -0.47265625
Time:  0.04484300000000019

Memory:  1.3203125
Time:  0.054806099999999525

Первое решение быстрее, но память посчитана некорректно (видимо этот инструмент не очень подходит).
Второе решение медленнее, но используется дополнительная память.

'''
# Скрипт из данного курса. Составить новое число из исходного, записав цифры в обратном порядке.
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@decor
def num_reverse_1(number):
    return recursive_reverse(number)


@decor
def num_reverse_2(number):
    new_number = ''
    while number > 0:
        new_number += str(number % 10)
        number //= 10
    return new_number

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    97     21.9 MiB     21.9 MiB           1   @profile
    98                                         def num_reverse_1(number):
    99     21.9 MiB      0.0 MiB           1       return recursive_reverse(number)
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   102     21.9 MiB     21.9 MiB           1   @profile
   103                                         def num_reverse_2(number):
   104     21.9 MiB      0.0 MiB           1       new_number = ''
   105     21.9 MiB      0.0 MiB          16       while number > 0:
   106     21.9 MiB      0.0 MiB          15           new_number += str(number % 10)
   107     21.9 MiB      0.0 MiB          15           number //= 10
   108     21.9 MiB      0.0 MiB           1       return new_number
   
Оба решения идентичны с точки зрения используемой памяти.

Измерения собственным декоратором:
Memory:  0.0
Time:  0.00010810000000027742
Memory:  0.0
Time:  7.719999999977745e-05

Решение без использавания рекурсии ожидаемо быстрее. С точки зрения используемой памяти решения идентичны.
'''

if __name__ == "__main__":
    n = int(input("Введите число: "))
    multiple_20_21_1()
    multiple_20_21_2()
    init_list = [randint(-100, 100) for _ in range(100000)]
    get_list_1(init_list)
    get_list_2(init_list)
    num_reverse_1(n)
    num_reverse_2(n)

