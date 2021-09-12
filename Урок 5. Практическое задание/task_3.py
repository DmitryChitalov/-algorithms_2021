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

import time
from collections import deque

num = 10000

new_list = [el for el in range(num)]
new_deque = deque(new_list)


def time_check(action):
    def wrapper(*args):
        start = time.time()
        result = action(*args)
        finish = time.time()
        print(f'Время выполнения: {finish - start}\n')
        return result

    return wrapper


@time_check
def append_list(num):
    for i in range(num):
        new_list.insert(0, i)


@time_check
def append_deque(num):
    for i in range(num):
        new_deque.appendleft(i)


@time_check
def extend_list():
    a = [1, 2]
    for i in range(len(a)):
        new_list.insert(0, a[i])


@time_check
def extend_deque():
    new_deque.extendleft([1, 2])


@time_check
def pop_list(new_list):
    for i in range(len(new_list)):
        new_list.pop(0)


@time_check
def pop_deque(new_deque):
    for i in range(len(new_deque)):
        new_deque.popleft()


print('Cписок appendleft: ')
new_list_1 = append_list(num)

print('Очередь appendleft: ')
new_deque_1 = append_deque(num)

print('Cписок extendleft: ')
new_list_2 = extend_list()

print('Очередь extendleft: ')
new_deque_2 = extend_deque()

print('Cписок popleft: ')
new_list_3 =pop_list(new_list)

print('Очередь popleft: ')
new_deque_3 = pop_deque(new_deque)


"""
Cписок appendleft: 
Время выполнения: 0.07506704330444336
Очередь appendleft: 
Время выполнения: 0.0

Cписок extendleft: 
Время выполнения: 0.0009829998016357422
Очередь extendleft: 
Время выполнения: 0.0

Cписок popleft: 
Время выполнения: 0.5515656471252441
Очередь popleft: 
Время выполнения: 0.0010111331939697266

На основании замеров можно сделать вывод, что deque имеет преимущество над списком.
Все операции left, которые были выполнены, очередь выполняла быстрее списка.
"""