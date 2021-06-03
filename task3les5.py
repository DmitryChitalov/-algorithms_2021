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


print(timeit("list_func_1", globals=globals(),number=1000))
print(timeit("deque_func_1", globals=globals(),number=1000))
print(timeit("list_func_2", globals=globals(),number=1000))
print(timeit("deque_func_2", globals=globals(),number=1000))
print(timeit("list_func_3", globals=globals(),number=1000))
print(timeit("deque_func_3", globals=globals(),number=1000))
print(timeit("list_func_4", globals=globals(),number=1000))
print(timeit("deque_func_4", globals=globals(),number=1000))

""" Результаты измерений:
---- Вставление элемента в начало ----
6.349999999999412e-05
6.290000000000462e-05
---- Вставление элемента в конец ----
6.349999999999412e-05
6.270000000001275e-05
---- Удаление элемента с конца ----
6.799999999999862e-05
6.779999999999287e-05
---- Удаление элемента с начала ----
6.810000000000149e-05
6.789999999999574e-05

Процесс заполнения списка происходит немного дольше, чем зполнение дека
Процесс удаления элементов тоже быстрее происходит в деке, нежели в списке
"""