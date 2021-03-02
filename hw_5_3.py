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


def append_lst(lst):
    lst.append(1001)
    return lst


def insert_lst(lst):
    lst.insert(0, 1001)


def pop_lst_0(lst):
    lst.pop(0)
    return lst


def pop_lst_last(lst):
    lst.pop()
    return lst


def append_deq(deq):
    deq.append(1001)
    return deq


def insert_deq(deq):
    deq.appendleft(1001)
    return deq


def pop_deq_0(deq):
    deq.popleft()
    return deq


def pop_deq_last(deq):
    deq.pop()
    return deq


lst = [i for i in range(1000)]
deq = deque(lst)

print(timeit("append_lst(lst)", globals=globals(), number=100000))
print(timeit("append_deq(deq)", globals=globals(), number=100000))
print('---------------------------------------------')
print(timeit("insert_lst(lst)", globals=globals(), number=100000))
print(timeit("insert_deq(deq)", globals=globals(), number=100000))
print('---------------------------------------------')
print(timeit("pop_lst_0(lst)", globals=globals(), number=100000))
print(timeit("pop_deq_0(deq)", globals=globals(), number=100000))
print('---------------------------------------------')
print(timeit("pop_lst_last(lst)", globals=globals(), number=100000))
print(timeit("pop_deq_last(deq)", globals=globals(), number=100000))

# время добавление элемента в конец для списка и очереди практичеки одинаковое
# время добавления элемента в начало для очереди существенно ниже
# время удаления первого элемента для очереди существенно ниже
# время удаления последнего элемента ля списка и очереди практичеки одинаковое
