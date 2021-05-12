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


some_list = list()
some_deque = deque()


def list_append():
        some_list.append('test1')


def list_left_insert():
        some_list.insert(0, 'test2')


def deque_left_append():
        some_deque.appendleft('test2')


def deque_append():
        some_deque.append('test1')


def list_index():
        some_list.index('test1')


def deque_index():
        some_deque.index('test1')


def pop_left_list():
        some_list.pop(0)


def pop_left_deque():
        some_deque.popleft()


def pop_deque():
        some_deque.pop()


def pop_list():
        some_list.pop()


list_append()
deque_left_append()

print(f'Добавление в НАЧАЛО СПИСКА: {timeit("list_left_insert()", globals=globals(), number=100000)}')
print(f'Добавление в НАЧАЛО ДЕКА: {timeit("deque_left_append()", globals=globals(), number=100000)}')
# Добавление в НАЧАЛО СПИСКА: 2.2248623000000003
# Добавление в НАЧАЛО ДЕКА: 0.0108066
print(f'Добавление в КОНЕЦ СПИСКА: {timeit("list_append()", globals=globals(), number=100000)}')
print(f'Добавление в КОНЕЦ ДЕКА: {timeit("deque_append()", globals=globals(), number=100000)}')
# Добавление в КОНЕЦ СПИСКА: 0.009787400000000446
# Добавление в КОНЕЦ ДЕКА: 0.01383570000000045
print(f'Взятие по индексу из СПИСКА: {timeit("list_index()", globals=globals(), number=1000)}')
print(f'Взятие по индексу из ДЕКА: {timeit("deque_index()", globals=globals(), number=1000)}')
# Взятие по индексу из СПИСКА: 1.5863710000000002
# Взятие по индексу из ДЕКА: 1.8640840000000005
print(f'Удаления из НАЧАЛА СПИСКА: {timeit("pop_left_list()", globals=globals(), number=100000)}')
print(f'Удаления из НАЧАЛА ДЕКА: {timeit("pop_left_deque()", globals=globals(), number=100000)}')
# Удаления из НАЧАЛА СПИСКА: 1.7805083000000002
# Удаления из НАЧАЛА ДЕКА: 0.00919559999999997
print(f'Удаление из КОНЦА СПИСКА: {timeit("pop_list()", globals=globals(), number=100000)}')
print(f'Удаление из КОНЦА ДЕКА: {timeit("pop_deque()", globals=globals(), number=100000)}')
# Удаление из КОНЦА СПИСКА: 0.012712200000000173
# Удаление из КОНЦА ДЕКА: 0.009799300000000066
''' 
    Добавление и удаление в начало списка медленее чем у дека, из за разницы сложностей операции
линейной у списка и константной у дека.
    Добавление и удаление в конец списка не уступает деку, т.к. сложности операций одинаковые.
    Взятие по индексу быстрее в списке.
    Можно утверждать что документация верна.
'''