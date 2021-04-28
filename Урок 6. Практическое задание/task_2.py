"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from memory_profiler import memory_usage
import timeit
import task_2_cython as cp


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
    prime_num = a[n - 1]
    return prime_num


start_timer_1 = timeit.default_timer()
memory_1 = memory_usage()[0]

n_5000 = 5000
print('Python sieve(5000): ', sieve(n_5000))

print(f' *** Использование памяти  - {memory_usage()[0] - memory_1} MiB.')
print(f' *** Время выполнения  - {timeit.default_timer() - start_timer_1} сек.')

start_timer_2 = timeit.default_timer()
memory_2 = memory_usage()[0]

print('Cython sieve(5000): ', cp.sieve_cython(n_5000))

print(f' *** Использование памяти  - {memory_usage()[0] - memory_2} MiB.')
print(f' *** Время выполнения  - {timeit.default_timer() - start_timer_2} сек.')


"""

Еще один из возможных вариантов оптимизации - использовании библиотеки Cython.
Cython позволяет писать обычный Python-код с некоторыми незначительными модификациями, такими как
добавление к переменной информации о ее типе и затем транслировать его в С-код
Такой подход позволяет более оптимально использовать память, а также ускоряет работу Python-программ.

Ниже приведены резульаты выполнения алгоритма Решето Эратосфена для кода на Python и Cython:

Python sieve(5000):  48611
 *** Использование памяти  - 0.34765625 MiB.
 *** Время выполнения  - 0.2181051989991829 сек.

Cython sieve(5000):  48611
 *** Использование памяти  - 0.2578125 MiB.
 *** Время выполнения  - 0.20859971400022914 сек.

"""

