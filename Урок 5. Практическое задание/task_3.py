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
from collections import deque
test_list = list()
test_deque = deque()


def list_append():
    for el in range(10000):
        test_list.append(el)


def list_left_insert():
    for el in range(10000):
        test_list.insert(0, el)


def deque_left_append():
    for el in range(10000):
        test_deque.appendleft(el)


def deque_append():
    for el in range(10000):
        test_deque.append(el)


def pop_left_list():
    while len(test_list) != 0:
        test_list.pop(0)


def pop_left_deque():
    while len(test_deque) != 0:
        test_deque.popleft()


def pop_deque():
    while len(test_deque) != 0:
        test_deque.pop()


def pop_list():
    while len(test_list) != 0:
        test_list.pop()


list_append()
deque_left_append()
print(test_list)
print(f'Скорость добавления элемента в КОНЕЦ СПИСКА: {timeit("list_append()", globals=globals(), number=10)}')
print(f'Скорость удаления элемента с КОНЦА СПИСКА: {timeit("pop_list()", globals=globals(), number=10)}')
print(f'Скорость добавления элемента в НАЧАЛО СПИСКА: {timeit("list_left_insert()", globals=globals(), number=10)}')
print(f'Скорость удаления элемента с НАЧАЛА СПИСКА: {timeit("pop_left_list()", globals=globals(), number=10)}')
print(f'Скорость добавления элемента в НАЧАЛО ДЕКА: {timeit("deque_left_append()", globals=globals(), number=10)}')
print(f'Скорость удаления элемента с НАЧАЛА ДЕКА: {timeit("pop_left_deque()", globals=globals(), number=10)}')
print(f'Скорость добавления элемента в КОНЕЦ ДЕКА: {timeit("deque_append()", globals=globals(), number=10)}')
print(f'Скорость удаления элемента с КОНЦА ДЕКА: {timeit("pop_deque()", globals=globals(), number=10)}')


''' 1)Скорость добавления элемента в конец списка и в конец дека + - одинаковая, это объясняется сложностью функции 
        append O(1). 
    2)Скорость добавления элемента в начало списка на много ниже, чем скорость добавления элемента в начало дека.
        Это можно объяснить сложностью выполняемых функций. Сложность insert - O(N), сложность appendleft - O(1)
    3)Скорость удаления элемента с начла списка ниже, чем с начала дека т.к. сложность функции pop - O(N),
        a сложность функции popleft - O(1)
    4)Скорость удаления элемента с конца списка и с конца дека + - одинакова, в обоих случаях оспользуется функция 
        pop O(N)
    Вывод: При необходимости лучше использовать deque т.к. его функции оптимизированны => работают быстрее.'''
