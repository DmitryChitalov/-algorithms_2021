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


def eratosthenes_sieve(num):
    n = num*100
    a = [el for el in range(n+1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = list(filter(lambda x: x != 0, a))
    return a[num-1]


print(f'{timeit("simple(10)",globals=globals(), number = 100)} simple(10)' )
print(f'{timeit("eratosthenes_sieve(10)",globals=globals(), number = 100)} eratosthenes_sieve(10)')

print(f'{timeit("simple(100)",globals=globals(), number = 100)} simple(100)' )
print(f'{timeit("eratosthenes_sieve(100)",globals=globals(), number = 100)} eratosthenes_sieve(100)')

print(f'{timeit("simple(1000)",globals=globals(), number = 100)} simple(1000)' )
print(f'{timeit("eratosthenes_sieve(1000)",globals=globals(), number = 100)} eratosthenes_sieve(1000)')

'''
0.0045269 simple(10)
0.006950499999999998 eratosthenes_sieve(10)
0.4502739 simple(100)
0.08973589999999992 eratosthenes_sieve(100)
75.56530029999999 simple(1000)
0.7955311000000052 eratosthenes_sieve(1000)
При небольших значениях i быстрее работает функция simple(ее сложность О(n^2), 
при больших значениях i быстрее работает функция eratosthenes_sieve(ее сложность O(n log log n)))
'''