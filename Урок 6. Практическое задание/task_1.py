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
from timeit import timeit
from pympler import asizeof
import numpy as np


"""______________пример 1_____________________"""


def sum_of_range_natural_nums(num):
    if num == 1:
        return num
    else:
        return num + sum_of_range_natural_nums(num - 1)


@profile
def i1():
    print(timeit('sum_of_range_natural_nums(2500)', globals=globals(), number=1000))
    sum_of_range_natural_nums(2500)


# i1()  # 6.1740440700014005

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     38.4 MiB     38.4 MiB           1   @profile
    36                                         def i1():
    37     40.1 MiB      1.7 MiB           1       sum_of_range_natural_nums(2500)

Самая очевидная оптимизация памяти - уйти от рекурсии
"""


def sum_of_range_natural_nums2(num):
    return sum([x for x in range(1, num + 1)])


@profile
def i():
    sum_of_range_natural_nums2(2500)
    print(timeit('sum_of_range_natural_nums2(2500)', globals=globals(), number=1000))


# i()  # 1.214360932001

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    61     38.4 MiB     38.4 MiB           1   @profile
    62                                         def i():
    63     38.4 MiB      0.0 MiB           1       sum_of_range_natural_nums2(2500)
    
теперь функция не просит дополнительной памяти + такая функция не упадет, если число иттераций 
превысит 1000, к тому же она быстрее
"""

"""______________пример 2_____________________"""


def sum_of_row(num, result=1):
    if num < 1:
        return 'некорректное значение'
    elif num == 1:
        return result
    else:
        return result + sum_of_row(num - 1, -(result / 2))


@profile
def test():
    sum_of_row(2000)
    print(timeit('sum_of_row(2000)', globals=globals(), number=1000))


# test()  # 5.9687690530008695

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    91     38.5 MiB     38.5 MiB           1   @profile
    92                                         def test():
    93     40.5 MiB      2.0 MiB           1       sum_of_row(2000)

тут можно не только уйти от рекурсии, но и воспользоваться генератором
"""


def gener_new_num(i=1):
    while True:
        yield i
        i = - (i / 2)


def sum_of_row2(num):
    result = gener_new_num()
    i = sum([next(result) for _ in range(num)])
    return i


@profile
def test2():
    sum_of_row2(2000)
    print(timeit('sum_of_row2(2000)', globals=globals(), number=1000))


# test2()  # 4.864952231000643

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   119     38.6 MiB     38.6 MiB           1   @profile
   120                                         def test2():
   121     38.6 MiB      0.0 MiB           1       sum_of_row2(2000)

при этой реализации дополнительная память не потребовалась, плюс время работы функции немного, но быстрее
"""

"""______________пример 3_____________________"""

"""
реализуем большой массив через list comprehension (обычный список) 
"""


def my_array(num):
    return [x for x in range(num)]


"""
и через numpy
"""


def my_array2(num):
    return np.arange(4)


a = my_array(100000)
b = my_array(100000)
c = np.arange(100000)
d = np.arange(100000)

"""
наша задача - складывать значения по позициям в каждом массиве (длина массивов одинаковая)
"""


def sum_nums_in_arr(x, y):
    return [x[i] + y[i] for i in range(len(a))]


def sum_nums_in_arr2(x, y):
    return x + y


@profile
def test5():
    result = sum_nums_in_arr(a, b)
    print(asizeof.asizeof(result))
    print(timeit('sum_nums_in_arr(a, b)', globals=globals(), number=100))

# test5()

"""
4 024 448  - большой объем памяти
7.135893288999796 - медленная обработка
Filename: /home/nella/GeekBrains/algorithms_2021/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   182     61.5 MiB     61.5 MiB           1   @profile
   183                                         def test5():
   184     64.8 MiB      3.3 MiB           1       result = sum_nums_in_arr(a, b)
   185     65.1 MiB      0.2 MiB           1       print(asizeof.asizeof(result))
   186     65.7 MiB      0.6 MiB           1       print(timeit('sum_nums_in_arr(a, b)', globals=globals(), number=100))
"""

@profile
def test6():
    result = sum_nums_in_arr2(c, d)
    print(asizeof.asizeof(result))
    print(timeit('sum_nums_in_arr2(c, d)', globals=globals(), number=100))

test6()

"""
800 120 - занимает на порядок меньше памяти
0.010016449999966426 - скорость обработки выше почти на три порядка
Filename: /home/nella/GeekBrains/algorithms_2021/-algorithms_2021/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   204     61.3 MiB     61.3 MiB           1   @profile
   205                                         def test6():
   206     62.1 MiB      0.8 MiB           1       result = sum_nums_in_arr2(c, d)
   207     62.1 MiB      0.0 MiB           1       print(asizeof.asizeof(result))
   208     62.3 MiB      0.2 MiB           1       print(timeit('sum_nums_in_arr2(c, d)', globals=globals(), number=100))
"""

"""
в итоге numpy позволяет добиться и большей скорости обратки данных, и сами данные весят меньше
для обработки требуется меньше оперативной памяти
"""
