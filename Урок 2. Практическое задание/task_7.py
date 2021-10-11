"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import sys
sys.setrecursionlimit(10000)

def sum_func(n, res = 0):
    if n == 0:
        return res
    res += n

    return sum_func(n-1,res)


def prove_it(n):
    if n*(n+1)/2 == sum_func(n):
        return True
    else:
        return False

def check_all_in_set(n,start=1):
    if n == 0:
        return True
    if start == n:
        return prove_it(start)
    elif prove_it(start):
        return check_all_in_set(n, start + 1)
    else:
        return False

print(check_all_in_set(878))