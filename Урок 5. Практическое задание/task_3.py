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

from time import time
from collections import deque

def timer(func):
    def wrapped(*args):
        start = time()
        response = func(*args)
        print(f'Время выполнения функции {func.__name__}: {time() - start}')  #
        return response
    return wrapped


@timer
def fill_list_insert(l):             # заполнение списка методом insert
    for i in range(100000):
        l.insert(0, f'el{i}')


@timer
def fill_deque(d):                   # заполнение deque методом appendleft
    for i in range(100000):
        d.appendleft(f'el{i}')


@timer
def operations_list_extend(l):       # расширяем список сначала переворачивая его
    l.reverse()
    l.extend(range(1000000))
    l.reverse()


@timer
def operations_deque_extendleft(d):  # расширяем deque методом extendleft
    d.extendleft(range(1000000))


@timer
def operations_list_pop(l):          # очищаем список с начала в конец
    for i in range(len(l)):
        l.pop(0)


@timer
def operations_deque_popleft(d):     # очищаем deque методом popleft
    for i in range(len(d)):
        d.popleft()


test_list = []
test_deque = deque()

fill_list_insert(test_list)             # заполнение списка методом insert
fill_deque(test_deque)                  # заполнение deque методом appendleft

operations_list_extend(test_list)       # расширяем список сначала переворачивая его
operations_deque_extendleft(test_deque) # расширяем deque методом extendleft

operations_list_pop(test_list)          # очищаем список с начала в конец
operations_deque_popleft(test_deque)    # очищаем deque методом popleft


"""
вывод
заполнение deque происходит в разы быстрее
> Время выполнения функции fill_list_insert: 2.739314079284668
> Время выполнения функции fill_deque: 0.018988370895385742

а вот мой аналог функции extendleft для списка работает с такой же скоростью как и в deque
> Время выполнения функции operations_list_extend: 0.0199887752532959
> Время выполнения функции operations_deque_extendleft: 0.02198624610900879

popleft работает не сопоставимо быстрей чем аналог в списках
> Время выполнения функции operations_list_pop: 279.8265538215637
> Время выполнения функции operations_deque_popleft: 0.06396102905273438

форумы врут
"""

