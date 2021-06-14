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

# Как и предполагалось вставка в начало и удаление из начала для деки(дек) на пару порядков быстрее, работа с
# концами и там и там одинаковая


from random import randint
from timeit import timeit
from collections import deque


def list_append(lst):
    for i in range(100):
        lst.append(randint(1, 5000))


def deq_append(deq):
    for i in range(100):
        deq.append(randint(1, 5000))


def list_ins_begin(lst):
    for i in range(100):
        lst.insert(0, randint(1, 5000))


def deq_ins_begin(deq):
    for i in range(100):
        deq.appendleft(randint(1, 5000))


def list_pop(lst):
    for i in range(100):
        lst.pop()


def deq_pop(deq):
    for i in range(100):
        deq.pop()


def list_pop_begin(lst):
    for i in range(100):
        lst.pop(0)


def deq_pop_begin(deq):
    for i in range(100):
        deq.popleft()


my_lst = [randint(1, 5000) for el in range(1, 100000)]
my_deq = deque(my_lst)
print('Вставка в конец лист/дека')
print(timeit("list_append(my_lst)", globals=globals(), number=10000))
print(timeit("deq_append(my_deq)", globals=globals(), number=10000))
print('Вставка в начало лист/дека')
print(timeit("list_ins_begin(my_lst)", globals=globals(), number=100))
print(timeit("deq_ins_begin(my_deq)", globals=globals(), number=100))
print('Удаление с начала лист/дека')
print(timeit("list_pop_begin(my_lst)", globals=globals(), number=100))
print(timeit("deq_pop_begin(my_deq)", globals=globals(), number=100))
print('удаление с конца лист/дека')
print(timeit("list_pop(my_lst)", globals=globals(), number=10000))
print(timeit("deq_pop(my_deq)", globals=globals(), number=10000))
