"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from collections import deque
from timeit import timeit
from random import randint

n = 10000
list1 = []
deque1 = deque()
list2 = [i for i in range(n)]
deque2 = deque([i for i in range(n)])


def fill_list(l):
    for i in range(n):
        l.insert(0, i)
    return l


def fill_deque(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_list(l):
    for i in range(n):
        l[randint(1, 1000)] = randint(1, 100)
    return l


def change_deque(dq):
    for i in range(n):
        dq[randint(1, 1000)] = randint(1, 100)
    return dq


print('Время заполнения списка при 10 повторениях: ', timeit(
    'fill_list(list1)',
    setup='from __main__ import fill_list, list1, n',
    number=10
))

print('Время заполнения двусторонней очереди при 10 повторениях: ', timeit(
    'fill_deque(deque1)',
    setup='from __main__ import fill_deque, deque1, n',
    number=10
))

print('-' * 100)
print('Время изменения списка при 10 повторениях: ', timeit(
    'change_list(list2)',
    setup='from __main__ import change_list, list2, n',
    number=10
))
print('Время изменения двусторонней очереди при 10 повторениях: ', timeit(
    'change_deque(deque2)',
    setup='from __main__ import change_deque, deque2, n',
    number=10
))
