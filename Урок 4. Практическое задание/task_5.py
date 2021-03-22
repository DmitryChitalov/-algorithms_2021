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
import timeit


def simple(i):   # O(N**2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:  # O(N**2)
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


# i_ = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i_))
print('*' * 10)
print(simple(10), timeit.timeit('simple(10)', number=100, globals=globals()))
print(simple(100), timeit.timeit('simple(100)', number=100, globals=globals()))
print(simple(1000), timeit.timeit('simple(1000)', number=10, globals=globals()))
# f = int(input('Введите порядковый номер искомого простого числа: '))


def eratosfen(n):  # O(N**2)
    a = []
    for i in range(n + 1):  # O(n**2)
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:  # O(n**2)
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)  # O(N)
    a.remove(0)
    return sum(a)


print('*' * 10)
print(eratosfen(10), timeit.timeit('eratosfen(10)', number=100, globals=globals()))
print(eratosfen(100), timeit.timeit('eratosfen(100)', number=100, globals=globals()))
print(eratosfen(1000), timeit.timeit('eratosfen(1000)', number=10, globals=globals()))

# Алгоритм Эратосфена быстрее во всех случаях т.к. в нём изначально присутствует готовый массив,
# элементы которого просто перебираются.
