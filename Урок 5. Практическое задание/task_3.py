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

list_to_test = list(range(10000))
deque_to_test = deque(list_to_test)


def list_append(length):
    list_test = list()
    for i in range(length):
        list_test.append(i)


def deque_append(length):
    deque_test = deque()
    for i in range(length):
        deque_test.append(i)


def list_append_left(length):
    list_test = list()
    for i in range(length):
        list_test.insert(0, i)


def deque_append_left(length):
    deque_test = deque()
    for i in range(length):
        deque_test.appendleft(i)


def list_get(list_arg):
    test = list_arg[5000]


def deque_get(deque_arg):
    test = deque_arg[5000]


def list_pop(length, list_arg):
    for i in range(length):
        list_arg.pop()


def deque_pop(length, deque_arg):
    for i in range(length):
        deque_arg.pop()


functions = ['list_append(1000)',
             'deque_append(1000)',
             'list_append_left(1000)',
             'deque_append_left(1000)',
             'list_get(list_to_test)',
             'deque_get(deque_to_test)'
             ]

functions_2 = ['list_pop(10000, list_to_test)', 'deque_pop(10000, deque_to_test)']

for item in functions:
    print(f"Функция {item}\t ---> {timeit(item, globals=globals(), number=10000)}")

for item in functions_2:
    print(f"Функция {item}\t ---> {timeit(item, globals=globals(), number=1)}")

'''
Результаты показывают что добавление элементов быстрее в deque, причем в начало списка существенно быстрее.
По удалению особой разницы нет.
По считыванию элемета бысрее list.


Функция list_append(1000)	 ---> 0.6276845
Функция deque_append(1000)	 ---> 0.5855786

Функция list_append_left(1000)	 ---> 2.1083544
Функция deque_append_left(1000)	 ---> 0.6175461000000002

Функция list_get(list_to_test)	 ---> 0.0009487999999997498
Функция deque_get(deque_to_test)	 ---> 0.0017484000000003164

Функция list_pop(10000, list_to_test)	 ---> 0.0005154000000002767
Функция deque_pop(10000, deque_to_test)	 ---> 0.0005245999999998752
'''
