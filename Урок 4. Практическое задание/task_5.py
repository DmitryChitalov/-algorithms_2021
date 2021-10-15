"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (теорию по Решету нужно искать в сети)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from timeit import timeit


# O(n*2)
def simple(i):
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


# O(n*2)
def simple_re(i, n=10000):
    m = (n - 1) // 2
    b = [True] * m
    t, p, ps = 0, 3, [2]
    while p * p < n:
        if b[t]:
            ps.append(p)
            j = 2 * t * t + 6 * t + 3
            while j < m:
                b[j] = False
                j = j + 2 * t + 3
        t += 1
        p += 2
    while t < m:
        if b[t]:
            ps.append(p)
        t += 1
        p += 2
    return ps[i - 1]


# O(n*2)
def simple_re_set(i, n=10000):
    prime_list = []
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        sieve -= set(range(prime, n + 1, prime))
    return prime_list[i - 1]


num_10 = 10
num_100 = 100
num_1000 = 1000

print(simple(num_10))
print(simple_re(num_10))
print(simple_re_set(num_10))
print(f'simple:', timeit("simple(num_10)", globals=globals(), number=10))
print(f'simple_re:', timeit("simple_re(num_10)", globals=globals(), number=10))
print(f'simple_re_set:', timeit("simple_re_set(num_1000)", globals=globals(), number=10))

print(simple(num_100))
print(simple_re(num_100))
print(simple_re_set(num_100))
print(f'simple:', timeit("simple(num_100)", globals=globals(), number=10))
print(f'simple_re:', timeit("simple_re(num_100)", globals=globals(), number=10))
print(f'simple_re_set:', timeit("simple_re_set(num_1000)", globals=globals(), number=10))

print(simple(num_1000))
print(simple_re(num_1000))
print(simple_re_set(num_1000))
print(f'simple:', timeit("simple(num_1000)", globals=globals(), number=10))
print(f'simple_re:', timeit("simple_re(num_1000)", globals=globals(), number=10))
print(f'simple_re_set:', timeit("simple_re_set(num_1000)", globals=globals(), number=10))

'''
29
29
29
simple: 0.00021958099999999647
simple_re: 0.016485335000000004
simple_re_set: 0.49491457699999997
541
541
541
simple: 0.04036881800000003
simple_re: 0.018960509999999986
simple_re_set: 0.5113557729999999
7919
7919
7919
simple: 4.785837585
simple_re: 0.017865120000000623
simple_re_set: 0.42951660099999955
Эффективнее алгорритм simple_re
'''