"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import *
from timeit import timeit

my_deque = deque()
my_list = []
test_list = [i for i in range(25)]


def list_append(any_list):
    for i in any_list:
        my_list.append(i)


def deque_append(any_list):
    for i in any_list:
        my_deque.append(i)


def list_pop(any_list):
    for _ in any_list:
        my_list.pop()


def deque_pop(any_list):
    for _ in any_list:
        my_deque.pop()


def list_insert(any_num):
    for i in range(any_num):
        my_list.insert(0, i)


def deque_append_left(any_num):
    for i in range(any_num):
        my_deque.appendleft(i)


def pop_index_list(any_num):
    for _ in range(any_num):
        my_list.pop(0)


def pop_index_deque(any_num):
    for _ in range(any_num):
        my_deque.popleft()


def list_extend(any_list):
    my_list.extend(any_list)


print('list_append: ', timeit('list_append(test_list)', globals=globals()))
print('deq_append: ', timeit('deque_append(test_list)', globals=globals()))
print('list_pop: ', timeit('list_pop(test_list)', globals=globals()))
print('deq_pop: ', timeit('deque_pop(test_list)', globals=globals()))
print('list_insert: ', timeit('list_insert(25)', globals=globals(), number=10000))
print('deque_append_left: ', timeit('deque_append_left(25)', globals=globals(), number=10000))
print('pop_index_list: ', timeit('pop_index_list(10)', globals=globals(), number=1000))
print('pop_index_deque: ', timeit('pop_index_deque(10)', globals=globals(), number=1000))


"""
list_append:  1.675197
deq_append:  0.9748284
Дек заполняется гораздо быстрее чем список, очевидное преимущество.

list_pop:  0.8363246000000002
deq_pop:  0.8145797000000004
Удаление с конца одинаково по времени.

********************************************
--------------------------------------------
pop_index_list:  0.42228390000000005
pop_index_deque:  0.000539200000000406
--------------------------------------------
list_insert:  9.6164904
deque_append_left:  0.011291199999998724
--------------------------------------------
Вставка в начало и вытаскивание в тысячи раз быстрее в деке, получается, что деку нет равных в случае необходимости 
записи по индексу или вытаскивании элемента (pop возвращает элемент удаляя его).
"""
