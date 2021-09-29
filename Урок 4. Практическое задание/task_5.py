"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve) - функция по ссылке не считает i-e число

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""

from cProfile import run
from timeit import timeit


def simple(i):  # O(n^2)
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


def get_prime_sieve(n):  # O(n)
    sieve = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    sieve.extend([i for i in range(29, n * 7) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and
                  i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0 and i % 29 != 0])

    len_sieve = len(sieve)
    for i in range(4, len_sieve):
        for j in range(i + 1, len_sieve):
            if sieve[i] != 1 and sieve[j] % sieve[i] == 0:
                sieve[j] = 1

    primes_list = [p for p in sieve if p != 1]
    len_primes_list = len(primes_list)
    while len_primes_list <= n:
        range_left = primes_list[len_primes_list - 1]
        range_right = range_left + primes_list[len_primes_list//4]
        sieve = [i for i in range(range_left, range_right) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and
                 i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and
                 i % 23 != 0 and i % 29 != 0]
        sieve = primes_list + sieve

        len_sieve = len(sieve)
        for i in range(4, len_sieve):
            begin = i + 1 if i > len_primes_list else len_primes_list
            for j in range(begin, len_sieve):
                if sieve[i] != 1 and sieve[j] % sieve[i] == 0:
                    sieve[j] = 1

        primes_list = [p for p in sieve if p != 1]
        len_primes_list = len(primes_list)

    return primes_list[n - 1]


if __name__ == '__main__':
    i = int(input('Введите порядковый номер искомого простого числа: '))

    print(simple(i))
    print(get_prime_sieve(i))

    print('=' * 50)

    REPEAT = 1000000 // i
    print(f"Время выполнения первого алгоритма: {timeit('simple(i)', number=REPEAT, globals=globals())}")
    print(f"Время выполнения второго алгоритма: {timeit('get_prime_sieve(i)', number=REPEAT, globals=globals())}")

    print('=' * 50)

    run('simple(i)')
    print('*' * 50)
    run('get_prime_sieve(i)')

    # Результаты выполнения

    # ВЫВОД. Временные замеры показали, что оценка сложности, скорее всего, верна: алгоритм "Решето Эратосфена" работает
    # быстрее уже на числа близких к сотне, а при приближении к 1000 разрыв увеличивается в разы, но всё же это
    # не похоже на квадратичную разницу. Так что первый алгоритм, вероятно, не квадратичную сложность имеет, возможно,
    # n log n
"""
Введите порядковый номер искомого простого числа: 1000
7919
7919
==================================================
Время выполнения первого алгоритма: 212.3193199
Время выполнения второго алгоритма: 62.64389540000002
==================================================
         4 function calls in 0.202 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.201    0.201 <string>:1(<module>)
        1    0.201    0.201    0.201    0.201 task_5.py:25(simple)
        1    0.000    0.000    0.202    0.202 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


**************************************************
         13 function calls in 0.063 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.063    0.063 <string>:1(<module>)
        1    0.062    0.062    0.063    0.063 task_5.py:45(get_prime_sieve)
        1    0.001    0.001    0.001    0.001 task_5.py:47(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_5.py:56(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_5.py:61(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_5.py:73(<listcomp>)
        1    0.000    0.000    0.063    0.063 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        
=====================================================================
=====================================================================

Введите порядковый номер искомого простого числа: 100
541
541
==================================================
Время выполнения первого алгоритма: 11.793079500000001
Время выполнения второго алгоритма: 4.892353
==================================================
         4 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_5.py:25(simple)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


**************************************************
         9 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_5.py:45(get_prime_sieve)
        1    0.000    0.000    0.000    0.000 task_5.py:47(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_5.py:56(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        
==================================================================================
==================================================================================
Введите порядковый номер искомого простого числа: 10
29
29
==================================================
Время выполнения первого алгоритма: 1.0063403000000002
Время выполнения второго алгоритма: 1.3007432000000003
==================================================
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_5.py:25(simple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


**************************************************
         9 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_5.py:45(get_prime_sieve)
        1    0.000    0.000    0.000    0.000 task_5.py:47(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_5.py:56(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
                
"""
