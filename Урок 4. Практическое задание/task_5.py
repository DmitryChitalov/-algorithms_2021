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

def simple(i): # O(n^2)
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

def sieve(prime_num): # $O(nlog(log n))
    """Реализация решета Эратосфена"""
    right_edge = prime_num *10
    sieve_lst = list(range(right_edge))
    sieve_lst[1] = 0
    curr = 2
    while curr < right_edge:
        if sieve_lst[curr]:
            del_idx = curr * 2
            while del_idx < right_edge:
                sieve_lst[del_idx] = 0
                del_idx += curr
        curr += 1
    for i in sieve_lst:
        if not i:
            pass
        else:
            if prime_num == 1:
                return i
            else:
                prime_num -= 1

i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(sieve(i))
print(timeit.timeit('simple(i)',number=100,globals=globals()))
print(timeit.timeit('sieve(i)',number=100,globals=globals()))
"""
Введите порядковый номер искомого простого числа: 10
29
29
0.0018560000000000798
0.0023684999999993295

Введите порядковый номер искомого простого числа: 100
541
541
0.1951539000000002
0.024121700000000246

Введите порядковый номер искомого простого числа: 1000
7919
7919
35.7107977
0.300438800000002

Различие трудоемкости алгоритмов состаавляет 10^(lg(n)-1)  и для простого алгоритма
очень быстро растет.
"""
