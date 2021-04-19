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


test_lst = list()
test_deq = deque()
val_for_search = -1
n = 1000
# выражения, время которых мы замеряем
operation = ['создание', 'чтение', 'поиск', 'удаление из начала', 'добавление в начало', 'удаление из конца']
lst_operation = [
    '''for a in range(n):
    test_lst.append(a)''',
    '''for a in range(n):
    test_val=test_lst[a]''',
    '''if val_for_search in test_lst:
    pass''',
    '''for a in range(n):
    test_lst.pop(0)''',
    '''for a in range(n):
    test_lst.insert(0,a)''',
    '''for a in range(n):
    test_lst.pop()'''
]

deq_operation = [
    '''for a in range(n):
    test_deq.append(a)''',
    '''for a in range(n):
    test_val=test_deq[a]''',
    '''if val_for_search in test_deq:
    pass''',
    '''for a in range(n):
    test_deq.popleft()''',
    '''for a in range(n):
    test_deq.appendleft(a)''',
    '''for a in range(n):
    test_deq.pop()'''
]

print('Операции со списком:')
for op, st in zip(operation, lst_operation):
    print(f'{op} {timeit(st, number=100, globals=globals())}')

print('\nОперарации с deque')
for op, st in zip(operation, deq_operation):
    print(f'{op} {timeit(st, number=100, globals=globals())}')

"""
Операции со списком:
создание 0.005769805999999999
чтение 0.0034117159999999987
поиск 0.109804635
удаление из начала 1.451579651
добавление в начало 2.4521184509999996
удаление из конца 0.005412846999999665

Операрации с deque
создание 0.005300000000000082
чтение 0.004581697999999967
поиск 0.10567549400000065
удаление из начала 0.005026069000000355
добавление в начало 0.0053991060000004865
удаление из конца 0.004976076999999357

Выводы. В большенстве операциях deque равен списку. 
        В добавлении и удалении из начала deque лучше,
        также дополнительно имеет полезные методы.
"""
