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

# O(?)
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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

# O(1)
def gen():
    g_i = 2
    while True:
        g_i += 1
        yield g_i

# O(2n)
def sieve_eratosthenes(n):
    num = [1, 2]
    nums = gen()
    for g_i in nums:
        flag_add = True
        for g_j in num[1:]:
            if g_i % g_j == 0:
                flag_add = False
                break
        if flag_add:
            num.append(g_i)
        if len(num) > n:
            break
    return num[-1]


print("*" * 6)
j = int(input('Введите порядковый номер искомого простого числа: '))
print(sieve_eratosthenes(j))
print("***\t10\t***")
x = 10
print(timeit("simple(x)", "from __main__ import simple, x", number=10000))
print(timeit("sieve_eratosthenes(x)", "from __main__ import sieve_eratosthenes, x", number=10000))
print("***\t100\t***")
y = 100
print(timeit("simple(y)", "from __main__ import simple, y", number=10000))
print(timeit("sieve_eratosthenes(y)", "from __main__ import sieve_eratosthenes, y", number=10000))
print("***\t1000\t***")
z = 1000
print(timeit("simple(z)", "from __main__ import simple, z", number=100))
print(timeit("sieve_eratosthenes(z)", "from __main__ import sieve_eratosthenes, z", number=100))
'''
Введите порядковый номер искомого простого числа: 100
541
******
Введите порядковый номер искомого простого числа: 100
541
***	10  ***
0.1277359330000003        simple
0.08966213599999939       sieve_eratosthenes
***	100	***
15.736823377              simple
3.7575429090000014        sieve_eratosthenes
***	1000 ***              ! но запусков 100
26.274951502              simple
2.8481693129999996        sieve_eratosthenes
'''