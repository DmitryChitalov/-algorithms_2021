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


def func(num_i, n_x=10):
    try:
        n = n_x * num_i
        list_x = list(range(2, n + 1))
        for num in list_x:
            if num != 0:
                for el in range(2 * num, n+1, num):
                    list_x[el-2] = 0
        return list(filter(lambda x: x != 0, list_x))[num_i - 1]
    except IndexError:
        return func(num_i, n_x*2)


for num_x in [10, 100, 1000]:
    print(f'Время выполнения функции simple: {timeit(stmt="simple(num_x)", globals=globals(), number=10)}')
    print(f'Время выполнения функции func: {timeit(stmt="func(num_x)", globals=globals(), number=10)}')
    print(func(num_x))
    print(func(num_x) == simple(num_x))


# решение с использованием решето эратосфена,
# уже на 100 элементе работает быстрее.
# так как сложность у него O(n*log(log n)
# а у simple сложность O(n**2)
