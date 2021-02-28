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
from random import randint
from collections import deque


# list insert in middle - dq insert in middle
def list_insert(lst, elem):
    lst.insert(len(lst) // 2, elem)


def deque_insert(dq, elem):
    dq.insert(len(dq) // 2, elem)


# list insert - deque append_left
def list_insert_into_start(lst, elem):
    lst.insert(0, elem)


def deque_insert_into_start(dq, elem):
    dq.appendleft(elem)


# list append - deque append
def list_append(lst, elem):
    lst.append(elem)


def deque_append(dq, elem):
    dq.append(elem)


# list - pop(0) - deque popleft
def list_pop_from_start(lst):
    lst.pop(0)


def deque_pop_from_start(dq):
    dq.popleft()


# list - pop() - deque pop
def list_pop_from_end(lst):
    lst.pop()


def deque_pop_from_end(dq):
    dq.pop()


# extend, extend


def list_extend(lst, ext_lst):
    lst.extend(ext_lst)


def deque_extend(dq, ext_lst):
    dq.extend(ext_lst)


# extend left

def list_extend_left(lst, ext_lst):
    ext_lst.extend(lst)


def deque_extend_left(dq, ext_lst):
    dq.extendleft(ext_lst)


my_lst = [randint(0, 100) for i in range(100)]
my_dq = deque(my_lst)
element = 10
extend_lst = [randint(0, 100) for i in range(10)]

print("Вставка в середину:")
print(f"List: {timeit('list_insert(my_lst, element)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_insert(my_dq, element)', globals=globals(), number=100000)}")

print("Вставка в начало:")
print(f"List: {timeit('list_insert_into_start(my_lst, element)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_insert_into_start(my_dq, element)', globals=globals(), number=100000)}")

print("Вставка в конец:")
print(f"List: {timeit('list_append(my_lst, element)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_append(my_dq, element)', globals=globals(), number=100000)}")

print("Удаление с головы: ")
print(f"List: {timeit('list_pop_from_start(my_lst)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_pop_from_start(my_dq)', globals=globals(), number=100000)}")

print("Удаление с схвоста: ")
print(f"List: {timeit('list_pop_from_end(my_lst)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_pop_from_end(my_dq)', globals=globals(), number=100000)}")

print("Расширение: ")
print(f"List: {timeit('list_extend(my_lst, extend_lst)', globals=globals(), number=100000)}")
print(f"Deque: {timeit('deque_extend(my_dq, extend_lst)', globals=globals(), number=100000)}")

print("Расширение с начала: ")
print(f"List: {timeit('list_extend_left(my_lst, extend_lst)', globals=globals(), number=10)}")
print(f"Deque: {timeit('deque_extend_left(my_dq, extend_lst)', globals=globals(), number=10)}")
"""
Вставка в середину:
List: 1.0082881
Deque: 3.8739946

Вставка в начало:
List: 6.1400277999999995
Deque: 0.011353800000000192

Вставка в конец:
List: 0.012458099999999916
Deque: 0.01294919999999955

Удаление с головы: 
List: 22.519617600000004
Deque: 0.009743799999995417

Удаление с схвоста: 
List: 0.010173000000001764
Deque: 0.010135399999995798

Расширение: 
List: 0.02537230000000079
Deque: 0.026473000000002855

Расширение с начала: 
List: 0.08777660000000509
Deque: 1.2677875999999983

Вывод:
Операции добавления и удаления в конец отрабатываею одинаково быстро для списка и дэки.
Операции добавления элементов в начало для списка выполняются значительно медленнее, чем для дэки. 
Вставака в середину выполняется быстрее для списка.
расширение списка работает одинаково быстро в обе стороны. А расширение дэки слева
выполняется значительно медленнее. 
"""
