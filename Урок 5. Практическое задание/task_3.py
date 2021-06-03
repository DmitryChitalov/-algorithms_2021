"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from timeit import timeit
from collections import deque

lst = []

deque = deque()


def lst_filling():
    for el in range(1000):
        lst.append(el)


def deq_filling():
    for el in range(1000):
        deque.append(el)


print(timeit('lst_filling', globals=globals()))
print(timeit('deq_filling', globals=globals()))


def lst_insert():
    for el in range(10000):
        lst.insert(0, el)


def deque_insert():
    for el in range(10000):
        deque.appendleft(el)


print(timeit('lst_insert', globals=globals()))
print(timeit('deque_insert', globals=globals()))

# Судя по замерам можно сказать что они всегда разные, но приблизительно равны, однако в большинстве случаев
# deque уступает по скорости.
