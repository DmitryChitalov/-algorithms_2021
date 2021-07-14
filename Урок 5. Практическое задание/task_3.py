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
import random

n = 1000
lst1 = []
lst2 = [i for i in range(n)]
deq1 = deque()
deq2 = deque([i for i in range(n)])


def list_start(lst, n):
    """Вставка элементв в начало списка"""
    for i in range(n):
        lst.insert(0, i)
    return lst


def list_change(lst, n):
    """Изменяет n случайных элементов списка"""
    len_lst = len(lst)
    for i in range(n):
        lst[random.randint(1, len_lst-1)] = random.random()
    return lst


def deque_start(dq, n):
    """Заполняет пустую очередь"""
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_deque(deq, n):
    """Изменяет n случайных элементов очереди"""
    deq_len = len(deq)
    for i in range(n):
        deq[random.randint(1, deq_len-1)] = random.random()
    return deq


print("Время заполнения списка при 100 повторениях: ", timeit(
        "list_start(lst1, n)",
        setup="from __main__ import list_start, lst1, n",
        number=100
    ))

print("Время заполнения двусторонней очереди при 100 повторениях: ", timeit(
        "deque_start(deq1, n)",
        setup="from __main__ import deque_start, deq1, n",
        number=100
    ))

print("==============================================================")
print("Время изменения списка при 100 повторениях: ", timeit(
        "list_change(lst2, n)",
        setup="from __main__ import list_change, lst2, n",
        number=100
    ))
print("Время изменения двусторонней очереди при 100 повторениях: ", timeit(
        "change_deque(deq2, n)",
        setup="from __main__ import change_deque, deq2, n",
        number=100
    ))

"""
Очередь заполняет список в начале на три порядка быстрее, что ожидаемо, 
изменение элементов заполненных объектов происходит примерно одинаково"""