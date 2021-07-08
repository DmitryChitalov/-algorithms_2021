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


# def reshat_eratosfen(num):
#     a = [x for x in range(num+1)]
#     a[1] = 0
#     i = 2
#     while i < num:
#         if a[i] != 0:
#             j = i + i
#             while j <= num:
#                 a[j] = 0
#                 j += i
#         i += 1
#     a = sorted(list(set(a)))
#     a.remove(0)
#     return a[-1]



def my_func(num):   # квадратичное
    if num == 1:    # константное
        return 2    # константное
    prime = [2, 3]  # константное
    while len(prime) < num:     # линейное
        candidate = prime[-1] + 2   # константное
        iter = len(prime) + 1   # константное
        while iter > len(prime):    # линейное
            i = 0                   # константное
            while i < len(prime):   # линейное
                if candidate % prime[i] == 0:   # константное
                    break   # константное
                i += 1      # константное
            else:       # константное
                prime.append(candidate) # константное
            candidate += 2  # константное
    return prime[-1]    # константное

print(my_func(i))

# print(timeit('simple(i)', globals=globals()))
# print(timeit('my_func(i)', globals=globals()))
# print(timeit('reshat_eratosfen(71)', globals=globals()))
