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
import collections
from collections import deque
from time import time

let_list = list('list')
deque_list = deque(let_list)

### start append ###
start = time()
for i in range(10000):
    deque_list.append(i)
    deque_list.appendleft(i)
end = time()
print(end - start)
### end append ###

### start pop ###
start = time()
for i in range(10000):
    deque_list.pop()
    deque_list.popleft()
end = time()
print(end - start)
### end pop ###

### start append ###
start = time()
for i in range(10000):
    let_list.insert(0, i)
    let_list.append(i)
end = time()
print(end - start)
### end append ###

### start pop ###
start = time()
for i in range(10000):
    list.pop([1000-i])
    list.pop([0])
end = time()
print(end - start)
### end pop ###

#deque быстрее работает со всеми операциями