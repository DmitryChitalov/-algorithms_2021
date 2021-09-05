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

lst_to_test = list(range(10000))
deq_to_test = deque(lst_to_test)


def lst_append(length):
    lst_test = list()
    for i in range(length):
        lst_test.append(i)


def deq_append(length):
    deq_test = deque()
    for i in range(length):
        deq_test.append(i)


def lst_append_left(length):
    lst_test = list()
    for i in range(length):
        lst_test.insert(0, i)


def deq_append_left(length):
    deq_test = deque()
    for i in range(length):
        deq_test.appendleft(i)


def lst_get(lst_arg):
    test = lst_arg[5000]


def deq_get(deq_arg):
    test = deq_arg[5000]


def lst_pop(length, lst_arg):
    for i in range(length):
        lst_arg.pop()


def deq_pop(length, deq_arg):
    for i in range(length):
        deq_arg.pop()


functions = ['lst_append(1000)',
             'deq_append(1000)',
             'lst_append_left(1000)',
             'deq_append_left(1000)',
             'lst_get(lst_to_test)',
             'deq_get(deq_to_test)'
             ]

functions_2 = ['lst_pop(1000, lst_to_test)', 'deq_pop(1000, deq_to_test)']

for item in functions:
    print(f"Функция {item}\t - {timeit(item, globals=globals(), number=10000)} сек")

for item in functions_2:
    print(f"Функция {item}\t -  {timeit(item, globals=globals(), number=1)} сек")

"""
Результаты: добавление элементов (append) примерно одинаковы; добавление в начало списка deque работает 
существенно быстрее чем lst.
По удалению цифры тоже одинаковые.

Функция lst_append(1000)	 - 0.8019821 сек
Функция deq_append(1000)	 - 0.8846677 сек
Функция lst_append_left(1000)	 - 3.1922279 сек
Функция deq_append_left(1000)	 - 0.8146319000000002 сек
Функция lst_get(lst_to_test)	 - 0.0021290000000000475 сек
Функция deq_get(deq_to_test)	 - 0.0025978000000002055 сек
Функция lst_pop(1000, lst_to_test)	 -  5.230000000011614e-05 сек
Функция deq_pop(1000, deq_to_test)	 -  5.780000000044083e-05 сек
"""