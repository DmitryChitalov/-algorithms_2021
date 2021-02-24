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


def simple(i):  # O(n**2)
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


def eratosphen(i):  # O(NlogN)
    simple = [2]
    number = 2
    count = 1
    while count < i:  # O(N)
        is_simple = True
        number += 1
        for el in simple:  # O(logN) - потому что на каждом шаге уменьшается число значений
            if number % el == 0:  # O(1)
                is_simple = False
                break
        if is_simple:  # O()
            simple.append(number)  # O(1)
            count += 1  # O(1)
        number += 1  # O(1)
    return simple[i-1]  # O(1)


# i = int(input('Введите порядковый номер искомого простого числа: '))
i = 220
print(simple(i))
print(eratosphen(i))

num = 10
print('Обычный алгоритм:', timeit("simple(num)", setup="from __main__ import simple, num", number=1000))
print('Решето Эратосфена:', timeit("eratosphen(num)", setup="from __main__ import eratosphen, num", number=1000))

"""
Алгоритм Эратосфена работает гораздо быстрее, потому что в данном алгоритме на каждом последующем шаге 
значительно уменьшается число элементов, с которыми мы сравниваем исходное число

"""