from collections import deque
from timeit import timeit

some_list = []
some_deque = deque(some_list)

def list_func_1():
    new_list = []
    for i in range(10000):
        new_list.insert(0, i)
    return new_list

def list_func_2():
    new_list = []
    for i in range(10000):
        new_list.append(0, i)
    return new_list

def list_func_3():
    new_list = []
    for i in range(10000):
        new_list.pop(-1)
    return new_list

def list_func_4():
    new_list = []
    for i in range(10000):
        new_list.pop(0)
    return new_list

def deque_func_1():
    new_deque = deque()
    for i in range(10000):
        new_deque.appendleft(i)
    return new_deque

def deque_func_2():
    new_deque = deque()
    for i in range(10000):
        new_deque.append(i)
    return new_deque

def deque_func_3():
    new_deque = deque()
    for i in range(10000):
        new_deque.pop()
    return new_deque

def deque_func_4():
    new_deque = deque()
    for i in range(10000):
        new_deque.popleft()
    return new_deque


print(timeit("list_func_1", globals=globals(),number=10000))
print(timeit("deque_func_1", globals=globals(),number=10000))
print(timeit("list_func_2", globals=globals(),number=10000))
print(timeit("deque_func_2", globals=globals(),number=10000))
print(timeit("list_func_3", globals=globals(),number=10000))
print(timeit("deque_func_3", globals=globals(),number=10000))
print(timeit("list_func_4", globals=globals(),number=10000))
print(timeit("deque_func_4", globals=globals(),number=10000))

""" Результаты измерений:
---- Добавление элемента в начало ----
0.00013960000000000014
0.00015070000000000014
---- Добавление элемента в конец ----
0.00015070000000000014
0.00013949999999999727
---- Удаление элемента с конца ----
0.00015070000000000014
0.00018309999999999854
---- Удаление элемента с начала ----
0.00013950000000000073
0.00015060000000000073

Процесс додавления элементов в начало дека происходит немного дольше, чем зполнение списка
Процесс додавления элементов в конец происходит быстрее в деке
Удаление элементов с конца происходит быстрее в списке, нежели в деке
Удаление элементов с начала происходит быстрее в списке, нежели в деке
"""