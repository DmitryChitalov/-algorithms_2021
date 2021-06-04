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
from timeit import timeit
from collections import deque
from random import randint

n = 10 ** 4
list1 = []
deque1 = deque()
list2 = [i for i in range(10 ** 5)]
deque2 = deque([i for i in range(10 ** 5)])


def fill_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def fill_deque(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_list(lst):
    for _ in range(90000):
        lst[randint(1, 8001)] = randint(1, 150)
    return lst


def change_deque(dq):
    for _ in range(90000):
        dq[randint(1, 8001)] = randint(1, 150)
    return dq


if __name__ == '__main__':
    print('Время заполнения списка при 10 повторениях: ', timeit(
        'fill_list(list1)',
        setup='from __main__ import fill_list, list1, n',
        number=10
    ))

    print('Время заполнения двусторонней очереди при 10 повторениях: ', timeit(
        'fill_deque(deque1)',
        setup='from __main__ import fill_deque, deque1, n',
        number=10
    ))

    print('-' * 150)
    print('Время изменения списка при 10 повторениях: ', timeit(
        'change_list(list2)',
        setup='from __main__ import change_list, list2',
        number=10
    ))

    print('Время изменения двусторонней очереди при 10 повторениях: ', timeit(
        'change_deque(deque2)',
        setup='from __main__ import change_deque, deque2',
        number=10
    ))
# def f1():
#     list_1 = []
#     for i in range (1, 1000):
#         list_1.append(i**3)
#
#
# def f2():
#     deq_obj = deque()
#     for i in range (1, 1000):
#         deq_obj.append(i**3)
#
# def f3():
#     list_1 = []
#     for i in range(1,1000):
#         list_1.insert(0, i**3)
#
# def f4():
#     deq_obj = deque()
#     for i in range(1, 1000):
#         deq_obj.appendleft(i ** 3)
#
# # print(timeit.timeit(f1, number = 10000))
# # print(timeit.timeit(f2, number = 10000))
# print(timeit.timeit(f3, number = 10000))
# print(timeit.timeit(f4, number = 10000))
