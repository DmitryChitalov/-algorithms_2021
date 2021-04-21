"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from timeit import timeit
from random import randint
from collections import deque

my_list = [randint(1, 100) for i in range(1000)]
my_deque = deque(my_list)


def list_insert_left(my_l):
    my_l.insert(0, 1)
    return my_l


def deque_insert_left(my_deq):
    my_deq.appendleft(1)
    return my_deq


def list_pop_left(my_l):
    my_l.pop(0)
    return my_l


def deque_pop_left(my_deq):
    my_deq.popleft()
    return my_deq


def list_get(my_l):
    return my_l[777777]


def deque_get(my_deq):
    return my_deq[777777]


print(timeit('list_insert_left(my_list)',
             'from __main__ import list_insert_left, my_list', number=100000))

print(timeit('deque_insert_left(my_deque)',
             'from __main__ import deque_insert_left, my_deque', number=100000))

print(timeit('list_pop_left(my_list)',
             'from __main__ import list_pop_left, my_list', number=100000))

print(timeit('deque_pop_left(my_deque)',
             'from __main__ import deque_pop_left, my_deque', number=100000))

my_list = [randint(1, 100) for i in range(1000000)]
my_deque = deque(my_list)

print(timeit('list_get(my_list)',
             'from __main__ import list_get, my_list', number=100000))

print(timeit('deque_get(my_deque)',
             'from __main__ import deque_get, my_deque', number=100000))

# Данные замеры полностью подтверждают информацию в документации
# Добавление элементов происходит быстрее в деке, а доступ к элементу в листе