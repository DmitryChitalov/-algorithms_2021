"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""
import sys

from memory_profiler import profile
from timeit import default_timer
from functools import reduce

START_RANGE = 0
FINISH_RANGE = 50000


def measure(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        print(f'Результат работы {func.__name__} {default_timer() - start}')
        return result
    return wrapper

@measure
@profile
def func_nonoptimized(start=START_RANGE, finish=FINISH_RANGE):
    def divided_by_digit(num, digit=7):
        return True if reduce(lambda x, y: x + y, (int(x) for x in str(num))) % digit == 0 else False
    l = [pow(i, 3) for i in range(start, finish, 2) if divided_by_digit(pow(i, 3))]
    print(f'Размер результата {sys.getsizeof(l)}')
    return l


@measure
@profile
def func_optimized(start=START_RANGE, finish=FINISH_RANGE):
    result = 0
    for i in range(start, finish, 2):
        n = pow(i, 3)
        sumnum = sum(int(x) for x in str(n))
        if sumnum % 7 == 0:
            result += n
    print(f'Размер результата {sys.getsizeof(result)}')
    return result


if __name__ == '__main__':
    print(sum(func_nonoptimized()))
    print(func_optimized())


'''
Что пытался изобразить:
оптимизация путем изоляции вычислений внутри самой функции. Таким образом функция возвращает уже вычисленный
результат. Поскольку сложность O(n**2), то для замеров применил sys.getsizeof. В относительном выражении выигрыш
по памяти запредельный)))), в абсолютном выражении profile не зафиксировал разницы за счет порядка (шага)
измерения.
Дополнительно обратил внимание, то такой подход положительно сказался на скорости выполнения. Полагаю, что это 
частный случай, только для такого рода задачи, а в НЕоптимизиравонном варианте применены универсальные
конструкции питон.
Вывод: в ряде случаев следует рассмотреть вариант написания своего варианта функции, выполняющей специфичный
функционал.  



Размер результата 26040
Filename: /home/master/PycharmProjects/Q1_algo/algo_2021/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     38.6 MiB     38.6 MiB           1   @measure
    26                                         @profile
    27                                         def func_nonoptimized(start=START_RANGE, finish=FINISH_RANGE):
    28     38.6 MiB      0.0 MiB       25001       def divided_by_digit(num, digit=7):
    29     38.6 MiB      0.0 MiB     1351736           return True if reduce(lambda x, y: x + y, (int(x) for x in str(num))) % digit == 0 else False
    30     38.6 MiB      0.0 MiB       25003       l = [pow(i, 3) for i in range(start, finish, 2) if divided_by_digit(pow(i, 3))]
    31     38.6 MiB      0.0 MiB           1       print(f'Размер результата {sys.getsizeof(l)}')
    32     38.6 MiB      0.0 MiB           1       return l


Результат работы wrapper 358.60850606299937
88391342610686656
Размер результата 32
Filename: /home/master/PycharmProjects/Q1_algo/algo_2021/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     38.6 MiB     38.6 MiB           1   @measure
    36                                         @profile
    37                                         def func_optimized(start=START_RANGE, finish=FINISH_RANGE):
    38     38.6 MiB      0.0 MiB           1       result = 0
    39     38.8 MiB      0.0 MiB       25001       for i in range(start, finish, 2):
    40     38.8 MiB      0.0 MiB       25000           n = pow(i, 3)
    41     38.8 MiB      0.2 MiB      738368           sumnum = sum(int(x) for x in str(n))
    42     38.8 MiB      0.0 MiB       25000           if sumnum % 7 == 0:
    43     38.8 MiB      0.0 MiB        2966               result += n
    44     38.8 MiB      0.0 MiB           1       print(f'Размер результата {sys.getsizeof(result)}')
    45     38.8 MiB      0.0 MiB           1       return result


Результат работы wrapper 201.9717829000001
88391342610686656
'''
