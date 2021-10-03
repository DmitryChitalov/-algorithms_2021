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
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""


import timeit


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


def eratosfen(i):
    n = 2
    l = 500
    sieve = [x for x in range(1)]
    sieve[1] = 0
    while n < 1:
        if sieve[n] != 0:
            m = n * 2
            while m < 1:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i -1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit.timeit("simple(i)", globals=globals(),number=100))
print(simple(i))

"""
Введите порядковый номер искомого простого числа: 25
0.008378700000000183
97
"""
