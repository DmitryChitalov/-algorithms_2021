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

from timeit import timeit
from collections import deque


def create_lst():
    new_lst = [i for i in range(100000)]
    return new_lst


def create_deque_lst(obj):
    deq_obj = deque(obj)
    return deq_obj


def add_to_list(obj):
    obj.append('1')
    return obj


def add_to_deque(obj):
    obj.append('1')
    return obj


def insert_in_list(obj):
    obj.insert(0, '1')
    return obj


def insert_in_deque(obj):
    obj.appendleft('1')
    return obj


def pop_in_list(obj):
    obj.pop()
    return obj


def pop_in_deque(obj):
    obj.pop()
    return obj


def pop_left_list(obj):
    obj.pop(0)
    return obj


def pop_left_deque(obj):
    obj.popleft()
    return obj


simple_lst = list('0' * 100000)
some_list = create_lst()
some_deque_list = create_deque_lst(simple_lst)
print(f"Создание списка через list: "
      f"{timeit('create_lst()', number=100, globals=globals())}")
print(f"Создание списка через deque: "
      f"{timeit('create_deque_lst(simple_lst)', number=100, globals=globals())}")
print(f"Добавление значения в конец списка через list: "
      f"{timeit('add_to_list(some_list)', number=10000, globals=globals())}")
print(f"Добавление значения в конец списка через deque: "
      f"{timeit('add_to_deque(some_deque_list)', number=10000, globals=globals())}")
print(f"Добавление значения в начало списка через list: "
      f"{timeit('insert_in_list(some_list)', number=10000, globals=globals())}")
print(f"Добавление значения в начало списка deque: "
      f"{timeit('insert_in_deque(some_deque_list)', number=10000, globals=globals())}")
print(f"Удаление значения с конца списка через list: "
      f"{timeit('pop_in_list(some_list)', number=10000, globals=globals())}")
print(f"Удаление значения с конца списка через deque: "
      f"{timeit('pop_in_deque(some_deque_list)', number=10000, globals=globals())}")
print(f"Удаление значения с начала списка через list: "
      f"{timeit('pop_left_list(some_list)', number=10000, globals=globals())}")
print(f"Удаление значения с начала списка через deque: "
      f"{timeit('pop_left_deque(some_deque_list)', number=10000, globals=globals())}")


"""
Создание deque намного быстрее чем через list. Также быстрее выполняется вставка и удаления в начале списка. 
Если удалять/вставлять значения в конец списка, то скорость идиентична. 
Ещё преимущестов deque доп.функции облегчающие работу программиста.
"""