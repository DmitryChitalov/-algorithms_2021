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


def eratosthen(n, sd=0):
    sieve = set(range(2, n**2 + 1))
    for i in range(n):
        sd = min(sieve)
        sieve -= set(range(sd, n**2 + 1, sd))
    return sd


n = int(input('Введите порядковый номер искомого простого числа: '))

print(simple(n))
print(timeit("simple(n)", globals=globals(), number=1000))

print(eratosthen(n))
print(timeit("eratosthen(n)", globals=globals(), number=1000))

# применил алгоритм Эратосфена на основе вычитаний множеств,
# при увеличении порядкового номера время растет экспоненциально O(len(...))
