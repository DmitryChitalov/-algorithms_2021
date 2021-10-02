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


import timeit


# Сложность: O(n^2) (наверное)
# Простой алгоритм: перебираем делители числа, если оно делится только на себя и на единицу, то прибавляем к count
# единицу и идем дальше до указанного последнего простого числа.
def simple(last_num):
    count = 1
    num = 2
    while count <= last_num:
        divider = 1
        is_simple = True
        while divider <= num:
            if num % divider == 0 and divider != 1 and divider != num:
                is_simple = False
                break
            divider += 1
        if is_simple:
            if count == last_num:
                break
            count += 1
        num += 1
    return num


# Сложность O(n log(log n))
# Как я понял, если число простое, то числа кратные ему тоже являются простыми не будут и мы их отмечаем False и так
# дальше в цикле, а после этого достаем последнее значение.
def eratosfen(i, l=500):
    n = 2
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] == 1:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


# Если граница подобрана оптимально, то решето значительно быстрее.


if __name__ == '__main__':
    a10 = timeit.timeit('simple(10)', globals=globals(), number=100)
    a100 = timeit.timeit('simple(100)', globals=globals(), number=100)
    a1000 = timeit.timeit('simple(1000)', globals=globals(), number=100)
    b10 = timeit.timeit('eratosfen(10, 30)', globals=globals(), number=100)
    b100 = timeit.timeit('eratosfen(100, 542)', globals=globals(), number=100)
    b1000 = timeit.timeit('eratosfen(1000, 7920)', globals=globals(), number=100)
    print(a10, a100, a1000, b10, b100, b1000)
