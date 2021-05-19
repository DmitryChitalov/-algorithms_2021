"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import Timer


def bubble_sort1(n):
    lst = [randint(-100, 100) for i in range(n)]

    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return


def bubble_sort2(n):
    lst = [randint(-100, 100) for i in range(n)]

    for i in range(len(lst)-1):
        is_move = False
        for j in range(len(lst)-1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_move = True

        if not is_move:
            break

    return


n = 10
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_1', t.timeit(number=10))

n = 100
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_2', t.timeit(number=10))

n = 1000
t = Timer("bubble_sort1(n)", "from __main__ import bubble_sort1, n")
print('t1_3', t.timeit(number=10))

n = 10
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_1', t.timeit(number=10))

n = 100
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_2', t.timeit(number=10))

n = 1000
t = Timer("bubble_sort2(n)", "from __main__ import bubble_sort2, n")
print('t2_3', t.timeit(number=10))


# t1_1 0.0003116000000000091
# t1_2 0.016124399999999997
# t1_3 3.5524643
# t2_1 0.0002740000000001075
# t2_2 0.015260000000000051
# t2_3 2.7485299
