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
from scipy.special import lambertw
from math import e
import warnings
from timeit import timeit
from random import randint

warnings.filterwarnings('ignore')


def simple(i):
    """Без использования «Решета Эратосфена»
    O(n^2)
    """
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


def sieve(num):
    """
    O(e ^ -lambertw(-1 / num, k=-1))
    """
    a = []
    rng = int(e ** -lambertw(-1 / num, k=-1)).real
    for i in range(rng + 5):  # O(e ^ -lambertw(-1 / num, k=-1))
        a.append(i)

    a[1] = 0
    i = 2

    while i <= rng:  # O(e ^ -lambertw(-1 / num, k=-1))
        if a[i] != 0:
            j = i + i
            while j <= rng:  # O(e ^ -lambertw(-1 / num, k=-1)) - O(n)
                a[j] = 0
                j += i
        i += 1

    a = list(sorted(set(a)))  # O(n)
    return a[num]


if __name__ == '__main__':
    for i in range(2, 100):
        print(sieve(i) == simple(i))
    number = 1000
    print(timeit('simple (number)', globals=globals( ), number=100))
    print(timeit('sieve (number)', globals=globals( ), number=100))
"""
Алгоритм нахождения простого числа по порядковому номеру с применением алгоритма 'Решето Эратосфена' работает многократно
быстрее, чем наивный алгоритм.
Достигается данный результат прежде всего тем, что нам не требуется осуществлять перебор делителей, и мы осуществляем
меньше вызовов вложенного while. Верхний предел исследуемого массивая определяется при помощи теоремы о распределении
простых чисел: кол-во чисел ~ N * lnN.

P.S.
Я не уверен, что так можно было описывать алгоритмическую сложность, но какого-то общеиспользуемого обозначения
найти не удалось.
"""