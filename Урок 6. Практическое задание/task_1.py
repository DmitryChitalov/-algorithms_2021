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

import copy
import collections

from memory_profiler import profile
from sys import getrefcount
from random import randint


"""Скрипт № 1"""
# Решение без оптимизации
@profile
def my_func_1():
    """Профилирование функции без освобождения памяти

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    31     14.0 MiB     14.0 MiB           1   @profile
    32                                         def my_func_1():
    33     17.8 MiB      3.8 MiB           1       x = list(range(100000))
    34     18.8 MiB      1.1 MiB           1       y = copy.deepcopy(x)
    35     18.8 MiB      0.0 MiB           1       return x
    """

    x = list(range(100000))
    y = copy.deepcopy(x)
    return x

# Решение с оптимизацией
@profile
def my_func_2():
    """Профилирование функции с освобождением памяти

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    37     18.7 MiB     18.7 MiB           1   @profile
    38                                         def my_func_2():
    39     18.9 MiB      0.1 MiB           1       x = list(range(100000))
    40     18.9 MiB      0.0 MiB           1       print(getrefcount(x))
    41     19.7 MiB      0.8 MiB           1       y = copy.deepcopy(x)
    42     19.7 MiB      0.0 MiB           1       print(getrefcount(y))
    43     19.7 MiB      0.0 MiB           1       del x
    44     19.0 MiB     -0.8 MiB           1       y = None
    45     19.0 MiB      0.0 MiB           1       return y
    """

    x = list(range(100000))
    print(getrefcount(x))
    y = copy.deepcopy(x)
    print(getrefcount(y))
    del x
    y = None
    return y

""" Выводы по скрипту № 1:
После того как созданный список больше не нужен,
ссылку на него можно удалить, что приведет к уменьшению
искользуемой памяти до стартовых значений.
"""



"""Скрипт № 2"""
class Point_1:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return "Точка: {} \t Значение: {}".format(self.x, self.y, self.z)


# Решение без оптимизации
@profile
def my_func_3():
    """Профилирование функции без освобождения памяти

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    101     19.2 MiB     19.2 MiB           1   @profile
    102                                         def my_func_3():
    103     19.2 MiB      0.0 MiB           1       objs = []
    104     32.0 MiB      0.0 MiB      100001       for i in range(100000):
    105     32.0 MiB     12.8 MiB      100000           objs.append(Point(randint(0,50), randint(0, 50), randint(0, 50)))
    106     32.0 MiB      0.0 MiB           1       x = objs[0]
    107     32.0 MiB      0.0 MiB           1       y = objs[-1]
    108     32.0 MiB      0.0 MiB           1       print(x)
    109     32.0 MiB      0.0 MiB           1       print(y)
    """

    objs = []
    for i in range(100000):
        objs.append(Point_1(randint(0,50), randint(0, 50), randint(0, 50)))
    x = objs[0]
    y = objs[-1]
    print(x)
    print(y)


# Решение c оптимизации
@profile
def my_func_4():
    """Профилирование функции с освобождением памяти

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    111     19.9 MiB     19.9 MiB           1   @profile
    112                                         def my_func_4():
    113     19.9 MiB      0.0 MiB           1       objs = []
    114     30.7 MiB  -2728.4 MiB      100001       for i in range(100000):
    115     30.7 MiB  -2717.6 MiB      100000           objs.append(Point(randint(0,50), randint(0, 50), randint(0, 50)))
    116     30.7 MiB      0.0 MiB           1       x = objs[0]
    117     30.7 MiB      0.0 MiB           1       y = objs[-1]
    118     20.2 MiB    -10.5 MiB           1       del objs
    119     20.2 MiB      0.0 MiB           1       print(x)
    120     20.2 MiB      0.0 MiB           1       print(y)
    """
    objs = []
    for i in range(100000):
        objs.append(Point_1(randint(0,50), randint(0, 50), randint(0, 50)))
    x = objs[0]
    y = objs[-1]
    del objs
    print(x)
    print(y)


# Решение с использованием слотов
class Point_2:
    __slots__ = 'x', 'y', 'z'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return "Точка: {} \t Значение: {}".format(self.x, self.y, self.z)


@profile
def my_func_5():
    """Профилирование функции с использованием __slots__

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    171     14.4 MiB     14.4 MiB           1   @profile
    172                                         def my_func_5():
    173     14.4 MiB      0.0 MiB           1       objs = []
    174     23.5 MiB      0.0 MiB      100001       for i in range(100000):
    175     23.5 MiB      9.1 MiB      100000           objs.append(Point_2(randint(0,50), randint(0, 50), randint(0, 50)))
    176     23.5 MiB      0.0 MiB           1       x = objs[0]
    177     23.5 MiB      0.0 MiB           1       y = objs[-1]
    178     23.6 MiB      0.0 MiB           1       print(x)
    179     23.6 MiB      0.0 MiB           1       print(y)
    """
    objs = []
    for i in range(100000):
        objs.append(Point_2(randint(0,50), randint(0, 50), randint(0, 50)))
    x = objs[0]
    y = objs[-1]
    print(x)
    print(y)


""" Выводы по скрипту № 2:
После того как созданный список больше не нужен,
ссылку на него можно удалить, что приведет к уменьшению
искользуемой памяти до стартовых значений.
Использование __slots__ позволяет оптимизировать использование памяти,
практически аналогичное удалению созданного списка.
Недостаток: активация __slots__ запрещает создание всех элементов.
Также невозможно будет динамически добавлять новые переменные в класс.
"""


if __name__ == '__main__':
    my_func_1()
    my_func_2()
    my_func_3()
    my_func_4()
    my_func_5()


