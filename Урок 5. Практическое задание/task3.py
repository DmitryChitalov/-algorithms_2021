import random
from collections import deque
import timeit

# пункт a
def fill_list(n):
    l = []
    for i in range(n):
        l.append(random.randint(-100, 100))
    return l


def fill_deque(n):
    dq = deque()
    for i in range(n):
        dq.append(random.randint(-100, 100))
    return dq


print("Наполнение списка: ")
print(timeit.timeit('fill_list(100)', setup='from __main__ import fill_list', number=10000))
print("Наполнение Deque: ")
print(timeit.timeit('fill_deque(100)', setup='from __main__ import fill_deque', number=10000))
print("Наполнение списка происходит немного дольше")

# пункт b
def append_left_list(l, item):
    return l.insert(0, item)

def append_left_list2(l, item):
    return [item] + l

def append_left_dq(dq, item):
    return dq.appendleft(item)


l = fill_list(5)
dq = fill_deque(5)
print("Добавление элемента в начало списка: ")
print(timeit.timeit(f'append_left_list({l},100)', globals = globals(), number=10000))
print("Добавление элемента в начало Deque: ")
print(timeit.timeit(f'append_left_dq({dq}, 100)', globals = globals(), number=10000))
print("Добавление элемента в начало списка (второй вариант): ")
print(timeit.timeit(f'append_left_list2({l},100)', globals = globals(), number=10000))

print("Добавление элемента в начало списка быстрее работает для списков")

def pop_left_list(l):
    l0 = l[0]
    l[:] = l[1:]
    return l0

def pop_left_dq(dq):
    return dq.popleft()


print("удаление первого элемента списка: ")
print(timeit.timeit(f'pop_left_list({l})', globals = globals(), number=10000))
print("удаление первого элемента Deque: ")
print(timeit.timeit(f'pop_left_dq({dq})', globals = globals(), number=10000))


print("Удаление первого лемента также быстрее у списков")
def extend_left_list(l,items):
    for i in range(len(items)):
        l.insert(0, items[i])
    l[:] = l
    return l

def extend_left_dq(dq, items):
    dq.extendleft(items)
    return dq

s = 'itemsitemsitems'
print("Расширение списка слева: ")
print(timeit.timeit(f'extend_left_list({l},s)', globals = globals(), number=10000))
print("Расширение Deque слева: ")
print(timeit.timeit(f'extend_left_dq({dq},s)', globals = globals(), number=10000))

print("Расширение списка слева работает значительно медленнее, чем DQ")
