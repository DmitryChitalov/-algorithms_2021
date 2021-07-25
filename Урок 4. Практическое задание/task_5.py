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


def erat(i):
    l = 2000
    a = [n for n in range(l + 1)]
    a[1] = 0
    n = 2
    while n <= l:
        if a[n] != 0:
            m = n + n
            while m <= l:
                a[m] = 0
                m = m + n
        n = n + 1

    return [p for p in a if p != 0][i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(erat(i))

print(timeit('simple(i)', globals=globals(),number=1000))
print(timeit('erat(i)', globals=globals(),number=1000))
'''
i - 10
number = 100
0.0023405000000003007
0.012223300000000048

i - 100
number = 1000
1.8785500000000002
0.6202927999999996

Решето Эратосфена лучше  для поиска числа с большим порядковым номером
Простой поиск = O(n*2)
Решето = O(n log(log n))

'''