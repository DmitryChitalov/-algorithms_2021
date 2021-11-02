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


def ff():
    n = int(input())
    m = n * 10
    s = (x for x in range(2, m+1) if x not in [i for sub in [list(range(2 * j, m+1, j)) for j in range(2, m // 2)] for i in sub])
    return [next(s) for i in range(n)][-1]

print(ff())

# def fff():
#     n = int(input())
#     ar = [True for i in range(n + 1)]
#     print(ar)
#     ar[0], ar[1] = False, False
#     print(ar)
#     ]

# print(fff())

# def fff(n):
#     ar = [i for i in range(1, n+1, 2)]
#     print(ar)
#     ar[0] = 2
#     print(ar)
#     arr =[]
#     for ind, el in enumerate(ar):
#         # print(ind, el)
#         for item in ar:
#             print(item)
#             if item % el == 0 and item / 1 == item :
#                 arr.append(item)
#                 break
    


# print(fff(10))



# n = int(input())
# a = []
# for i in range(n + 1):
#     a.append(i)
# a[1] = 0
# i = 2
# while i <= n:
#     if a[i] != 0:
#         j = i + i
#         while j <= n:
#             a[j] = 0
#             j = j + i
#     i += 1
# a = set(a)
# a.remove(0)
# print(a)

