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

import math
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


"""С использованием «Решета Эратосфена»"""


def is_simple(num, my_list):
    dividers = [el for el in my_list if num % el == 0]
    return len(dividers) == 0


def my_simple(i):
    simple_nums = [2, 3]
    if i < 2:
        return simple_nums[0]
    elif i == 2:
        return simple_nums[1]
    counter = 4
    while True:
        if is_simple(counter, simple_nums):
            simple_nums.append(counter)
        if len(simple_nums) == i:
            return simple_nums[-1]
        counter += 1


if __name__ == '__main__':
    print(simple(1000))
    print(my_simple(1000))

    print(timeit('simple(10)', globals=globals(), number=1000))
    print(timeit('my_simple(10)', globals=globals(), number=1000))
    print(timeit('simple(100)', globals=globals(), number=1000))
    print(timeit('my_simple(100)', globals=globals(), number=1000))
    print(timeit('simple(1000)', globals=globals(), number=100))
    print(timeit('my_simple(1000)', globals=globals(), number=100))
    print(timeit('simple(10000)', globals=globals(), number=10))
    print(timeit('my_simple(10000)', globals=globals(), number=10))


"""
0.03593852499034256
0.04531006398610771
2.3457276769913733
1.7369118540082127
38.962435688998085
27.5903577489662
640.4655136930523
414.4120352159953

Process finished with exit code 0

сложность первой функции О(n**3)
сложность второй функции О(n**2)

в первом случае мы просчитываем для каждого числа возможность деления на каждого числа до него без остатка
во втором случаем мы проверяем деление каждого числа на простые числа до него,
т.е. нам не надо раз за разом проходить все числа, которые были до этого числа.
Безусловно второй метод более эффективный, хотя и также ресурсозатратный
"""
