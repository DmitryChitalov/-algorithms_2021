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
print('pop_index_list: ', timeit('pop_index_list(10)', globals=globals(), number=10000))
print('pop_index_deque: ', timeit('pop_index_deque(10)', globals=globals(), number=10000))


# list_append:  1.9280297
# deq_append:  1.6044415
# list_pop:  1.3915056999999997
# deq_pop:  1.3622752
# Эти операции примерно одинаковы по затратам времени.
# list_insert:  16.9736148
# deque_append_left:  0.016698000000001656
# pop_index_list:  7.597794499999999
# pop_index_deque:  0.007629800000000131
# Вставка  слева и вытаскивание - дают разницу в тысячу раз в пользу дека, что более чем существенно.
