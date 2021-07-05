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
from time import time

my_list = []
my_deque = deque()


def timer(func):
    def wrapped(*args):
        start = time()
        response = func(*args)
        print(f'Время выполнения функции {func.__name__}: {time() - start}')  #
        return response
    return wrapped


@timer
def list_insert(lst):
    for i in range(100000):
        lst.insert(0, i)


@timer
def deque_appendleft(dq):
    for i in range(100000):
        dq.appendleft(i)


@timer
def list_pop(lst):
    for i in range(len(lst)):
        lst.pop(0)


@timer
def deque_popleft(dq):
    for i in range(len(dq)):
        dq.popleft()


list_insert(my_list)
deque_appendleft(my_deque)
list_pop(my_list)
deque_popleft(my_deque)
"""
Вывод:
Время выполнения функции list_insert: 2.6165153980255127
Время выполнения функции deque_appendleft: 0.005004405975341797
Время выполнения функции list_pop: 0.9896032810211182
Время выполнения функции deque_popleft: 0.00502467155456543

Добавление элемента в начало работает гораздо быстрее в deque, чем в обычном списке. Также и удаление
элемента из начала обычного списка занимает в тысячи раз больше времени, чем удаление элемента из начала списка
в deque

Следовательно, deque очень эффективно и быстро справляется с задачами добавления и извлечения объектов.
"""
