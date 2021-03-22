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
    end = 10
    while True:
        a = []
        for i in range(end + 1):
            a.append(i)
        a[1] = 0
        i = 2
        while i <= end:
            if a[i] != 0:
                j = i + i
                while j <= end:
                    a[j] = 0
                    j = j + i
            i += 1
        end = end + end
        a = list(set(a))
        a.remove(0)
        if len(a) > num:
            break
    return a[num]



i_10 = 10
i_100 = 100
i_1000 = 1000

print(f'simple(i_10)= {timeit("simple(i_10)", "from __main__ import simple, i_10", number=100)}')
print(f'eratosthenes_sieve(i_10)= {timeit("eratosthenes_sieve(i_10)", "from __main__ import eratosthenes_sieve, i_10", number=100)}')
print(f'simple(i_100)= {timeit("simple(i_100)", "from __main__ import simple, i_100", number=100)}')
print(f'eratosthenes_sieve(i_100)= {timeit("eratosthenes_sieve(i_100)", "from __main__ import eratosthenes_sieve, i_100", number=100)}')
print(f'simple(i_1000)= {timeit("simple(i_1000)", "from __main__ import simple, i_1000", number=100)}')
print(f'eratosthenes_sieve(i_1000)= {timeit("eratosthenes_sieve(i_1000)", "from __main__ import eratosthenes_sieve, i_1000", number=100)}')


"""
Резюмируя:
Очевидно Решето Эратосфена превосходит наивный алгоритм по мере увеличения индекса простого числа.
Сложность функции:
    simple O(n**2)
    eratosthenes_sieve O(n)

simple(i_10)=                   0.004424821000000023
eratosthenes_sieve(i_10)=       0.004405107000000019

simple(i_100)=                  0.48599090500000003
eratosthenes_sieve(i_100)=      0.087730894

simple(i_1000)=                 82.282387626
eratosthenes_sieve(i_1000)=     1.6972288559999953
"""






















