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

import cProfile
from collections import deque

def list_app_func(num):
    lst = []
    for i in num:
        lst.append(i)

def deque_app_func(num):
    lst = deque()
    for i in num:
        lst.append(i)

def list_ins_func(num):
    lst = []
    for i in num:
        lst.insert(0, i)

def deque_ins_func(num):
    lst = deque()
    for i in num:
        lst.appendleft(i)


def main():
    my_nums = [i for i in range(50000)]

    list_app_func(my_nums)
    deque_app_func(my_nums)
    list_ins_func(my_nums)
    deque_ins_func(my_nums)

cProfile.run('main()')

# судя по сделанным замерам, наиболее эффектиным будет использование deque