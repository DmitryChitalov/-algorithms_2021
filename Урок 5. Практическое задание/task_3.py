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

from timeit import timeit

from collections import deque

list_object = [1, 2, 3]

deque_object = deque(list_object)


def fill_list():
    list_object = [x for x in range(10000)]

    return list_object


def fill_deque():
    deque_object = [x for x in range(10000)]

    return deque_object


def list_in():
    list_object.insert(0, 12)

    return list_object


def deque_al():
    deque_object.appendleft(12)

    return deque_object


def list_pop():
    list_object.pop(0)

    return list_object


def deque_pop():
    deque_object.popleft()

    return deque_object


def list_ex():
    a = [1, 2, 3]

    for i in range(len(a)):
        list_object.insert(0, a[i])

    return list_object


def deque_ex():
    deque_object.extendleft([1, 2, 3])

    return deque_object


print(

    timeit(

        "fill_list()",

        setup="from __main__ import fill_list", number=10000))

print(

    timeit(

        "fill_deque()",

        setup="from __main__ import fill_deque", number=10000))

print(

    timeit(

        "list_in()",

        setup="from __main__ import list_in", number=10000))

print(

    timeit(

        "deque_al()",

        setup="from __main__ import deque_al", number=10000))

print(

    timeit(

        "list_pop()",

        setup="from __main__ import list_pop", number=10000))

print(

    timeit(

        "deque_pop()",

        setup="from __main__ import deque_pop", number=10000))

print(

    timeit(

        "list_ex()",

        setup="from __main__ import list_ex", number=10000))

print(

    timeit(

        "deque_ex()",

        setup="from __main__ import deque_ex", number=10000))

'''

Заполнение 10 000 повторений:

LIST - 3.588361864000035

DEQUE - 3.498583904000043



Добавление элемента в начало 10 000 повторов:

list_in - 0.018863858999793592

deque_al - 0.0008656929999233398

LIST дольше вставляет элемент в начало списка



Удаление элемент из начала 10 000 повторов:

list_pop - 0.0095296779995806

deque_pop - 0.0008654559997012257

LIST дольше удаляет элемент из начала списка



Добавление списка элементов в начало 10 000 повторов:

list_ex - 0.17280757199978325

deque_ex - 0.0015425530000356957

LIST дольше добавляет список элементов в начало
'''
