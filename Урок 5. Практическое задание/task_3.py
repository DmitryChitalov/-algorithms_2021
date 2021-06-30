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

from collections import deque
from timeit import timeit


my_deque = deque([])
my_list = []

def append_list(lst):
    for i in range(10000):
        lst.append(i)
    return lst


def append_deque(deq):
    for i in range(10000):
       deq.append(i)
    return deq


def insert_list(lst):
    for i in range(10000):
        lst.insert(0, i)


def appendleft_deque(deq):
    for i in range(10000):
        deq.appendleft(i)


def change_list(lst):
    for i in range(10000):
        lst[i] = lst[i] + 1

def change_deque(deq):
    for i in range(10000):
        deq[i] = deq[i] + 1


print(f"append_list {timeit('append_list(my_list)', globals=globals(), number = 10)}")
print(f"append_deque {timeit('append_deque(my_deque)', globals=globals(), number = 10)}")
print(f"insert_list {timeit('insert_list(my_list)', globals=globals(), number = 10)}")
print(f"appendleft_deque {timeit('appendleft_deque(my_deque)', globals=globals(), number = 10)}")

lst2 = append_list(my_list)
deq2 = append_deque(my_deque)
print(f"change_list {timeit('change_list(lst2)', globals=globals(), number = 10)}")
print(f"change_deque {timeit('change_deque(deq2)', globals=globals(), number = 10)}")

"""Добавление в конец списка и конец дека происходит примерно за одно и тоже время, т.к. сложность одинаковая О(1)
Добавление в начало значительно быстрее в деке. Остальные операции имеют одинаковую  сложность и незначительно быстрее в 
обычном списке"""
