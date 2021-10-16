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

deque_empty = deque()
lst_empty = []

full_lst = [i for i in range(10**4)]
full_deque = deque([i for i in range(10**4)])


def push_to_lst(lst):
    for i in range(1000):
        lst.append(i)
    return lst


def push_to_deque(deq):
    for i in range(1000):
        deq.append(i)
    return deq


def insert_to_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def left_to_deque(deq):
    for i in range(1000):
        deq.appendleft(i)
    return deq


def pop_lst(lst):
    for i in range(1000):
        lst.pop(0)
    return lst


def popleft_deq(deq):
    for i in range(1000):
        deq.popleft()
    return deq


print('Заполнение 1 - списка 2 - дека')
print(timeit('push_to_lst(lst_empty)', globals=globals(), number=10000))
print(timeit('push_to_deque(deque_empty)', globals=globals(), number=10000))

print('Вставка элементов в начало массива 1 - списка 2 - дека')
print(timeit('insert_to_lst(full_lst)', globals=globals(), number=100))
print(timeit('left_to_deque(full_deque)', globals=globals(), number=100))

print('Получение элементов из начала массива 1 - списка 2 - дека')
print(timeit('pop_lst(full_lst)', globals=globals(), number=100))
print(timeit('popleft_deq(full_deque)', globals=globals(), number=100))

"""
Заполнение массивов идет быстрее у deque, хотя и не на много (15 % примерно). Но вот при получении элементов или при
вставке элементов в начало массива, deque в огромное кол-во раз. Происходит это, я так понял, из-за того, что принцип
работы deque основывается на построении стека.
"""