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


my_list = []
my_deque = deque()


def full_list(n):
    for el in range(n):
        my_list.append(el)


def full_deque(n):
    for el in range(n):
        my_deque.append(el)


print(f'__________________________________________')
print(f'Добавление в лист')
print(f'{timeit("full_list(10000)",globals=globals(),number=1)}'[:10])
print(f'Добавление в deque')
print(f'{timeit("full_deque(10000)",globals=globals(),number=1)}'[:10])
print('Добавление быстрее deque')


def one_position_list(n):
    for el in range(n):
        my_list.insert(0, el)


def one_position_deque(n):
    for el in range(n):
        my_deque.appendleft(el)


print(f'__________________________________________')
print(f'Добавление в начало лист')
print(f'{timeit("one_position_list(10000)",globals=globals(),number=1)}'[:10])
print(f'Добавление в начало deque')
print(f'{timeit("one_position_deque(10000)",globals=globals(),number=1)}'[:10])
print('Добавление быстрее deque')


def index_list():
    count = len(my_list) // 7
    while count <= 0:
        my_list.index(count, my_list)
        count -= 1


def index_deque():
    count = len(my_deque) // 7
    while count <= 0:
        my_deque.index(count, my_deque)
        count -= 1


print(f'__________________________________________')
print(f'Поиск индекса элемента лист')
print(f'{timeit("index_list()",globals=globals(),number=1)}'[:10])
print(f'Поиск индекса элемента deque')
print(f'{timeit("index_deque()",globals=globals(),number=1)}'[:10])
print('Поиск индекса быстрее лист')


def mid_add_list():
    mid = len(my_list) // 2
    my_list.insert(mid, mid)


def mid_add_deque():
    mid = len(my_deque) // 2
    my_deque.insert(mid, mid)


print(f'__________________________________________')
print(f'Добавление в середину лист')
print(f'{timeit("mid_add_list()",globals=globals(),number=10000)}'[:10])
print(f'Добавление в середину deque')
print(f'{timeit("mid_add_deque()",globals=globals(),number=10000)}'[:10])
print('Добавление в середину быстрее list')


def pop_one_list():
    my_list.pop(0)


def pop_one_deque():
    my_deque.popleft()


print(f'__________________________________________')
print(f'Удаление первого элемента лист')
print(f'{timeit("pop_one_list()",globals=globals(),number=10000)}'[:10])
print(f'Удаление первого элемента deque')
print(f'{timeit("pop_one_deque()",globals=globals(),number=10000)}'[:10])
print('Удаление первого элемента быстрее deque')


def pop_list():
    my_list.pop()


def pop_deque():
    my_deque.pop()


print(f'__________________________________________')
print(f'Удаление последнего элемента лист')
print(f'{timeit("pop_list()",globals=globals(),number=10000)}'[:10])
print(f'Удаление последнего элемента deque')
print(f'{timeit("pop_deque()",globals=globals(),number=10000)}'[:10])
print('Удаление последнего элемента быстрее deque')
print(f'__________________________________________')
print('Добавление в конец, добавление в начало, удаление последнего и первого элемента -- быстрее deque')
print('Добавление в середину, поиск индекса -- быстрее list')