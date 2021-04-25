"""Числа Фибоначчи"""
import sys


sys.setrecursionlimit(10000)


def fib(n, summ):
    if n < 1:
        return summ
    return fib(n-1, summ+n)


c = 998
# c = 998 - уже не работает
# необузданная рекурсия вызывает переполнение стека
print(fib(c, 0))
