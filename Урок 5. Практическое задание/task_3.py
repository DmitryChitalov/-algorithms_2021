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

# 1) Заполнение листа и очереди через append показали примерно одинаковые трудозатраты на исполнение функций;
# 2) appendleft и insert работают примерно одинаково. Несмотря на то, что appendleft
# должен работать быстрее так как сложность О(1). А встроенная insert имеет сложность O(n).


from timeit import timeit
from collections import deque

simple_lst = []

deq_obj = deque()

def lst_filling():
    for el in range(1000):
        simple_lst.append(el)

def deq_filling():
    for el in range(1000):
        deq_obj.append(el)


print('РАБОТА С APPEND')
print(timeit('lst_filling', globals=globals()))
print(timeit('deq_filling', globals=globals()))


def lst_insert():
    for el in range(10000):
        simple_lst.insert(0, el)


def deq_apndlft():
    for el in range(10000):
        deq_obj.appendleft(el)


print('РАБОТА С INSERT И APPENDLEFT')
print(timeit('lst_insert', globals=globals()))
print(timeit('deq_apndlft', globals=globals()))