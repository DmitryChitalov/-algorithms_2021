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

import timeit


def simple(i):
    """Без использования «Решета Эратосфена»
    O(n^2)"""
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


def eratosfen(i):
    """Решето Эратосфена
    O(n log (log n))"""
    last_num = 100000 + 1
    integers_num = [j for j in range(last_num)]
    integers_num[1] = 0
    cur_num = 2
    while cur_num < last_num:
        if integers_num[cur_num] != 0:
            next_num = cur_num * 2
            while next_num < last_num:
                integers_num[next_num] = 0
                next_num += cur_num
        cur_num += 1
    return [k for k in integers_num if k != 0][i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))

print(timeit.timeit("simple(i)", globals=globals(), number=100))
print(timeit.timeit("eratosfen(i)", globals=globals(), number=100))


"""
Время выполнения простой функции при n = 1000: 19.8793526
Время выполнения решета Эратосфена n = 1000: 2.1402652999999994

Первый алгоритм эффективен при небольших значения n, однако для n более 400 эффективнее становится алгоритм с решетом
Время выполнения простой функции при n = 400: 2.6934495999999997
Время выполнения решета Эратосфена n = 400: 2.0614513999999993
"""



