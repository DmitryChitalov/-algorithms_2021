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
from random import randint
from collections import deque

RAND_FROM = 1
RAND_TO = 10
LIST_NUM = 1000

my_list = [randint(RAND_FROM, RAND_TO) for i in range(LIST_NUM)]
my_deque = deque(my_list)

def list_insert_left(my_list): # 2.331778246
    my_list.insert(0, 1)
    return my_list

def deque_insert_left(my_deq): # 0.012822941000000032
    my_deq.appendleft(1)
    return my_deq

def list_pop_left(my_list): # 1.6549568570000002
    my_list.pop(0)
    return my_list

def deque_pop_left(my_deq): # 0.011912592999999916
    my_deq.popleft()
    return my_deq

def list_get(my_list): # 0.012520632000000198
    return my_list[LIST_NUM - 1]

def deque_get(my_deq): # 0.014342572000000331
    return my_deq[LIST_NUM - 1]

print(f"list_insert_left: {timeit('list_insert_left(my_list)', globals=globals(), number=100000)}")
print(f"deque_insert_left: {timeit('deque_insert_left(my_deque)', globals=globals(), number=100000)}")
print(f"list_pop_left: {timeit('list_pop_left(my_list)', globals=globals(), number=100000)}")
print(f"deque_pop_left: {timeit('deque_pop_left(my_deque)', globals=globals(), number=100000)}")
print(f"list_get: {timeit('list_get(my_list)', globals=globals(), number=100000)}")
print(f"deque_get: {timeit('deque_get(my_deque)', globals=globals(), number=100000)}")

# Добавление элементов быстрее в deque
# Доступ к элементу быстрее в list (хоть и не намного)
# как и написано в документации