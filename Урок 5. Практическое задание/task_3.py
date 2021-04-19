from collections import deque
from timeit import timeit
from random import randint as rd


def pop_list(ls):
    ls.pop(0)
def pop_deque(deq):
    deq.popleft()

def pop_list_1(ls):
    ls.pop()
def pop_deque_1(deq):
    deq.pop()


def count_list(ls):
    ls.count(5)
def count_deque(deq):
    deq.count(5)

def reverse_list(ls):
    ls.reverse()
def reverse_deque(deq):
    deq.reverse()


def extend_list(ls):
    ls.extend([4, 43, 5, 2])


def extend_deque(deq):
    deq.extend([4, 43, 5, 2])


def extend_deque_1(deq):
    deq.extendleft([4, 43, 5, 2])


def append_list(ls):
    ls.append(6)


def append_deque(deq):
    deq.append(3)


def insert_list(ls):
    ls.insert(0, 6)


def append_left_deque(deq):
    deq.appendleft(8)


def insert_list_mid(ls):
    ls.insert(len(ls) // 2, 7)


def insert_deque_mid(deq):
    deq.insert(len(deq) // 2, 7)


data_list = [i for i in range(100000)]
data_deque = deque([el for el in range(100000)])
print(f'Удаление pop')
print(f'list: {timeit("pop_list(data_list)", globals=globals(), number=100000)}')
print(f'deque: {timeit("pop_deque(data_deque)", globals=globals(), number=100000)}')

data_list_1 = [rd(0, 100) for i in range(100000)]
data_deque_1 = deque([rd(0, 100) for el in range(100000)])
print(f'list: {timeit("pop_list_1(data_list_1)", globals=globals(), number=100000)}')
print(f'deque: {timeit("pop_deque_1(data_deque_1)", globals=globals(), number=100000)}')

print(f'Count  ')
print(f'list: {timeit("count_list(data_list)", globals=globals(), number=100000)}')
print(f'deque: {timeit("count_deque(data_deque)", globals=globals(), number=100000)}')
print(f' Reverse  ')

data_list_2 = [rd(0, 100) for i in range(100000)]
data_deque_2 = deque([rd(0, 100) for el in range(100000)])
print(f'list: {timeit("reverse_list(data_list_2)", globals=globals(), number=10000)}')
print(f'deque: {timeit("reverse_deque(data_deque_2)", globals=globals(), number=10000)}')
print(f' Extend  ')
data_list_3 = [rd(0, 100) for i in range(100000)]
data_deque_3 = deque([rd(0, 100) for el in range(100000)])

print(f'list: {timeit("extend_list(data_list_3)", globals=globals(), number=10000)}')
print(f'deque: {timeit("extend_deque(data_deque_3)", globals=globals(), number=10000)}')
print(f'deque_2: {timeit("extend_deque_1(data_deque_3)", globals=globals(), number=10000)}')

print(f' Append ')
print(f'list: {timeit("append_list(data_list)", globals=globals(), number=10000)}')
print(f'deque: {timeit("append_deque(data_deque)", globals=globals(), number=10000)}')

print(f'insert')

print(f'list: {timeit("insert_list(data_list)", globals=globals(), number=10000)}')
print(f'deque: {timeit("append_left_deque(data_deque)", globals=globals(), number=10000)}')

print(f' insert mid')

print(f'list: {timeit("insert_list_mid(data_list)", globals=globals(), number=10000)}')
print(f'deque: {timeit("insert_deque_mid(data_deque)", globals=globals(), number=10000)}')


#deque быстрее работает на удаление и вставку с НАЧАЛО
#Список быстрее в операциях Reverse и вставка в СЕРЕДИНУ