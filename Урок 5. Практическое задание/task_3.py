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

my_list = [elem for elem in range(100000)]
my_deque = deque(my_list)


def pop_left_deque(check_deque):  # вытаскиваем из начала очереди
    check_deque.popleft()


def append_left_deque(check_deque, el):  # добавляем в начало очереди
    check_deque.appendleft(el)


def pop_left_list(check_list):  # вытаскиваем из начала списка
    check_list.pop(0)


def append_left_list(check_list, el):  # вставляем в начало списка
    check_list.insert(0, el)


print('popleft_list')
print(timeit('pop_left_list(my_list)', globals=globals(), number=1000))

print('popleft_deque')
print(timeit('pop_left_deque(my_deque)', globals=globals(), number=1000))

print('append_left_list')
print(timeit('append_left_list(my_list, 5)', globals=globals(), number=1000))

print('append_left_deque')
print(timeit('append_left_deque(my_deque, 5)', globals=globals(), number=1000))

"""
Информация в документации является правильной. 
Время затраченное на исполнение программ отражает правильность написанного, очередь быстрее, если мы вытаскивам
или вставляем элемент.
"""
