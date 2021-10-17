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
import timeit
from collections import deque

test_list = []
def insert_lst():
    for i in range(1, 100):
        test_list.insert(0, i)
    return test_list

def pop_lst():
    for i in range(1, 100):
        test_list.pop(0)
    return test_list

"""Что-бы сделать аналог extendleft, я должен реверсировать, другого варианта не вижу"""
def extend_lst():
    for i in range(1, 100):
        test_list.extend([i, i])
    test_list.reverse()
    return test_list
#
# print(insert_lst())
# print(pop_lst())
# print(extend_lst())

print('замеры по list')
print(
    timeit.timeit(
        "insert_lst()",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "pop_lst()",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "extend_lst()",
        globals=globals(),
        number=1000))

test_deque = deque()
def appendleft_deque():
    for i in range(1, 100):
        test_deque.appendleft(i)
    return test_deque

def popleft_deque():
    for i in range(1, 100):
        test_deque.popleft()
    return test_deque

def extendleft_deque():
    for i in range(1, 100):
        test_deque.extendleft([i, i])
    return test_deque

# print(appendleft_deque())
# print(popleft_deque())
# print(extendleft_deque())
print('замеры по аналогичным методам deque')

print(
    timeit.timeit(
        "appendleft_deque()",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "popleft_deque()",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "extendleft_deque()",
        globals=globals(),
        number=1000))

test_list_two = []
def append_lst():
    for i in range(1, 100):
        test_list_two.append(i)
    return test_list_two

#print(append_lst())

test_deque_two = deque()
def append_deque():
    for i in range(1, 100):
        test_deque_two.append(i)
    return test_deque_two

#print(append_deque())
print('Сравнение метода append в list и deque')
print(
    timeit.timeit(
        "append_lst()",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "append_deque()",
        globals=globals(),
        number=1000))

"""
Документация не врет
"""
