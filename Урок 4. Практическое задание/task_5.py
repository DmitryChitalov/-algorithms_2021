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

from math import sqrt
from timeit import timeit


def simple(i):  # O(n^2)
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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

def eratosphen(i):  # O(NlogN)
    """C использованием «Решета Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
        return [p for p in sieve if p != 0][i - 1]

print(eratosphen(i))

print(f'simple(10):\t {simple(10)}. {timeit("simple(10)", globals=globals(), number=1000)}')                    # 0.037
print(f'eratosphen(10):\t {eratosphen(10)}. {timeit("eratosphen(10)", globals=globals(), number=1000)}')        # 0.970
print(f'simple(100):\t {simple(100)}. {timeit("simple(100)", globals=globals(), number=1000)}')                 # 1.963
print(f'eratosphen(100):\t {eratosphen(100)}. {timeit("eratosphen(100)", globals=globals(), number=1000)}')     # 0.977
print(f'simple(1000):\t {simple(1000)}. {timeit("simple(1000)", globals=globals(), number=100)}')               # 33.57
print(f'eratosphen(1000):\t {eratosphen(1000)}. {timeit("eratosphen(1000)", globals=globals(), number=100)}')   # 0.989

# На больших числах решето Эратосфена выполняется намного быстрее, т.к. имеет более эффективный алгоритм:
# O(NlogN) против O(n^2) у обычного перебора.