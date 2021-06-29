  
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

# 1. Создаем простой список (list) и очередь (deque).

from random import randint
from collections import deque
from timeit import timeit

def fill_list():
    l = []
    for i in range(10):
        num = randint(10, 100)
        l.append(num)
# Это можно было записать в одну строку: l = [randint(10, 100) for i in range(10)]
    return l
print(fill_list())

def fill_deque():
    l = [randint(10, 100) for i in range(10)]
    dq = deque(l)
    #l.append(num)
    return dq
print(fill_deque())

print(f'Заполнение списка', timeit("fill_list()", globals=globals(), number=1000))
print(f'Заполнение Deque', timeit("fill_deque()", globals=globals(), number=1000))
print('Вывод: Заполнение происходит одинаково быстро')
print('-----------------------------------------------')

# Сравнивываем операцию вставки эл-та в ДЕК (appendleft() - в начало очереди, append() - в конец) и
# в СПИСОК (append() - в конец, insert(index, item) - по индексу 0).

# Добавление в конец СПИСка с функцией append
def add_list():
    lst = [randint(1, 20) for i in range(1000)]
    lst.append(10000)
    return (lst)
print('Добавление в конец СПИСка с функцией append', add_list())

# Добавление в начало СПИСка с функцией insert
def add_list_1():
    lst = [randint(1, 20) for i in range(1000)]
    lst.insert(0, 10000)
    return (lst)
print('Добавление в начало СПИСка с функцией insert', add_list_1())


# Вставка эл-та в ДЕК appendleft() - в начало очереди.
def add_deque():
    l = [randint(10, 100) for i in range(1000)]
    dq = deque(l)
    dq.appendleft(10000)
    return dq
print('Вставка эл-та в ДЕК appendleft() - в начало очереди', add_deque())

# Вставка эл-та в ДЕК append() -  в конец очереди.
def add_deque_1():
    l = [randint(10, 100) for i in range(1000)]
    dq = deque(l)
    dq.append(10000)
    return dq
print('Вставка эл-та в ДЕК append() -  в конец очереди', add_deque_1())
print('-----------------------------------------------')

print(f'Добавление в конец СПИСка с функцией append', timeit("add_list()", globals=globals(), number=10000))
print(f'Вставка эл-та в ДЕК append() -  в конец очереди', timeit("add_deque_1()", globals=globals(), number=10000))

print(f'Добавление в начало СПИСка с функцией insert', timeit("add_list_1()", globals=globals(), number=10000))
print(f'Вставка эл-та в ДЕК appendleft() - в начало очереди', timeit("add_deque()", globals=globals(), number=10000))

"""
Добавление в конец СПИСка с функцией append 6.6202486
Вставка эл-та в ДЕК append() -  в конец очереди 6.9986401
Добавление в начало СПИСка с функцией insert 7.449809499999999
Вставка эл-та в ДЕК appendleft() - в начало очереди 5.6738320999999985

В конец: Список и Дек - примерно одинаково
В начало - Дек чуть быстрее
"""























# Создаем очередь (deque).

