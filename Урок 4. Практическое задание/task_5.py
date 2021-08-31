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
    """Без использования «Решета Эратосфена»
    Сложность функции квадратичная"""
    count = 1
    n = 2
    while count <= i:  # O(n)
        t = 1
        is_simple = True
        while t <= n:  # O(n)
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


def eratosthenes(numb):
    """Сложность функции получилась квадратичная,
    но скорость выполнения намного выше"""
    n = numb * 10
    a = []
    for i in range(n + 1): # O(n)
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:  # O(n)
        if a[i] != 0:
            j = i + i
            while j <= n:  # O(n)
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    res = sorted(a)
    return res[numb - 1]


print(eratosthenes(i))

print('--' * 20)

print(10)
print(timeit('simple(10)', globals=globals(), number=10))
print(timeit('eratosthenes(10)', globals=globals(), number=10))
print('--' * 20)

print(100)
print(timeit('simple(100)', globals=globals(), number=10))
print(timeit('eratosthenes(100)', globals=globals(), number=10))
print('--' * 20)

print(1000)
print(timeit('simple(1000)', globals=globals(), number=10))
print(timeit('eratosthenes(1000)', globals=globals(), number=10))
print('--' * 20)
