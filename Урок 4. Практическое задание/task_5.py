"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (теорию по Решету нужно искать в сети)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from timeit import timeit


def simple(i):  # Алгоритмическая сложность O(n^2)
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


# Через решето Эратосфена

def eratosthenes(n):  # Алгоритмическая сложность O(n^2)
    my_list = [2]
    for k in range(3, n * 10, 2):
        i = 0
        while k > my_list[i]:
            if k % my_list[i] == 0:
                break
            elif my_list[i] * 2 > k:
                my_list.append(k)
                break
            i += 1
    return my_list[n - 1]


print(eratosthenes(i))
# Замеры
print(timeit('simple(10)', number=10, globals=globals()))  # 0.0003
print(timeit('eratosthenes(10)', number=10, globals=globals()))  # 0.0006

print(timeit('simple(100)', number=10, globals=globals()))  # 0.027
print(timeit('eratosthenes(100)', number=10, globals=globals()))  # 0.017

print(timeit('simple(1000)', number=10, globals=globals()))  # 4.895
print(timeit('eratosthenes(1000)', number=10, globals=globals()))  # 1.118

'''
Аналитика:
Чем дальше от 0 находиться простое число, тем больше времени необходимо для его вычисления
через алгоритм поиска простого числоа решета Эратосфена времени на поиск простого числа занимает в разы меньше времени
чем без его использования 
'''