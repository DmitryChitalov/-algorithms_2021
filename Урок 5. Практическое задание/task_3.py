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

lst = [1]*10000
deq = deque(lst)

print('Вставка в конец:')
print(f"\tList:  {timeit('lst.append(1)', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq.append(1)', globals=globals(),number=100000):0.8f}")
'''
Вставка в конец:
        List:  0.01127330
        Deque: 0.00740940
'''
print('Вставка в начало:')
print(f"\tList:  {timeit('lst.insert(0,1)', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq.appendleft(1)', globals=globals(),number=100000):0.8f}")
'''
Вставка в начало:
        List:  18.22218420
        Deque: 0.00821860
'''
print('Взятие из конца:')
print(f"\tList:  {timeit('lst.pop()', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq.pop()', globals=globals(),number=100000):0.8f}")
'''
Взятие из конца:
        List:  0.00712000
        Deque: 0.01063970
'''
print('Взятие из начала:')
print(f"\tList:  {timeit('lst.pop(0)', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq.popleft()', globals=globals(),number=100000):0.8f}")
'''
Взятие из начала:
        List:  6.59513980
        Deque: 0.00627960
'''
print('Взятие по индексу:')
print(f"\tList:  {timeit('lst[500]', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq[500]', globals=globals(),number=100000):0.8f}")
'''
Взятие по индексу:
        List:  0.00656600
        Deque: 0.00742640
'''
print('Вставка в середину:')
print(f"\tList:  {timeit('lst.insert(500,2)', globals=globals(),number=100000):0.8f}")
print(f"\tDeque: {timeit('deq.insert(500,2)', globals=globals(),number=100000):0.8f}")
'''
Вставка в середину:
        List:  4.04886350
        Deque: 0.21422800
'''
'''
Deque - быстрее в работе с началом и вставке по индексу
Взятие по индексу примерно одинаково

'''