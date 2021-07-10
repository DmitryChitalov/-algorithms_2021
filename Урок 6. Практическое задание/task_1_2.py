"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

import memory_profiler


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        res = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def recurs(n):
    def sum_el(n):
        if n == 0:
            return 0
        else:
            return 1 + sum_el(n-1) / (-2)
    return sum_el(n)

@decor
def cycle(n):
    sum = 0
    iter = 1
    for i in range(n):
        sum += iter
        iter /= -2
    return sum


print(recurs(900))
print(cycle(900))

"""По замерам видно, что выполнение циклом использует значительно меньше памяти, т.к.
в рекурссии необходимо хранить стек вызова"""