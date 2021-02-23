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


def simple(i):  # O(N^2)
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


def sieve(n):  # O(NlogN)
    find = n
    n = n * 100
    a = [el for el in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:  # O(N)
        if a[i] != 0:
            j = i + i
            while j <= n:  # O(logN)
                a[j] = 0
                j += i
        i += 1
    a = set(a)
    a.remove(0)
    a = sorted(list(a))
    return a[find - 1]


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(sieve(i))
print(timeit('simple(10)', globals=globals(), number=1000))
print(timeit('sieve(10)', globals=globals(), number=1000))

print(timeit('simple(100)', globals=globals(), number=1000))
print(timeit('sieve(100)', globals=globals(), number=1000))

print(timeit('simple(1000)', globals=globals(), number=1000))
print(timeit('sieve(1000)', globals=globals(), number=1000))

# чем больше порядковый номер числа, тем выше эффективность решета
# на небольших числах эффективнее просто алгоритм
