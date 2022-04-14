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

my_list = list(range(100000))
my_deque = deque(range(100000))


def fill_list():
    my_list.append(0)
    return my_list


def fill_deque():
    my_deque.append(0)
    return my_deque


def insert_left():
    my_list.insert(0, 0)
    return my_list


def append_left():
    my_deque.appendleft(0)
    return my_deque


def pop_left_list():
    return my_list.pop(0)


def pop_left():
    return my_deque.popleft()


def extend_list():
    result = [1, 2, 3] + my_list
    return result


def extend_left():
    my_deque.extendleft([1, 2, 3])
    return my_deque


print(f'Заполнение списка: ', timeit("fill_list()", globals=globals(), number=1000000))
print(f'Заполнение deque: ', timeit("fill_deque()", globals=globals(), number=1000000))
print(f'Замеры функции appendleft для списка: ', timeit("insert_left()", globals=globals(), number=10000))
print(f'Замеры функции appendleft для deque: ', timeit("append_left()", globals=globals(), number=10000))
print(f'Замеры функции popleft для списка: ', timeit("pop_left_list()", globals=globals(), number=1000))
print(f'Замеры функции popleft для deque: ', timeit("pop_left()", globals=globals(), number=1000))
print(f'Замеры функции extendleft для списка: ', timeit("extend_list()", globals=globals(), number=1000))
print(f'Замеры функции extendleft для deque: ', timeit("extend_left()", globals=globals(), number=1000))

# Вывод: Из результатов замеров видно, что если необходимо производить операции appendleft, extendleft и popleft,
# то лучше использовать deque.
