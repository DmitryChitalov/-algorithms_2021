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
# 1)


def append_lst(lst_):
    for i in range(5):
        lst_.append(i)
    return lst_


def append_deq(deq_):
    for i in range(5):
        deq_.append(i)
    return deq_


lst_1 = []
deq_1 = deque()

print(
    timeit(
        "append_lst(lst_1)",
        globals=globals()
        ), ' - Заполнение в конец списка')
print(
    timeit(
        "append_deq(deq_1)",
        globals=globals()
        ), ' - Заполнение в конец очереди')

# 2)


def insert_lst(lst_):
    for i in range(5):
        lst_.insert(0, i)
    return lst_


def appendleft_deq(deq_):
    for i in range(5):
        deq_.appendleft([i])
    return deq_


def pop_lst(lst_):
    for i in range(len(lst_)):
        lst_.pop()
    return lst_


def pop_deq(deq_):
    for i in range(len(deq_)):
        deq_.pop()
    return deq_


def remove_lst(lst_):
    for i in range(len(lst_)):
        lst_.remove()
    return lst_


def popleft_deq(deq_):
    for i in range(len(deq_)):
        deq_.popleft()
    return deq_


def extend_lst(lst_):
    lst_.extend([0, 1, 2, 3, 4])
    return lst_


def extend_deq(deq_):
    deq_.extend([0, 1, 2, 3, 4])
    return deq_


def insert_another_lst(lst_):
    lst_.insert(0, '0, 1, 2, 3, 4')
    return lst_


def extendleft_deq(deq_):
    deq_.extendleft([0, 1, 2, 3, 4])
    return deq_


lst_2 = [1, 2, 3, 4, 5]
deq_2 = deque([1, 2, 3, 4, 5])

print(
    timeit(
        "insert_lst(lst_2)",
        globals=globals(),
        number=1000), ' - Элемент в начало списка, значение number=1000, так как метод insert')
print(
    timeit(
        "appendleft_deq(deq_2)",
        globals=globals(),
        number=1000), ' - Элемент в начало очереди, значение number=1000, так как метод insert')
print(
    timeit(
        "pop_lst(lst_2)",
        globals=globals()
        ), ' - Достать элемент конца списка')
print(
    timeit(
        "pop_deq(deq_2)",
        globals=globals()
        ), ' - Достать элемент конца очереди')
print(
    timeit(
        "remove_lst(lst_2)",
        globals=globals()
        ), ' - Удаляет первый элемент в списке')
print(
    timeit(
        "popleft_deq(deq_2)",
        globals=globals()
        ), ' - Достать элемент начала очереди')
print(
    timeit(
        "extend_lst(lst_2)",
        globals=globals()
        ), ' - Добавляет элементы в конец списка')
print(
    timeit(
        "extend_deq(deq_2)",
        globals=globals()
        ), ' - Добавляет элементы в конец очереди')
print(
    timeit(
        "insert_another_lst(lst_2)",
        globals=globals(),
        number=1000), ' - Добавляет элементы в начало списка, значение number=1000, так как метод insert')
print(
    timeit(
        "extendleft_deq(deq_2)",
        globals=globals(),
        number=1000), ' - Добавляет элементы в начало очереди, значение number=1000, так как метод insert')