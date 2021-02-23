from timeit import timeit
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


def simple(i):  # O(n^3)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:  # O(n)
        t = 1
        is_simple = True
        while t <= n:  # O(n)
            if n % t == 0 and t != 1 and t != n:  # O(n)
                is_simple = False
                break
            t += 1
        if is_simple:  # O(n)
            if count == i:  # O(n)
                break
            count += 1
        n += 1
    return n


def function(num):  # O(n^2 log(n))
    find = num
    num = num * 100
    a = [el for el in range(num + 1)]
    a[1] = 0
    i = 2
    while i <= num:  # O(n)
        if a[i] != 0:  # O(n)
            j = i + i
            while j <= num:  # O(log(n))
                a[j] = 0
                j += i
        i += 1
    a = set(a)
    a.remove(0)
    a = sorted(list(a))
    return a[find - 1]


print(function(23))
print(simple(23))
print(timeit('function(10)', globals=globals(), number=1000))
print(timeit('function(100)', globals=globals(), number=1000))
print(timeit('function(1000)', globals=globals(), number=100))
print(timeit('simple(10)', globals=globals(), number=1000))
print(timeit('simple(100)', globals=globals(), number=1000))
print(timeit('function(1000)', globals=globals(), number=100))
"""
По мере увеличения поиска, наивный алгоритм уступает по времени алгоритму "Решето Эратосфена" Первая функция может
быть полезной при малом поиске, а алгоритм Эратосфена при больших числах.
"""
