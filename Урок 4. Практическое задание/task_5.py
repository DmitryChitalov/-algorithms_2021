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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def Sieve_of_Eratosthenes():
    n = i ** 2
    number_set = set(range(2, n))
    array = []
    while number_set:
        prime = min(number_set)
        array.append(prime)
        number_set -= set(range(prime, n, prime))
        if len(array) > i:
            break
    return array
print(Sieve_of_Eratosthenes()[i-1])

print(timeit("simple(i)", globals=globals(), number=1))
print(timeit("Sieve_of_Eratosthenes()", globals=globals(), number=1))

"""
Нашел другой вариант реализации алгоритма "Решето Эратосфена" и переделал его, чтобы можно было найти
i - е простое число. Этот алгоритм получился медленнее.
"""
