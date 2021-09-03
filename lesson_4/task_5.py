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


def eratosfen(i):
    l = 20 * i
    sieve = [x for x in range(l)]
    sieve[1] = 0
    j = 2
    while j < l:
        if sieve[j] != 0:
            k = j + j
            while k < l:
                sieve[k] = 0
                k += j
        j += 1
    return [el for el in sieve if el != 0][i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print('Без использования «Решета Эратосфена»: ', simple(i))

print('С использованием «Решета Эратосфена»: ', eratosfen(i))

print(timeit('simple(i)', number=10000, globals=globals()))
print(timeit('eratosfen(i)', number=10000, globals=globals()))

# sample i = 10,    0.1793712999999999
# eratosfen i = 10, 0.4681066999999999
#
# sample i = 100,    22.2917811
# eratosfen i = 100, 6.317381700000002
#
# sample i = 500,    760.5490115
# eratosfen i = 500, 760.5490115
#
# Алгоритм «Решето Эратосфена» работает медленнее на малых порядковых номерах простого числа
# и работает значительно быстрее на больших порядковых номерах числа
