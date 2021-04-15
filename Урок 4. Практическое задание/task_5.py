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
    """Без использования «Решета Эратосфена» - Квадратичная сложность О(n^2) """
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


def sieve(n):
    """ Сложность О(Nlog(logN))"""

    m = n * 10
    a = [i for i in range(m + 1)]
    a[1] = 0
    i = 2

    while i <= m:
        if a[i] != 0:
            j = i + i
            while j <= m:
                a[j] = 0
                j = j + i
        i += 1

    a = [i for i in a if i != 0]
    return a[n - 1]


n_10 = 10
n_100 = 100
n_1000 = 1000

print('simple(10): ', simple(n_10))
print('sieve(10): ', sieve(n_10))
print('simple(100): ', simple(n_100))
print('sieve(100): ', sieve(n_100))
print('simple(1000): ', simple(n_1000))
print('sieve(1000): ', sieve(n_1000))

print('simple(n_10)', timeit("simple(n_10)", setup='from __main__ import simple, n_10', number=100))
print('sieve(n_10)', timeit("sieve(n_10)", setup='from __main__ import sieve, n_10', number=100))
print('simple(n_100)', timeit("simple(n_100)", setup='from __main__ import simple, n_100', number=100))
print('sieve(n_100)', timeit("sieve(n_100)", setup='from __main__ import sieve, n_100', number=100))
print('simple(n_1000)', timeit("simple(n_1000)", setup='from __main__ import simple, n_1000', number=100))
print('sieve(n_1000)', timeit("sieve(n_1000)", setup='from __main__ import sieve, n_1000', number=100))


"""
Оценки сложности:
Простой алгоритм (simple): О(N^2)
Решето Эратосфена (sieve): О(Nlog(logN))

Время выполнения алгоритмов: 
simple(n_10) 0.0014814659999999868
sieve(n_10) 0.0019892959999999738
simple(n_100) 0.19284296299999998
sieve(n_100) 0.03233687799999996
simple(n_1000) 28.049433399
sieve(n_1000) 0.27304932900000267

Результаты замеров показали, что при увеличении количества элементов простой алгоритм выполняется намного медленнее 
алогирма "Решето Эратосфена". Такие данные соответсвуют оценке сложности двух алгоритмов.
"""
