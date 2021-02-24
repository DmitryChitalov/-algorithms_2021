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


# i = int(input('Введите порядковый номер искомого простого числа: '))


def sieve(num):
    """C использованием «Решета Эратосфена»"""
    n = num * 10
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        j = i * i
        while j < n:
            primes[j] = False
            j = j + i
    res = [x for x in range(n) if primes[x]]
    return res[num - 1]


print("Функция simple(10)")
print(simple(10))
print(timeit("simple(10)", globals=globals(), number=1000))
print("Функция sieve(10)")
print(sieve(10))
print(timeit("sieve(10)", globals=globals(), number=1000))
print("----------------------------------------------------")
print("Функция simple(100)")
print(simple(100))
print(timeit("simple(100)", globals=globals(), number=1000))
print("Функция sieve(100)")
print(sieve(100))
print(timeit("sieve(100)", globals=globals(), number=1000))
print("----------------------------------------------------")
print("Функция simple(1000)")
print(simple(1000))
print(timeit("simple(1000)", globals=globals(), number=100))
print("Функция sieve(1000)")
print(sieve(1000))
print(timeit("sieve(1000)", globals=globals(), number=100))
print("----------------------------------------------------")
"""
Добавил функцию sieve(), которая для поиска i простого числа использует алгоритм "решето Эратосфена".
Провел замеры работы обоих функций через timeit:
- при поиске 10 простого числа функции показали примерно равное время на 1000 запусках;
- при поиске 100 простого числа функция c решетом показала скорость в 10 раз быстрей на 1000 запусках;
- при поиске 1000 простого числа функция c решетом показала скорость в 100 раз быстрей на 100 запусках.
Асимтотическая сложность функции simple() О(N^2), тогда как сложность функции sieve() - O(N).
Отсюда и закономерность в снижении скорости на 10^2.
"""
