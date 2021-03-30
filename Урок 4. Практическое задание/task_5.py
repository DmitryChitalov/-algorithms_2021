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
from timeit import timeit


def simple(i):  # Сложность алгоритма O(n^2)
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


def sieve_of_eratosthenes(m):   # O(n log log n)
    n = 100000  # для 5000ого простого числа такого размера списка достаточно
    prime = [True for iterator in range(n + 1)]  # заполняем список всеми True
    p = 2
    while p * p <= n:
        if prime[p]:
            for iterator in range(p * p, n + 1, p):
                prime[iterator] = False  # выставляем в False те элементы, которые точно будут составными
        p += 1
    current_prime = 1
    for p in range(2, n + 1):
        if prime[p]:
            if current_prime == m:
                return p
            else:
                current_prime += 1


required_number = int(input('Введите порядковый номер искомого простого числа: '))

print(
    timeit(
        'simple(required_number)',
        globals=globals(),
        number=10))

print(
    timeit(
        'sieve_of_eratosthenes(required_number)',
        globals=globals(),
        number=10))

print(simple(required_number))
print(sieve_of_eratosthenes(required_number))

"""
Для 10ого числа время выполнения:
simple                 - 3.0000000000196536e-05
sieve_of_eratosthenes  - 0.018202400000000285
Навное решение работает быстрее

Для 100ого числа время выполнения:
simple                 - 0.003936700000000126
sieve_of_eratosthenes  - 0.018131099999999956
Навное решение все еще быстрее, но разрыв сокращается

Для 1000ого числа время выполнения:
simple                 - 0.5292240000000001
sieve_of_eratosthenes  - 0.018113500000000116
Решето работает быстрее

Для 5000ого числа время выполнения:
simple                 - 21.5711186
sieve_of_eratosthenes  - 0.023515599999999637
Отрыв решета увеличивается.

так как сложность наивного алгоритма O(n^2), а решета O(n log log n), наивный алгоритм выполняется быстрее при 
маленьких n. Однако на больших n разница в сложности начинает играть в пользу решета.
"""