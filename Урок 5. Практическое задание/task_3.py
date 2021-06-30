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

#####################################
# Замеры list

print('list append: ', round((timeit('''
def list_append(my_list):
    for i in range(10):
        my_list.append(i)
    return my_list
my_list = []
list_append(my_list)
''', number=10000)), 7))

print('list pop:    ', round((timeit('''
def list_pop():
    my_list = [i for i in range(10)]
    for i in range(10):
        my_list.pop()
    return my_list
list_pop()
''', number=10000)), 7))

print('list insert: ', round((timeit('''
def list_insert(my_list):
    for i in range(10):
        my_list.insert(i, 0)
    return my_list
my_list = []
list_insert(my_list)
''', number=10000)), 7))

#####################################
# Замеры deque

print('deque append:     ', round((timeit('''
from collections import deque
def deque_append(my_deque):
    for i in range(10):
        my_deque.append(i)
    return my_deque
my_deque = deque()
deque_append(my_deque)
''', number=10000)), 7))


print('deque appendleft: ', round((timeit('''
from collections import deque
def deque_appendleft(my_deque):
    for i in range(10):
        my_deque.appendleft(i)
    return my_deque
my_deque = deque()
deque_appendleft(my_deque)
''', number=10000)), 7))


print('deque pop:        ', round((timeit('''
from collections import deque
def deque_pop():
    my_deque = deque([i for i in range(10)])
    for i in range(10):
        my_deque.pop()
    return my_deque
deque_pop()
''', number=10000)), 7))


print('deque insert:     ', round((timeit('''
from collections import deque
def deque_insert(my_deque):
    for i in range(10):
        my_deque.insert(i, 0)
    return my_deque
my_deque = deque()
deque_insert(my_deque)
''', number=10000)), 7))


# Вывод: Добавление и удаление у list работает быстрее, чем у deque.
#        deque, как мне кажется, опережает list с помощью разднообразия команд, которыми можно управлять deque
#        Несомненно deque полезен, и без сомнения ему можно найти применение, но list всё же выигрывает.
