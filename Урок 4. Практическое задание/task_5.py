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


def simple(i):
    #  сложность O(n^3)
    """Без использования «Решета Эратосфена»"""
    count = 1  # O(1)
    n = 2  # O(1)
    while count <= i:  # O(n)
        t = 1  # O(1)
        is_simple = True  # O(1)
        while t <= n:  # O(n)
            if n % t == 0 and t != 1 and t != n:  # O(n)
                is_simple = False  # O(1)
                break  # O(1)
            t += 1  # O(1)
        if is_simple:  # O(n)
            if count == i:  # O(n)
                break  # O(1)
            count += 1  # O(1)
        n += 1  # O(1)
    return n  # O(1)


#  не разобрался с алгоритмом Решето, функция не моя =(, сделал просто оценку исходя из скорости работы
def func_sieve(num):  # O(n^2 log(n))
    find = num  # O(1)
    num = num * 100  # O(1)
    a = [el for el in range(num + 1)]
    a[1] = 0  # O(1)
    i = 2  # O(1)
    while i <= num:  # O(n)
        if a[i] != 0:  # O(n)
            j = i + i  # O(1)
            while j <= num:  # O(Log(n))
                a[j] = 0  # O(1)
                j += i  # O(1)
        i += 1  # O(1)
    a = set(a)  # O(n)
    a.remove(0)  # O(1)
    a = sorted(list(a))  # O(Log(n))
    return a[find - 1]  # O(1)


num_1 = 10
num_2 = 100
num_3 = 1000
print(f'{timeit("simple(num_1)", globals=globals(), number=10)}')
print(f'{timeit("simple(num_2)", globals=globals(), number=10)}')
print(f'{timeit("simple(num_3)", globals=globals(), number=10)}')
print('=' * 100)
print(f'{timeit("func_sieve(num_1)", globals=globals(), number=10)}')
print(f'{timeit("func_sieve(num_2)", globals=globals(), number=10)}')
print(f'{timeit("func_sieve(num_3)", globals=globals(), number=10)}')

"""
Функция - 1 "Наивный поиск" имеет место быть, только при небольшой объеме поиска.
Во всех других случаях применение алгоритма "Решето Эратосфена" Функция -2 предпочтительный и быстрей.
Алгорит "Решето Эратосфена" лучше.
"""
