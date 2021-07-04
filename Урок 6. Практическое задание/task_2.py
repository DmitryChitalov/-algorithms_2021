"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

from memory_profiler import profile
from random import randint

# один из способов оптимизировать код это переопределять переменные, когда старые нам уже не нужны.
# ниже приведен бесполезный код: в первом случае мы не переопределяем переменную data внутри функции, когда уже
# взяли из нее нужную нам переменную a. Во втором случае мы переопредляем data и избавляемся от ненужного нам уже
# списка в памяти, выигрывая около двух мебибайт в данном случае (профилировка приведена после кода):

@profile
def do_stuff():
    data = [randint(0, 100) for i in range(100_000)]
    a = data[5]
    second_data = [randint(0, 100) for i in range(100_000)]
    b = second_data[5]
    return a * b


do_stuff()

@profile
def do_stuff():
    data = [randint(0, 100) for i in range(100_000)]
    a = data[5]
    data = [randint(0, 100) for i in range(100_000)]
    b = data[5]
    return a * b

do_stuff()

# Без переопределения:
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     14     18.3 MiB     18.3 MiB           1   @profile
#     15                                         def do_stuff():
#     16     19.5 MiB      1.2 MiB      100003       data = [randint(0, 100) for i in range(100_000)]
#     17     19.5 MiB      0.0 MiB           1       a = data[5]
#     18     21.0 MiB      1.5 MiB      100003       second_data = [randint(0, 100) for i in range(100_000)]
#     19     21.0 MiB      0.0 MiB           1       b = second_data[5]
#     20     21.0 MiB      0.0 MiB           1       return a * b
#
# С переопределением:
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     27     19.1 MiB     19.1 MiB           1   @profile
#     28                                         def do_stuff():
#     29     19.9 MiB      0.8 MiB      100003       data = [randint(0, 100) for i in range(100_000)]
#     30     19.9 MiB      0.0 MiB           1       a = data[5]
#     31     20.6 MiB     -0.7 MiB      100003       data = [randint(0, 100) for i in range(100_000)]
#     32     19.2 MiB     -1.5 MiB           1       b = data[5]
#     33     19.2 MiB      0.0 MiB           1       return a * b
