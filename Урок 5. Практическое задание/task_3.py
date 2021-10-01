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

import time
from collections import deque

my_list = []
my_deque = deque()


def check_time(fn):
    def wrapper(*args):
        start_val = time.time()
        fn(*args)
        end_val = time.time()
        print(f'{fn.__name__}, Операция заняла {end_val - start_val} сек')

    return wrapper


@check_time
def filling_list_append(n):
    for i in range(n):
        my_list.append(i)


@check_time
def filling_list_insert(n):
    for i in range(n):
        my_list.insert(0, i)


@check_time
def filling_deque_append(n):
    for i in range(n):
        my_deque.append(i)


@check_time
def filling_deque_append_left(n):
    for i in range(n):
        my_deque.appendleft(i)


filling_list_append(100000)
filling_list_insert(100000)
filling_deque_append(100000)
filling_deque_append_left(100000)

"""
filling_list_append, Операция заняла 0.012975454330444336 сек
filling_list_insert, Операция заняла 12.504160404205322 сек
filling_deque_append, Операция заняла 0.009981155395507812 сек
filling_deque_append_left, Операция заняла 0.011977195739746094 сек

Заполнение списка и дека с конаца выполняется с одинаковой скоростью и сложностью - О(1), 
Но при добавлении элементов в начало, дек быстрее т.к. сложность операции вставки в начало - О(1), 
а для списка - О(n).
"""


@check_time
def change_list(n):
    for i in range(n):
        my_list[i] = 'new_data'


@check_time
def change_deque(n):
    for i in range(n):
        my_deque[i] = 'new_data'


change_list(200000)
change_deque(200000)

"""
change_list, Операция заняла 0.020459413528442383 сек
change_deque, Операция заняла 0.8024697303771973 сек
При доступе к элементу по индексу и изменении элемента, 
обычный список работает быстрее, чем дек.
"""


@check_time
def list_pop_begin(n):
    for i in range(n):
        my_list.pop(0)


@check_time
def deque_popleft(n):
    for i in range(n):
        my_deque.pop()


list_pop_begin(100000)
deque_popleft(100000)

"""
list_pop_begin, Операция заняла 8.515764951705933 сек
deque_popleft, Операция заняла 0.013972282409667969 сек
Удаление элемента с начала списка быстрее выполняется в деке (сложность - О(1)),
чем  в обычном списке (сложность - О(n))
"""


@check_time
def list_extend_left(n):
    for i in range(n):
        a = [1, 2, 3]
        for j in range(len(a)):
            my_list.insert(0, a[j])


@check_time
def deque_extend_left(n):
    for i in range(n):
        my_deque.extendleft([1, 2, 3])


list_extend_left(100000)
deque_extend_left(100000)

'''
list_extend_left, Операция заняла 68.17402052879333 сек
deque_extend_left, Операция заняла 0.026447534561157227 сек
При добавлении списка элементов в начало сложность при использовании обычного списка О(n^2),
тогда как при использвании дека сложность всего О(1)'''
