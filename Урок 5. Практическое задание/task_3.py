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
from timeit import Timer


def fill_lst(n):
    return list(range(n))


def fill_deq(n):
    return deque(list(range(n)))


def insert_to_start_lst(in_lst, n):
    for i in range(n):
        in_lst.insert(0, i)

    return in_lst


def insert_to_end_lst(in_lst, n):
    for i in range(n):
        in_lst.append(i)

    return in_lst


def insert_to_start_deq(in_deq, n):
    for i in range(n):
        in_deq.appendleft(i)

    return in_deq


def insert_to_end_deq(in_deq, n):
    for i in range(n):
        in_deq.append(i)

    return in_deq


def get_count_lst(in_lst, n):
    return in_lst.count(n)


def get_count_deq(in_deq, n):
    return in_deq.count(n)


el_count = 100000
lst = []
deq = deque([])

print('# Заполнение lst')
t1 = Timer("fill_lst(el_count)", "from __main__ import fill_lst, el_count")
print('t1', t1.timeit(number=10))
lst = list(range(el_count))

print('# Заполнение deq')
t2 = Timer("fill_deq(el_count)", "from __main__ import fill_deq, el_count")
print('t2', t2.timeit(number=10))
deq = deque(lst)

el_count = 1000
print(f'# Добавление в начало lst {el_count} элементов')
t1 = Timer("insert_to_start_lst(lst, el_count)", "from __main__ import insert_to_start_lst, lst, el_count")
print('t1', t1.timeit(number=10))

print(f'# Добавление в начало deq {el_count} элементов')
t2 = Timer("insert_to_start_deq(deq, el_count)", "from __main__ import insert_to_start_deq, deq, el_count")
print('t2', t2.timeit(number=10))

print(f'# Добавление в конец lst {el_count} элементов')
t1 = Timer("insert_to_end_lst(lst, el_count)", "from __main__ import insert_to_end_lst, lst, el_count")
print('t1', t1.timeit(number=10))

print(f'# Добавление в конец deq {el_count} элементов')
t2 = Timer("insert_to_end_deq(deq, el_count)", "from __main__ import insert_to_end_deq, deq, el_count")
print('t2', t2.timeit(number=10))

value = 0
print('# Подсчет количества элементов lst равных 0')
t1 = Timer("get_count_lst(lst, value)", "from __main__ import get_count_lst, lst, value")
print('t1', t1.timeit(number=10))

print('# Подсчет количества элементов deq равных 0')
t2 = Timer("get_count_deq(deq, value)", "from __main__ import get_count_deq, deq, value")
print('t2', t2.timeit(number=10))

# Вывод:
# Из выполненных операций наилучшую производительность deque показывает на добавлении элементов в
# начало, либо конец очереди. В случае добавления в начало deq разница в два порядка.
# Первоначальное заполнение очереди, подсчет числа элементов, равных N, занимает примерно
# одинаковое время. Т.е. информация в документации верна

# # Заполнение lst
# t1 0.031723412000000006
# # Заполнение deq
# t2 0.047900579000000006
# # Добавление в начало lst 1000 элементов
# t1 0.473038857
# # Добавление в начало deq 1000 элементов
# t2 0.0006975759999999775
# # Добавление в конец lst 1000 элементов
# t1 0.0021247610000000305
# # Добавление в конец deq 1000 элементов
# t2 0.0006843140000000192
# # Подсчет количества элементов lst равных 0
# t1 0.02656557599999998
# # Подсчет количества элементов deq равных 0
# t2 0.027721153
