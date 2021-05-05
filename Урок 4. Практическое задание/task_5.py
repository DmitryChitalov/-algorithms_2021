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

from timeit import default_timer, timeit


def simple(i):  # сложность O(n**2)
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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def eratosthenes(i):  # сложность O(log(log(n))), если я все правильно сделал) Так на занятии сказали)
    numbers = [_ for _ in range(10000)]
    numbers[1] = 0
    count = 0
    for n in numbers:
        if n:
            for _ in range(n + 2, len(numbers)):
                if numbers[_] % n == 0:
                    numbers[_] = 0
            count += 1
            if count == i:
                return n


print(eratosthenes(i))

print('Профилирование функции simple(10) через timeit: ' + str(timeit(
    'simple(10)',
    globals=globals(), number=1)))

print('Профилирование функции eratosthenes(10) через timeit: ' + str(timeit(
    'eratosthenes(10)',
    globals=globals(), number=1)))

print('Профилирование функции simple(100) через timeit: ' + str(timeit(
    'simple(100)',
    globals=globals(), number=1)))

print('Профилирование функции eratosthenes(100) через timeit: ' + str(timeit(
    'eratosthenes(100)',
    globals=globals(), number=1)))

print('Профилирование функции simple(1000) через timeit: ' + str(timeit(
    'simple(1000)',
    globals=globals(), number=1)))

print('Профилирование функции eratosthenes(1000) через timeit: ' + str(timeit(
    'eratosthenes(1000)',
    globals=globals(), number=1)))

'''
Вывод:
Решето эффективно только на больших числах. Так как с ним в любом случае генерируется большой массив, 
и происходят операции с его элементами. На маленьких же эффективнее первый метод, который в свою очередь можно 
еще оптимизировать.

Профилирование функции simple(10) через timeit: 7.570000000001187e-05
Профилирование функции eratosthenes(10) через timeit: 0.00880140000000007
Профилирование функции simple(100) через timeit: 0.0019122000000000305
Профилирование функции eratosthenes(100) через timeit: 0.08445110000000011
Профилирование функции simple(1000) через timeit: 0.31892299999999985
Профилирование функции eratosthenes(1000) через timeit: 0.5726100000000001
'''