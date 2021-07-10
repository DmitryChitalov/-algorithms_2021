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
from math import log, ceil
from timeit import timeit


def simple(i):
    """Без использования «Решета Эратосфена», O(N^2)"""
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


def sieve(i):
    """C использованием «Решета Эратосфена», решение по ссылке, O(NloglogN)"""
    numbers = []
    maxval = 1.2 * i * log(1.20661 * i + 0.00435) + 3  # число, полученное из номера, которое
    for k in range(ceil(maxval)):                      # заведомо больше нашего простого числа под этим номером
        numbers.append(k)                              # вне зависимости от порядка номера

    k = 2
    while k <= maxval:
        if numbers[k] != 0:
            j = k + k
            while j <= maxval:
                numbers[j] = 0
                j = j + k
        k += 1

    numbers = [i for i in numbers if i != 0]
    return numbers[i]


def my_sieve(i):
    """C использованием «Решета Эратосфена», мое решение, O(N^2)"""
    numbers = []
    maxval = 1.2 * i * log(1.20661 * i + 0.00435) + 3  # число, полученное из номера, которое
    for k in range(ceil(maxval)):                      # заведомо больше нашего простого числа под этим номером
        numbers.append(k)                              # вне зависимости от порядка номера

    for k in range(4, len(numbers)):
        if k % 2 == 0 or k % 3 == 0 or (k % 5 == 0 and k != 5):
            numbers[k] = 0
    numbers = [i for i in numbers if i != 0]

    for k in range(4, len(numbers)):
        for n in range(4, len(numbers)):
            if numbers[k] != 0 and numbers[n] % numbers[k] == 0 and n != k:
                numbers[n] = 0

    numbers = [i for i in numbers if i != 0]
    return numbers[i]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(sieve(i))
print(my_sieve(i))
print('//N = 10------------')
print('Наивный перебор:\n', timeit('simple(10)', globals=globals(), number=1))
print('Решето:\n', timeit('sieve(10)', globals=globals(), number=1))
print('Решето, мой алгоритм:\n', timeit('my_sieve(10)', globals=globals(), number=1))
print('//N = 100------------')
print('Наивный перебор:\n', timeit('simple(100)', globals=globals(), number=1))
print('Решето:\n', timeit('sieve(100)', globals=globals(), number=1))
print('Решето, мой алгоритм:\n', timeit('my_sieve(100)', globals=globals(), number=1))
print('//N = 1000------------')
print('Наивный перебор:\n', timeit('simple(1000)', globals=globals(), number=1))
print('Решето:\n', timeit('sieve(1000)', globals=globals(), number=1))
print('Решето, мой алгоритм:\n', timeit('my_sieve(1000)', globals=globals(), number=1))

'''
    Решето конечно эффективнее, так как затраты растут гораздо медленнее квадратичной зависимости, 
    различие проявляется критично с ростом номера числа 
    Мне не удалось написать алгоритм эффективнее, чем у древних греков, сложность вышла тоже квадратичная
'''