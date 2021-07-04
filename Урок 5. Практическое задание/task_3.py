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

my_list = []
for i in range(1000):
    my_list.append(i)

my_deque = deque()
for i in range(1000):
    my_deque.append(i)

def create_list():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    return

def create_deque():
    my_deque = deque()
    for i in range(1000):
        my_deque.append(i)
    return

def left_insert_list(my_list):
    for i in range(1000):
        my_list.insert(0,i)
    return my_list

def appendleft_deque(my_deque):
    for i in range(1000):
        my_deque.appendleft(i)
    return my_deque

def popleft_list(my_list):
    for i in range(1000):
        my_list.pop(0)
    return my_list

def popleft_deque(my_deque):
    for i in range(1000):
        my_deque.popleft()
    return my_deque


def extendleft_deque(my_deque,my_list):
    my_deque.extendleft(my_list)
    return my_deque


def extendright_list(my_list,my_deque):
    my_list.extend(my_deque)
    return my_list

def extendright_deque(my_deque,my_list):
    my_deque.extend(my_list)
    return my_deque

print(f'Создание списка {timeit("create_list",globals=globals(),number = 1000000)} sec')
print(f'Создание deque {timeit("create_deque",globals=globals(),number = 1000000)} sec')
print(f'Добавление слева в список {timeit("left_insert_list(my_list)",globals=globals(),number = 100)} sec')
print(f'Добавление слева в deque {timeit("appendleft_deque(my_deque)",globals=globals(),number = 100)} sec')
print(f'Удаление слева из списка {timeit("popleft_list(my_list)",globals=globals(),number = 100)} sec')
print(f'Удаление слева из deque {timeit("popleft_deque(my_deque)",globals=globals(),number = 100)} sec')
print(f'Добавление слева списка в deque {timeit("extendleft_deque(my_deque,my_list)",globals=globals(),number = 100)} sec')
print(f'Добавление справа deque в список {timeit("extendright_list(my_list,my_deque)",globals=globals(),number = 100)} sec')
print(f'Добавление справа списка в deque {timeit("extendright_deque(my_deque,my_list)",globals=globals(),number = 10)} sec')


"""
1 замер
Создание списка 0.217665 sec
Создание deque 0.12409809999999993 sec
Добавление слева в список 4.7861818 sec
Добавление слева в deque 0.008358600000000216 sec
Удаление слева из списка 4.5375366 sec
Удаление слева из deque 0.03446450000000034 sec
Добавление слева списка в deque 0.01383060000000036 sec
Добавление справа deque в список 4.8862442 sec
Добавление справа списка в deque 14.059666600000002 sec

2 замер
Создание списка 0.0785769 sec
Создание deque 0.06461510000000001 sec
Добавление слева в список 8.9862433 sec
Добавление слева в deque 0.022098100000000898 sec
Удаление слева из списка 4.4778018 sec
Удаление слева из deque 0.027061599999999686 sec
Добавление слева списка в deque 0.003662400000001398 sec
Добавление справа deque в список 1.4016845 sec
Добавление справа списка в deque 3.9187553999999984 sec

3 замер
Создание списка 0.1778321 sec
Создание deque 0.1003559 sec
Добавление слева в список 9.6519099 sec
Добавление слева в deque 0.04429159999999932 sec
Удаление слева из списка 4.4336231 sec
Удаление слева из deque 0.03107889999999891 sec
Добавление слева списка в deque 0.0034326999999994 sec
Добавление справа deque в список 1.3722876000000017 sec
Добавление справа списка в deque 3.884055199999999 sec

4 замер
Создание списка 0.27362269999999994 sec
Создание deque 0.14021260000000002 sec
Добавление слева в список 8.765808700000001 sec
Добавление слева в deque 0.03062930000000108 sec
Удаление слева из списка 4.4007244 sec
Удаление слева из deque 0.028229699999998914 sec
Добавление слева списка в deque 0.0030149000000001536 sec
Добавление справа deque в список 1.7543828999999995 sec
Добавление справа списка в deque 3.8325500000000012 sec

5 замер
Создание списка 0.2611268 sec
Создание deque 0.11381550000000001 sec
Добавление слева в список 9.418398700000001 sec
Добавление слева в deque 0.037373900000000404 sec
Удаление слева из списка 7.805323900000001 sec
Удаление слева из deque 0.015418300000000329 sec
Добавление слева списка в deque 0.001820199999997385 sec
Добавление справа deque в список 1.5554267999999993 sec
Добавление справа списка в deque 2.698125300000001 sec

Замеры показали, что создание и операции по работе с добавлением (как 1 элемента, так и списка) и удалением
элементов слева выполеняются в разы быстрее при работе с deque. 

Производя замеры по добавлению справа списка в deque при количестве повтор выполенения кода равным 100, 
время выполнения кода было непозволительно большим и еще наблюдалось аномальное заполнение дискогово 
пространства какими-то данными. За считанные секунды заполнялось до 9 гигабайт. Только снизив количество 
повторов до 10, смог получить какое-то вменяемое время выполнения оперции.

"""