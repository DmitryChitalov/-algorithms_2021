"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from memory_profiler import memory_usage
import timeit


def sieve(n):
    m = n * 10
    a = [i for i in range(m + 1)]
    a[1] = 0
    i = 2

    while i <= m:
        if a[i] != 0:
            j = i + i
            while j <= m:
                a[j] = 0
                j = j + i
        i += 1

    a = [i for i in a if i != 0]
    return a[n - 1]


start_timer = timeit.default_timer()
memory_1 = memory_usage()[0]

n_3000 = 3000
print('sieve(3000): ', sieve(n_3000))

print(f' *** Использование памяти  - {memory_usage()[0] - memory_1} MiB.')
print(f' *** Время выполнения  - {timeit.default_timer() - start_timer} сек.')

start_timer = timeit.default_timer()
memory_1 = memory_usage()[0]

n_3000 = 3000
print('Cython sieve(3000): ', cp.sieve(n_3000))

print(f' *** Использование памяти  - {memory_usage()[0] - memory_1} MiB.')
print(f' *** Время выполнения  - {timeit.default_timer() - start_timer} сек.')
