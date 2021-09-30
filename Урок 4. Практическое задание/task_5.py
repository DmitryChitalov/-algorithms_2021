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


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def primes(n=1):
    while True:
        if isprime(n):
            yield n
        n += 1


def simple_2(i):
    nums = []
    for n in primes():
        if i == len(nums):
            break
        nums.append(n)
    return nums[-1]


# i = int(input('Введите порядковый номер искомого простого числа: '))
i = 1000

print(simple(i), timeit('simple(i)', globals=globals(), number=10))
print(simple_2(i), timeit('simple(i)', globals=globals(), number=10))

'''
Не успел выполнить 5-е задание...
'''

