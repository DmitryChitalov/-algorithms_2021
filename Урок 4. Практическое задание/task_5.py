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


def eratosthenes(n):
    sieve_list = n * 100  # Для создания достаточно большого листа для сита
    sieve = [num for num in range(sieve_list + 1)]
    # sieve[1] = 0
    i = 2  # Начинем перебор с индекса 2
    while i <= sieve_list:  # O(logN)
        if sieve[i] != 0:
            s = i + i
            while s <= sieve_list:
                sieve[s] = 0
                s += i
        i += 1

    result = sorted(list(set(sieve)))
    result.remove(0)
    return result[n]


# i = int(input('Введите порядковый номер искомого простого числа: '))
print(f'Время simple для 10 ({simple(10)}):')
print(timeit(stmt="simple(10)", globals=globals(), number=100))
print(f'Время simple для 100 ({simple(100)}):')
print(timeit(stmt="simple(100)", globals=globals(), number=100))
print(f'Время simple для 1000 ({simple(1000)}):')
print(timeit(stmt="simple(1000)", globals=globals(), number=100))
print('/*/*/*/*/*/*/*/*/*/*/*/*/*')
print(f'Время eratosthenes для 10 ({eratosthenes(10)}):')
print(timeit(stmt="eratosthenes(10)", globals=globals(), number=100))
print(f'Время eratosthenes для 100 ({eratosthenes(100)}):')
print(timeit(stmt="eratosthenes(100)", globals=globals(), number=100))
print(f'Время eratosthenes для 1000 ({eratosthenes(1000)}):')
print(timeit(stmt="eratosthenes(1000)", globals=globals(), number=100))
print(f'Время eratosthenes для 10000 ({eratosthenes(10000)}):')
print(timeit(stmt="eratosthenes(10000)", globals=globals(), number=100))
"""

Время simple для 10 (29):
0.0016990960000000006
Время simple для 100 (541):
0.22727507799999996
Время simple для 1000 (7919):
38.797282078
/*/*/*/*/*/*/*/*/*/*/*/*/*
Время eratosthenes для 10 (29):
0.030998640999996496
Время eratosthenes для 100 (541):
0.4435348469999951
Время eratosthenes для 1000 (7919):
3.9758143249999947
Время eratosthenes для 10000 (104729):
56.463838735

Функция simple имеет квадратичную сложность O(n^2), 
функция eratosthenes O(logN), заметно, что с ростом пространства решета и порядковым номером искомого простого числа
эфективность функции решета  Эратосфена растет
"""