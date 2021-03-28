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

# O(n**2)
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

# O(n log(log n))
def er(i):
    numbers = list(range(10000))
    m = 2
    while m < len(numbers):
        if numbers[m] != 0:
            j = m * 2
            while j < len(numbers):
                numbers[j] = 0
                j += m
        m += 1
    element = set(numbers)
    element = sorted(list(element))
    return element[i+1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(er(i))

print('Simple --->', timeit('simple(i)', globals=globals(),number=100))
print('Eratos --->', timeit('er(i)', globals=globals(), number=100))

'''
10 число:
Simple ---> 0.002607000000000248
Eratos ---> 0.4207402

100 число:
Simple ---> 0.23228690000000007
Eratos ---> 0.45537839999999985

1000 число:
Simple ---> 36.6618763
Eratos ---> 0.4471812999999969

Решето работает быстрее на поиске большего i-го элеиента.

'''

