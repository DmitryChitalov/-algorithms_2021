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

def create_list():
    ls = [el for el in range(100)]
    return ls

def create_deque():
    dq = deque(el for el in range(100))
    return dq

def addendum_list_1(ls):
    for el in range(-100, -1):
        ls.insert(0, el)
    return ls

def addendum_list_2(ls):
    for el in range(-100, -1):
        ls.append(el)
    return ls


def addendum_deque(dq):
    for el in range(-100, -1):
        dq.appendleft(el)
    return dq

def removal_list_1(ls):
    for el in range(100):
        ls.pop(0)
    return ls

def removal_list_2(ls):
    for el in range(100):
        ls.pop()
    return ls

def removal_deque(dq):
    for el in range(100):
        dq.popleft()
    return dq

def adding_list_in_list(ls):
    ls.extend(ls)
    return ls

def adding_list_in_deque(dq):
    dq.extendleft(dq)
    return dq


print('ЗАПОЛНЕНИЕ МАССИВА')
print('create_list  => ', timeit(f'create_list()', globals=globals(), number=100000))
print('create_deque => ', timeit(f'create_deque()', globals=globals(), number=100000))
print('ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В МАССИВ')
print('insert:      => ', timeit(f'addendum_list_1(create_list())', globals=globals(), number=100000))
print('append:      => ', timeit(f'addendum_list_2(create_list())', globals=globals(), number=100000))
print('appendleft:  => ', timeit(f'addendum_deque(create_deque())', globals=globals(), number=100000))
print('УДАЛЕНИЕ ЭЛЕМЕНТОВ ИЗ МАССИВА')
print('pop(0):      => ', timeit(f'removal_list_1(create_list())', globals=globals(), number=100000))
print('pop:         => ', timeit(f'removal_list_2(create_list())', globals=globals(), number=100000))
print('popleft:     => ', timeit(f'removal_deque(create_deque())', globals=globals(), number=100000))
print('ДОБАВЛЕНИЕ СПИСКА В МАССИВ')
print('extend:      => ', timeit(f'adding_list_in_list(create_list())', globals=globals(), number=100000))
print('extendleft:  => ', timeit(f'adding_list_in_deque(create_deque())', globals=globals(), number=100000))

'''
    Проведенные замеры показывают, что заполнение массива осуществляется быстрее list. А вот для 
поэлементного добавления (удаления) в (из) начало(а) списка лучше использовать в начало deque. 
'''