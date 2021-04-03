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

from collections import deque
from timeit import timeit
from random import randint


def iteration_list(amount):
    global my_list
    my_list = [randint(1,100000) for el in range(amount)]

def iteration_deque(amount):
    global my_deque
    my_deque = deque(randint(1,100000) for el in range(amount))

def read_rnd_list(amount):
    global my_list
    for i in range(amount):
        el = my_list[randint(0, amount-1)]

def read_rnd_deque(amount):
    global my_deque
    for i in range(amount):
        el = my_deque[randint(0, amount-1)]

def append_begin_list(amount):
    global my_list
    for i in range(amount):
        my_list.insert(0, randint(1,100000))

def append_begin_deque(amount):
    global my_deque
    for i in range(amount):
        my_deque.appendleft(randint(1,100000))

def append_end_list(amount):
    global my_list
    for i in range(amount):
        my_list.append(randint(1,100000))

def append_end_deque(amount):
    global my_deque
    for i in range(amount):
        my_deque.append(randint(1,100000))

def pop_begin_list(amount):
    global my_list
    for i in range(amount):
        el = my_list.pop(0)

def pop_begin_deque(amount):
    global my_deque
    for i in range(amount):
        el = my_deque.popleft()

def pop_end_list(amount):
    global my_list
    for i in range(amount):
        el = my_list.pop(len(my_list)-1)

def pop_end_deque(amount):
    global my_deque
    for i in range(amount):
        el = my_deque.pop()


param = 100
my_list = []
my_deque = deque()

func_list = ['iteration_list', 'iteration_deque',
             'read_rnd_list', 'read_rnd_deque',
             'append_begin_list', 'append_begin_deque',
             'append_end_list', 'append_end_deque',
             'pop_begin_list', 'pop_begin_deque',
             'pop_end_list', 'pop_end_deque'
             ]
max_len = len(max(func_list, key=len))
print('Сделаем замеры скорости выполнения операций с простым списком (list) и очередью/стеком (deque)')
for el in func_list:
    print(f'Функция {el}:'.ljust(max_len+10,'_'), timeit(el+'(param)', number=1000, globals=globals()))

'''
Сделаем замеры скорости выполнения операций с простым списком (list) и очередью/стеком (deque)
Функция iteration_list:_____ 0.19090634700000003
Функция iteration_deque:____ 0.16528509000000002
Функция read_rnd_list:______ 0.14810604299999997
Функция read_rnd_deque:_____ 0.152819504
Функция append_begin_list:__ 5.089552139
Функция append_begin_deque:_ 0.16920039599999992
Функция append_end_list:____ 0.1707864429999999
Функция append_end_deque:___ 0.1695535890000004
Функция pop_begin_list:_____ 10.075134636
Функция pop_begin_deque:____ 0.011827423999999809
Функция pop_end_list:_______ 0.030105293999998395
Функция pop_end_deque:______ 0.011383670000000734

Вывод:
    deque имеет существенный выигрыш по:
    - append_begin в 30 раз
    - pop_begin в 900 раз
    - pop_end в 3 раза

Примечание:
    Извлечение pop(i) по произвольной позиции в deque не реализовано - следует использовать list.

'''