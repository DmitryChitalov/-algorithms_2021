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

def erotasfen(i):
    a = []
    l = 50000
    for n in range(l+1):
        a.append(n)
    a[1] = 0
    n = 2
    while n <= l:
        if a[n] != 0:
            m = n + n
            while m <= l:
                a[m] = 0
                m = m + n
        n = n + 1

    return [p for p in a if p != 0] [i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))

print(simple(i))
print(erotasfen(i))

print(
    timeit(
        'simple(i)',
        setup='from __main__ import simple, i',
        number=100))
print(
    timeit(
        'erotasfen(i)',
        setup='from __main__ import erotasfen, i',
        number=100))

'''
number = 100:

i = 10

0.002610416999999643
1.7538425420000001 

i = 100

0.19559445900000005
1.762457125

i = 1000
33.264449667
1.7460030840000016

Адгоритм Решето Эратосфена эффективен для поиска числа с большим порядковым номером
Простой поиск = O(n*2)
Решето = O(n log(log n))
 
'''