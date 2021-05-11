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
from timeit import timeit
from collections import deque

list_smple = []
list_deque = deque()

def firstel_lstsmpl(numbs):
    for i in range(numbs):
        list_smple.insert(0, 1)


def firstel_lstdeque(numbs):
    for i in range(numbs):
        list_deque.appendleft(0)

print('list_smple in добавление в начало: ', timeit('firstel_lstsmpl(100000)', number=1, globals=globals()))
print('list_deque in добавление в начало: ', timeit('firstel_lstdeque(100000)', number=1, globals=globals()))
'''
Результаты:
list_smple in добавление в начало:  5.997222
list_deque in добавление в начало:  0.011685400000000179
'''

def lastel_lstsmpl(numbs):
    for i in range(numbs):
        list_smple.append(0)

def lastel_lstdeque(numbs):
    for i in range(numbs):
        list_deque.append(0)

print('list_smple in добавление в конец: ', timeit('lastel_lstsmpl(100000)', number=1, globals=globals()))
print('list_deque in добавление в конец: ', timeit('lastel_lstdeque(100000)', number=1, globals=globals()))
'''
Результаты:
list_smple in добавление в конец:  0.016671399999999892
list_deque in добавление в конец:  0.007677200000000717
'''

def popfirstel_lstsmpl(numbs):
    for i in range(numbs):
        list_smple.pop(0)

def popfirstel_lstdeque(numbs):
    for i in range(numbs):
        list_deque.popleft()

def poplastel_lstsmpl(numbs):
    for i in range(numbs):
        list_smple.pop()

def poplastel_lstdeque(numbs):
    for i in range(numbs):
        list_deque.pop()

print('list_smple in удаление в начале: ', timeit('popfirstel_lstsmpl(100000)', number=1, globals=globals()))
print('list_deque in удаление в начале: ', timeit('popfirstel_lstdeque(100000)', number=1, globals=globals()))
print('list_smple in удаление в конце: ', timeit('poplastel_lstsmpl(100000)', number=1, globals=globals()))
print('list_deque in удаление в конце: ', timeit('poplastel_lstdeque(100000)', number=1, globals=globals()))
'''
Результаты:
list_smple in удаление в начале:  23.8420405
list_deque in удаление в начале:  0.009103700000000714
list_smple in удаление в конце:  0.00873239999999953
list_deque in удаление в конце:  0.00802060000000182
'''

def index_lstsmpl():
    for i in range(len(list_smple)):
        list_smple[i]

def index_lstdeque():
    for i in range(len(list_deque)):
        list_deque[i]

print('list_smple in index: ', timeit('index_lstsmpl()', number=1, globals=globals()))
print('list_deque in index: ', timeit('index_lstdeque()', number=1, globals=globals()))

'''
Результаты:
list_smple in index:  6.600000000002437e-06
list_deque in index:  8.100000000003937e-06
'''

"""
Вывод:
При добавлении и удалении элементов в конце список и дэк работают почти одинаково
При работе с началом списка (добавление и удаление) дэк имеет хорошее преимущество перед списком
Однако список хорошо справляется при точечной работе с доступом по индексу, нежели чем дэк. 

Поэтому выражение ниже можем считать справедливым
- если вам нужно что-то быстро дописать или вытащить, используйте deque.
- Если вам нужен быстрый случайный доступ, используйте list.
"""