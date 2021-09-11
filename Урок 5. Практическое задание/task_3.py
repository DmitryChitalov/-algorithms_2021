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


def pull_list():
    xperimnt_list = list(range(10000))
    return xperimnt_list

def popleft_list(xperimnt_list):
    xperimnt_list.pop(0)
    return xperimnt_list

def appendleft_list(xperimnt_list):
    xperimnt_list.insert(0, 10)
    return xperimnt_list

def extendleft_list(xperimnt_list):
    new_lst = [1, 2, 3, 4, 5]
    for i, num in enumerate(new_lst):
        xperimnt_list.insert(i, num)
    return xperimnt_list

def append_list(xperimnt_list):
    xperimnt_list.append(1)
    return xperimnt_list

def pull_deque():
    xperimnt_deque = deque(range(10000))
    return xperimnt_deque

def popleft_deque(xperimnt_deque):
    xperimnt_deque.popleft()
    return xperimnt_deque

def appendleft_deque(xperimnt_deque):
    xperimnt_deque.appendleft(10)
    return xperimnt_deque

def extendleft_deque(xperimnt_deque):
    new_lst = [1, 2, 3, 4, 5]
    xperimnt_deque.extendleft(new_lst)
    return xperimnt_deque

def append_deque(xperimnt_deque):
    xperimnt_deque.append(1)
    return xperimnt_deque


xperimnt_list = pull_list()
xperimnt_deque = pull_deque()



print(timeit("pull_list()", globals=globals(),number=10000))
print(timeit("pull_deque()", globals=globals(),number=10000))
print('-' * 30)
print(timeit("popleft_list(xperimnt_list)", globals=globals(),number=10000))
print(timeit("popleft_deque(xperimnt_deque)", globals=globals(),number=10000))
print('-' * 30)
print(timeit("appendleft_list(xperimnt_list)", globals=globals(),number=10000))
print(timeit("appendleft_deque(xperimnt_deque)", globals=globals(),number=10000))
print('-' * 30)
print(timeit("extendleft_list(xperimnt_list)", globals=globals(),number=10000))
print(timeit("extendleft_deque(xperimnt_deque)", globals=globals(),number=10000))
print('-' * 30)
print(timeit("append_list(xperimnt_list)", globals=globals(),number=10000))
print(timeit("append_deque(xperimnt_deque)", globals=globals(),number=10000))
"""
Мы можем видеть, что список заполняется быстрее цем дека, однако все действия связанные с левой частью
в деке соверщаются в разы быстрее. И в обычном действии типо append у деки все равно сохраняется небольшое 
преимущество перед списком.
"""

