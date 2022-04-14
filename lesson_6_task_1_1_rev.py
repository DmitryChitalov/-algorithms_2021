"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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
from memory_profiler import profile
from numpy import array

"""
Для 1-го примера взяла задание 1 к уроку 4 Алгоритмов
---
Задание 1 к уроку 4:
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit...

---
Сделала замеры кодов с функциями, которые были к уроку 4 (func_1, func_2)
Потом использовала array библиотеки numpy (func_1_new, func_2_new)
Замеры показали эффективность управления памятью numpy (ниже)
"""


@profile  # 1-й вариант решения к уроку 4
def func_1():
    nums = list(range(100000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# переписываем функцию с ипользованием list comprehensions
# list comprehensions определяет список и его содержимое одновременно, не вызывает append, => быстрее


@profile  # 2-й вариант решения к уроку 4
def func_2():
    nums = list(range(100000))
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


@profile  # оптимизация 1-го варианта с ипользованием array
def func_1_new():
    nums = array(range(100000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile  # оптимизация 2-го варианта с ипользованием array
def func_2_new():
    nums = array(range(100000))
    new_list = [num for num in nums if num % 2 == 0]
    return new_list


func_1()
func_1_new()
func_2()
func_2_new()

# Массивы NumPy быстрее, чем списки Python.
# Массив потребляет меньше памяти.
# Замеры такжже показали экономию памяти, для func_1 и func_1_new разница составила 2.0 MiB,
# для func_2 и func_2_new - 0.6 MiB.

'''
Результат замеров:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     24.2 MiB     24.2 MiB           1   @profile
    34                                         def func_1():
    35     26.1 MiB      1.9 MiB           1       nums = list(range(100000))
    36     26.1 MiB      0.0 MiB           1       new_arr = []
    37     27.4 MiB      0.0 MiB      100001       for i in range(len(nums)):
    38     27.4 MiB      0.7 MiB      100000           if nums[i] % 2 == 0:
    39     27.4 MiB      0.5 MiB       50000               new_arr.append(i)
    40     27.4 MiB      0.0 MiB           1       return new_arr


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    53     24.8 MiB     24.8 MiB           1   @profile
    54                                         def func_1_new():
    55     25.5 MiB      0.8 MiB           1       nums = array(range(100000))
    56     25.5 MiB      0.0 MiB           1       new_arr = []
    57     26.0 MiB      0.0 MiB      100001       for i in range(len(nums)):
    58     26.0 MiB      0.2 MiB      100000           if nums[i] % 2 == 0:
    59     26.0 MiB      0.2 MiB       50000               new_arr.append(i)
    60     26.0 MiB      0.0 MiB           1       return new_arr


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     24.8 MiB     24.8 MiB           1   @profile
    47                                         def func_2():
    48     26.1 MiB      1.3 MiB           1       nums = list(range(100000))
    49     26.6 MiB      0.4 MiB      100003       new_list = [num for num in nums if num % 2 == 0]
    50     26.6 MiB      0.0 MiB           1       return new_list



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     24.8 MiB     24.8 MiB           1   @profile
    64                                         def func_2_new():
    65     25.6 MiB      0.8 MiB           1       nums = array(range(100000))
    66     26.0 MiB      0.4 MiB      100003       new_list = [num for num in nums if num % 2 == 0]
    67     26.0 MiB      0.0 MiB           1       return new_list



Process finished with exit code 0
'''
