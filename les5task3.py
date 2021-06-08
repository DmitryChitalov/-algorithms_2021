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
0.00020660000000000123
0.00019000000000000267
---- Добавление элемента в конец ----
0.00032809999999999784
0.00026570000000000066
---- Удаление элемента с конца ----
0.029880300000000005
0.0226909
---- Удаление элемента с начала ----
0.00026230000000000003
0.00025179999999999647

Любое добавление (как в начало, так и в конец) происходит быстрее в деке, нежели в списке
При добавлении в начало списка сложность функции О(n), а в случае дека - О(1)
При добавлении в конец списка сложность ка и в деке О(1). Но поиграв с количеством элементов
можно заметитть, что дек раюотает быстрее, если элементов много.
При удалении элементов как с начала так и с конца можно заметить, что список опять работает 
медленнее. И там и там сложность будет О(1)
"""