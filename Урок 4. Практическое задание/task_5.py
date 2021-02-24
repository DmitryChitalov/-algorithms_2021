"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# def eratosthenes(n):
#     num_list = [2]
#     for i in range(n - 1):
#         n = num_list[-1]
#         while True:
#             temp_list = [n % x for x in num_list]
#             if 0 in temp_list:
#                 n += 1
#             else:
#                 num_list.append(n)
#                 break
#     return num_list[-1]

def eratosthenes(n):
    num_list = [2]
    for i in range(n - 1):
        n = num_list[-1]
        signal = 0
        while signal == 0:
            for j in num_list:
                if n % j == 0:
                    n += 1
                    break
            else:
                num_list.append(n)
                signal = 1
    return num_list[-1]


# print(eratosthenes(100))
print('Исходная функция')
print(
    timeit(
        "eratosthenes(10)",
        setup='from __main__ import eratosthenes',
        number=100))
print(
    timeit(
        "eratosthenes(100)",
        setup='from __main__ import eratosthenes',
        number=100))
print(
    timeit(
        "eratosthenes(1000)",
        setup='from __main__ import eratosthenes',
        number=100))

print('Решето Эратосфена')
print(
    timeit(
        "simple(10)",
        setup='from __main__ import simple',
        number=100))
print(
    timeit(
        "simple(100)",
        setup='from __main__ import simple',
        number=100))
print(
    timeit(
        "simple(1000)",
        setup='from __main__ import simple',
        number=100))

"""Если я правильно сделал, то у меня с Решетом сложность и время полчились выше, т.к. в Решете требуется проверить 
делимость со всеми предыдущими числами, т.е. допустим для нахождения числа 23 надо проверить делимость чисел от 19 до 
23 со всеми предыдущими простыми числами. У исходного алгоритма сложность линейная, у решета - квадратичная. """
