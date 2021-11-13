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
# import time


# def timeitt(f):
#     def wrap(*args):
#         time_start = time.time()
#         ret = f(*args)
#         time_end = time.time()
#         print('%s  %0.3f ms' % (f.__name__, (time_end-time_start)*1000.0))
#         return ret
#     return wrap


experimental_list = []
experimental_deque = deque([])


def fill_list():
    experimental_list = [el for el in range(10001)]
    return experimental_list

print(f"{fill_list.__name__} {timeit('fill_list()', globals=globals(), number=1000)}")


def fill_deque():
    experimental_deque = deque([el for el in range(10001)])
    return experimental_deque

print(f"{fill_deque.__name__} {timeit('fill_deque()', globals=globals(), number=1000)}")


def add_elms_list(some_lst, how_much_add = 0):
    for el in range(how_much_add):
        some_lst.append(el)
    return some_lst

print(f"{add_elms_list.__name__} {timeit('add_elms_list(experimental_list, 1000)', globals=globals(), number=1000)}")


def add_1_elm_list(some_lst, elm = 0):
    some_lst.append(elm)
    return some_lst

print(f"{add_1_elm_list.__name__} {timeit('add_1_elm_list(experimental_list, 777)', globals=globals(), number=1000)}")


def add_elms_deque(some_deque, how_much_add = 0):
    for el in range(how_much_add):
        some_deque.append(el)
    return some_deque

print(f"{add_elms_deque.__name__} {timeit('add_elms_deque(experimental_deque, 1000)', globals=globals(), number=1000)}")


def add_1_elm_deq(some_deque, elm = 0):
    some_deque.append(elm)
    return some_deque

print(f"{add_1_elm_deq.__name__} {timeit('add_1_elm_deq(experimental_deque, 777)', globals=globals(), number=1000)}")


def insert_at_beginning_of_list(where_to_insert = [], how_much_put = 0):
    for el in range(how_much_put, -1, -1):
        where_to_insert.insert(0, el)
    return where_to_insert

print(f"{insert_at_beginning_of_list.__name__} \
{timeit('insert_at_beginning_of_list(experimental_list, 100)', globals=globals(), number=1000)}")


def insert_1_elm_at_beginning_lst(where_to_insert, el = 0):
    where_to_insert.insert(0, el)
    return where_to_insert

print(f"{insert_1_elm_at_beginning_lst.__name__} \
{timeit('insert_1_elm_at_beginning_lst(experimental_list, 999)', globals=globals(), number=1000)}")


def insert_at_beginning_of_deque(where_to_insert = [], how_much_put = 0):
    for el in range(how_much_put, -1, -1):
        where_to_insert.appendleft(el)
    return where_to_insert

print(f"{insert_at_beginning_of_deque.__name__} \
{timeit('insert_at_beginning_of_deque(experimental_deque, 100)', globals=globals(), number=1000)}")


def insert_1_elm_at_beginning_deq(where_to_insert, el = 0):
    where_to_insert.appendleft(el)
    return where_to_insert

print(f"{insert_1_elm_at_beginning_deq.__name__} \
{timeit('insert_1_elm_at_beginning_deq(experimental_deque, 999)', globals=globals(), number=1000)}")


def pop_list(some_lst):
    some_lst.pop()
    return some_lst

print(f"{pop_list.__name__} \
{timeit('pop_list(experimental_list)', globals=globals(), number=1000)}")


def pop_deque(some_deque):
    some_deque.pop()
    return some_deque

print(f"{pop_deque.__name__} \
{timeit('pop_deque(experimental_deque)', globals=globals(), number=1000)}")


def pop_at_beginning_list(some_lst):
    some_lst.pop(0)
    return some_lst

print(f"{pop_at_beginning_list.__name__} \
{timeit('pop_at_beginning_list(experimental_list)', globals=globals(), number=1000)}")


def pop_at_beginning_deque(some_deque):
    some_deque.popleft()
    return some_deque

print(f"{pop_at_beginning_deque.__name__} \
{timeit('pop_at_beginning_deque(experimental_deque)', globals=globals(), number=1000)}")



def extend_list(some_lst, some_lst_2 = []):
    some_lst.extend(some_lst_2)
    return some_lst

print(f"{extend_list.__name__} \
{timeit('extend_list(experimental_list, [0,0,0,0,0])', globals=globals(), number=1000)}")


def extend_deque(some_deque, some_lst = []):
    some_deque.extend(some_lst)
    return some_deque

print(f"{extend_deque.__name__} \
{timeit('extend_deque(experimental_deque, [0,0,0,0,0])', globals=globals(), number=1000)}")


def extend_at_beginning_list(some_lst, some_lst_2 = []):
    for el in some_lst_2[::-1]:
        some_lst.insert(0, el)
    return some_lst

print(f"{extend_at_beginning_list.__name__} \
{timeit('extend_at_beginning_list(experimental_list, [1,1,1,1,1])', globals=globals(), number=1000)}")


def extend_1_elm_at_beginning_list(some_lst, some_lst_2 = []):
    some_lst.insert(0, some_lst_2)
    return some_lst

print(f"{extend_1_elm_at_beginning_list.__name__} \
{timeit('extend_1_elm_at_beginning_list(experimental_list, [5,5,5,5,5])', globals=globals(), number=1000)}")


def extend_at_beginning_deque(some_deque, some_lst = []):
    for el in some_lst[::-1]:
        some_deque.appendleft(el)
    return some_deque

print(f"{extend_at_beginning_deque.__name__} \
{timeit('extend_at_beginning_deque(experimental_deque, [1,1,1,1,1])', globals=globals(), number=1000)}")


def extend_1_elm_at_beginning_deq(some_deq, some_lst_2 = []):
    some_deq.appendleft(some_lst_2)
    return some_deq

print(f"{extend_1_elm_at_beginning_deq.__name__} \
{timeit('extend_1_elm_at_beginning_deq(experimental_deque, [5,5,5,5,5])', globals=globals(), number=1000)}")


# '''
#             заполнение
# fill_list 0.3158542929995747                            lst
# fill_deque 0.35795707199940807
#         добавление очереди и 1 элемента в конец
# add_elms_list 0.05734958299944992                       deq
# add_1_elm_list 0.00011644700134638697
# add_elms_deque 0.04863877699972363
# add_1_elm_deq 0.00011709899990819395
#         добавление очереди и 1 элемента в начало
# insert_at_beginning_of_list 102.76500970599955          deq
# insert_1_elm_at_beginning_lst 1.231384935999813
# insert_at_beginning_of_deque 0.004130698998778826
# insert_1_elm_at_beginning_deq 0.0001146850008808542
#         удаление элемента в конце и начале
# pop_list 0.0001007290011330042                          deq
# pop_deque 0.00010326399933546782
# pop_at_beginning_list 1.035745435001445
# pop_at_beginning_deque 0.00015522100147791207
#         добавляем список к списку в конец
# extend_list 0.0001652389983064495                       lst
# extend_deque 0.00023492899708799087
#         добавим очередь из другого списка и список целиком
# extend_at_beginning_list 6.147759742001654              deq
# extend_1_elm_at_beginning_list 1.2252583490007964
# extend_at_beginning_deque 0.000473916999908397
# extend_1_elm_at_beginning_deq 0.0002042720007011667

# deque рулит! особенно по вставке нескольких элемнтов в начало писка,
# да и по всавке одного элемента. Там где список был и быстрее, 
# то совсем незначительно.
# '''