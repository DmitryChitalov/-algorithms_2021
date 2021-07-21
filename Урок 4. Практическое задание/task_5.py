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
from timeit import timeit


def simple(i):
    """
    Без использования «Решета Эратосфена».
    Сложность: O(N^2)
    """
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


def sieve_of_eratosthenes(n):
    """
    Create a boolean array "prime[0..n]" and initialize
    all entries it as true. A value in prime[i] will
    finally be false if i is Not a prime, else true.
    Сложность: вероятно - O(N).
    """
    final_list = list()
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    for p in range(n + 1):
        if prime[p]:
            final_list.append(p)

    return final_list


"""x = int(input('Введите порядковый номер искомого простого числа: '))
print(x)"""

print(simple(168))
print(*sieve_of_eratosthenes(1000))


print("simple: ", timeit(stmt="simple(168)", number=1000, globals=globals()))
print("sieve_of_eratosthenes: ", timeit(stmt="sieve_of_eratosthenes(1000)", number=1000, globals=globals()))

"""
Функции выводят разные данные. Simple показывает порядковый номер искомого простого числа (10 это 29). 
Sieve_of_eratosthenes выводит ряд простых чисел [0..n] (10 это 2 3 5 7). Соответственно операций функция Simple 
выполняет больше при одинаковом входящем параметре. Для более-менее объективного теста придётся скореектировать 
входящие параметры.   

Тест 1:
simple(4)
sieve_of_eratosthenes(10)

print(simple(4)): 7
print(*sieve_of_eratosthenes(10)): 2 3 5 7
simple:  0.8017927999999999
sieve_of_eratosthenes:  0.6082182

Тест 2:
simple(25)
sieve_of_eratosthenes(100)

print(simple(25)): 97
print(*sieve_of_eratosthenes(100)): 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
simple:  29.4652797
sieve_of_eratosthenes:  3.184562200000002

Тест 3:
С количеством повторений теста 100000 не дождался результата. Уменьшил количество повторений до 1000.
simple(168)
sieve_of_eratosthenes(1000)

print(simple(168)): 997
print(*sieve_of_eratosthenes(1000)): 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 
109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 
277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 
461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 
653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 
859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997

simple:  17.5120656
sieve_of_eratosthenes:  0.3224815999999997

> Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее.
Очевидно, что с увеличением количества вычисляемых простых чисел использование алгоритма Эратосфена 
гораздо эффективнее, чем перебор.
"""
