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


def simple_2(x):
    """С использованием «Решета Эратосфена»"""
    n = 1000
    b = set()
    while len(b) < x:
        b = []
        for i in range(n + 1):
            b.append(i)
        b[1] = 0
        i = 2
        while i <= n:
            if b[i] != 0:
                j = i + i
                while j <= n:
                    b[j] = 0
                    j = j + i
            i += 1
        b = set(b)
        b.discard(0)
        n += 1000
    a = list(b)
    a.sort()
    return a[x-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(simple_2(i))

print(timeit("simple(10)", globals=globals(), number=10))       # 0.00039170900000051745
print(timeit("simple_2(10)", globals=globals(), number=10))     # 0.00460385299999988

print(timeit("simple(100)", globals=globals(), number=10))      # 0.03197509799999931
print(timeit("simple_2(100)", globals=globals(), number=10))    # 0.00451704399999997

print(timeit("simple(1000)", globals=globals(), number=10))     # 6.918288236
print(timeit("simple_2(1000)", globals=globals(), number=10))   # 0.5370673040000007


# Функция "Без использования «Решета Эратосфена»" имеет сложность O(2^n) и выполняется быстрее только на самых
# минимальных значениях.
# Функция "С использованием «Решета Эратосфена»" имеет сложность O(log n) или O(n log n), в зависимости от внутреннего
# параметра n (сейчас ==1000) и порядкого номера запрашиваемого числа; существенно выигрывает на больших значениях.
