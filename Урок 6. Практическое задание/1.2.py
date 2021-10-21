"""
"Решето Эратосфена"
Добавлено решение с использованием NumPy.
Вместо списка создаётся массив с элементами типа int.
Т.к. для создания решета используется большое количество элементов,
NumPy даёт большой выигрыш в использовании памяти.
Так же добавлен счётчик для подсчёта количества
найденных простых чисел, что бы функция возвращала
искомое простое число сразу же, как оно было найдено.
Это позволяет ускорить работу функции для небольших
искомых значений и не тратить ресурсы системы на
удаление дубликатов и сортировку.
Для 100-го простого числа:
Функция sieve:
Время выполнения: 0.565812 сек.
Использованная память: 0.5 Mib.
Функция sieve2:
Время выполнения: 0.5668151999999999 сек.
Использованная память: 0.01171875 Mib.
Для 1-го простого числа:
Функция sieve:
Время выполнения: 0.5757671 сек.
Использованная память: 0.2265625 Mib.
Функция sieve2:
Время выполнения: 0.21883599999999992 сек.
Использованная память: 0.01171875 Mib.
"""
import numpy as np
from memory_profiler import profile
from task_1 import time_memo_prof


# @time_memo_prof
@profile
def sieve(x):
    n = 1000000
    numbers = list(range(n + 1))
    numbers[1] = 0
    i = 2
    while i <= n:
        if numbers[i]:
            j = i * i
            while j <= n:
                numbers[j] = 0
                j = j + i
        i += 1
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[x]


# @time_memo_prof
@profile
def sieve2(x):
    n = 1000000
    # генерируем массив с помощью функции numpy.arange,
    # аналогичной range, но возвращающей сразу array
    numbers = np.arange(n + 1, dtype=int)
    numbers[1] = 0
    i = 2
    count = 0
    while i <= n:
        if numbers[i]:
            count += 1
            if count == x:
                return numbers[i]
            j = i * i
            while j <= n:
                numbers[j] = 0
                j = j + i
        i += 1


sieve(100)
sieve2(100)

"""
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\1.2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     30.0 MiB     30.0 MiB           1   @profile
    41                                         def sieve(x):
    42     30.0 MiB      0.0 MiB           1       n = 1000000
    43     68.5 MiB     38.6 MiB           1       numbers = list(range(n+1))
    44     68.5 MiB      0.0 MiB           1       numbers[1] = 0
    45     68.5 MiB      0.0 MiB           1       i = 2
    46     68.6 MiB -54685.2 MiB     1000000       while i <= n:
    47     68.6 MiB -54685.1 MiB      999999           if numbers[i]:
    48     68.6 MiB  -4292.2 MiB       78498               j = i * i
    49     68.6 MiB -53230.7 MiB     2200546               while j <= n:
    50     68.6 MiB -48938.5 MiB     2122048                   numbers[j] = 0
    51     68.6 MiB -48938.5 MiB     2122048                   j = j + i
    52     68.6 MiB -54685.2 MiB      999999           i += 1
    53     61.5 MiB     -7.1 MiB           1       numbers = list(set(numbers))
    54     61.7 MiB      0.3 MiB           1       numbers.sort()
    55     61.7 MiB      0.0 MiB           1       return numbers[x]
Filename: C:\Desktop\-algorithms_2021\Урок 6. Практическое задание\1.2.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    59     30.4 MiB     30.4 MiB           1   @profile
    60                                         def sieve2(x):
    61     30.4 MiB      0.0 MiB           1       n = 1000000
    62     34.2 MiB      3.8 MiB           1       numbers = np.arange(n+1, dtype=int)
    63     34.2 MiB      0.0 MiB           1       numbers[1] = 0
    64     34.2 MiB      0.0 MiB           1       i = 2
    65     34.2 MiB      0.0 MiB           1       count = 0
    66     34.2 MiB      0.0 MiB         540       while i <= n:
    67     34.2 MiB      0.0 MiB         540           if numbers[i]:
    68     34.2 MiB      0.0 MiB         100               count += 1
    69     34.2 MiB      0.0 MiB         100               if count == x:
    70     34.2 MiB      0.0 MiB           1                   return numbers[i]
    71     34.2 MiB      0.0 MiB          99               j = i * i
    72     34.2 MiB      0.0 MiB     2081055               while j <= n:
    73     34.2 MiB      0.0 MiB     2080956                   numbers[j] = 0
    74     34.2 MiB      0.0 MiB     2080956                   j = j + i
    75     34.2 MiB      0.0 MiB         539           i += 1
"""
