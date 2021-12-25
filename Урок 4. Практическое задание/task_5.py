"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (теорию по Решету нужно искать в сети)

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


def sieve(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:  # O(N)
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i  # O(log N)
        i += 1

    a = set(a)

    a.remove(0)
    return sorted(list(a))


def find_num(n):
    a = sieve(n * 100)
    return a[n-1]


#  i = int(input('Введите порядковый номер искомого простого числа: '))
print('Порядковый номер 10:')
print('Решето: ')
print(timeit('find_num(10)', 'from __main__ import find_num', number=1000))
print('Перебор: ')
print(timeit('simple(10)', 'from __main__ import simple', number=1000))
print('Порядковый номер 100:')
print('Решето: ')
print(timeit('find_num(100)', 'from __main__ import find_num', number=100))
print('Перебор: ')
print(timeit('simple(100)', 'from __main__ import simple', number=100))
print('Порядковый номер 1000:')
print('Решето: ')
print(timeit('find_num(1000)', 'from __main__ import find_num', number=10))
print('Перебор: ')
print(timeit('simple(1000)', 'from __main__ import simple', number=10))

# Сложность наивного алгоритма O(n**2), а сложность решета Эратосфена O(NlogN), следовательно эффективность решета
# растет с увеличением искомого порядкового номера
