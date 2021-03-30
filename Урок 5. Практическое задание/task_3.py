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
from collections import deque
from timeit import Timer

list_obj = []

N = int(input('Введите размер дека/списка: '))
for i in range(N):
    value = input(f'{i}) Введите что-нибудь: ')
    list_obj.append(value)

deq_obj = deque(list_obj)


def deque_append():
    deq_obj.pop('something')


def deque_appendleft():
    deq_obj.popleft('something')


def list_insert_start():
    list_obj.insert(0, 'something')


def list_insert_back():
    list_obj.insert(-1, 'something')

t1 = Timer("deque_append()", "from __main__ import deque_append")
print("deque append", t1.timeit(number=10000), "seconds")

t2 = Timer("deque_appendleft()", "from __main__ import deque_appendleft")
print("deque appendleft", t2.timeit(number=10000), "seconds")

t3 = Timer("list_insert_start()", "from __main__ import list_insert_start")
print("list insert start", t3.timeit(number=10000), "seconds")

t4 = Timer("list_insert_back()", "from __main__ import list_insert_back")
print("list insert back", t4.timeit(number=10000), "seconds")
