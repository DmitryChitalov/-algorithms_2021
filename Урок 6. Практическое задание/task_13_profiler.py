"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from functools import reduce

from memory_profiler import profile


@profile
def print_list_1():
    new_list = [el for el in range(100, 10001) if el % 2 == 0]
    result = reduce((lambda mul, cur: mul + cur), new_list)
    print(result)


@profile
def print_list_2():
    new_list = (el for el in range(100, 10001) if el % 2 == 0)
    result = reduce((lambda mul, cur: mul + cur), new_list)
    print(result)


# print_list_1()
print_list_2()

"""
Результаты:
Без оптимизации:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     19.0 MiB     19.0 MiB           1   @profile
    29                                         def print_list_1():
    30     19.2 MiB      0.2 MiB        9904       new_list = [el for el in range(100, 10001) if el % 2 == 0]
    31     19.2 MiB      0.0 MiB        9901       result = reduce((lambda mul, cur: mul + cur), new_list)
    32     19.2 MiB      0.0 MiB           1       print(result)

С оптимизацией:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     19.0 MiB     19.0 MiB           1   @profile
    36                                         def print_list_2():
    37     19.0 MiB      0.0 MiB       14855       new_list = (el for el in range(100, 10001) if el % 2 == 0)
    38     19.0 MiB      0.0 MiB        9901       result = reduce((lambda mul, cur: mul + cur), new_list)
    39     19.0 MiB      0.0 MiB           1       print(result)

 Для оптимизации использования памяти в функции print_list_2 был использовано генератор, вместо list comprehension.
 Теперь нет необходимости хранить список в памяти.
"""
