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


def fill_list(count):
    return list(range(count))


def fill_deque(count):
    return deque(range(count))


def appendleft_list(el):
    lst.insert(0, el)
    return lst


def appendleft_deque(el):
    deq.appendleft(el)
    return deq


def popleft_list():
    lst.pop(0)
    return lst


def popleft_deque():
    deq.popleft()
    return deq


def extendleft_list(el):
    lst.reverse()
    lst.extend(el)
    lst.reverse()
    return lst


def extendleft_deque(el):
    deq.extendleft(el)
    return deq


lst = fill_list(5)
deq = fill_deque(5)
print(lst)
print(deq)
print(appendleft_list('appendleft list'))
print(appendleft_deque('appendleft deque'))
print(popleft_list())
print(popleft_deque())
print(extendleft_list(['extend', 'left', 'list']))
print(extendleft_deque(['extend', 'left', 'deque']))

print('list:  ', timeit('fill_list(1000)', globals=globals(), number=10000))
print('deque: ', timeit('fill_deque(1000)', globals=globals(), number=10000))
print('list:  ', timeit('appendleft_list("appendleft list")', globals=globals(), number=10000))
print('deque: ', timeit('appendleft_deque("appendleft deque")', globals=globals(), number=10000))
print('list:  ', timeit("popleft_list()", globals=globals(), number=10000))
print('deque: ', timeit("popleft_deque()", globals=globals(), number=10000))
print('list:  ', timeit("extendleft_list(['extend', 'left', 'list'])", globals=globals(), number=10000))
print('deque: ', timeit("extendleft_deque(['extend', 'left', 'deque'])", globals=globals(), number=10000))

"""
fill_list(1000):                                  0.079714  seconds
fill_deque(1000):                                 0.1154302 seconds
appendleft_list('appendleft list'):               0.0284342 seconds
appendleft_deque('appendleft deque'):             0.0010768 seconds
pop_left_list(lst):                               0.0075034 seconds
pop_left_deque(deq):                              0.0012217 seconds
extendleft_list(['extend', 'left', 'list']):      0.0939664 seconds
extendleft_deque(['extend', 'left', 'deque']):    0.0022374 seconds

Заполнение Deque происходит медленнее, но методы appendleft(), popleft() и extendleft() работают намного быстрее.
"""
