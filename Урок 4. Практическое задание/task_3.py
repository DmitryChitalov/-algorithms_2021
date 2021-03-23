"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from random import randint
from cProfile import run
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(num):
    lst = str(num).split()
    for i in range(len(lst)):
        result = lst.pop()
    return result


def revers_5(num):
    return reversed(str(num))


num_10000 = randint(100000000, 10000000000000)
str_1 = """
for i in range(1000000):
    revers_1(num_10000)
"""
str_2 = """
for i in range(1000000):
    revers_2(num_10000)
"""
str_3 = """
for i in range(1000000):
    revers_3(num_10000)
"""

str_4 = """
for i in range(1000000):
    revers_4(num_10000)
"""

str_5 = """
for i in range(1000000):
    revers_5(num_10000)
"""

run(str_1)
print("*" * 100)
run(str_2)
print("*" * 100)
run(str_3)
print("*" * 100)
run(str_4)
print("*" * 100)
run(str_5)
print("=" * 100)
print("=" * 100)
print(f'revers_1(num_10000) - {timeit("revers_1(num_10000)", globals=globals())}')
print(f'revers_2(num_10000) - {timeit("revers_2(num_10000)", globals=globals())}')
print(f'revers_3(num_10000) - {timeit("revers_3(num_10000)", globals=globals())}')
print(f'revers_4(num_10000) - {timeit("revers_4(num_10000)", globals=globals())}')
print(f'revers_5(num_10000) - {timeit("revers_5(num_10000)", globals=globals())}')

"""
Вывод:
использование встроенных функций в python наиболее эффективный подход.
По результатам профилировки самые быстрые оказались функции revers_3,
которая использует срезы. И revers_5, которая использует встроенную функцию reversed().
revers_4 функция немного им уступает, за счет выполнения операций pop, len, split.
revers_1 - самая долгая за счет дополнительных рекурсивных вызывов, которых стало 14млн
(ncalls = 14000000/1000000)
"""
