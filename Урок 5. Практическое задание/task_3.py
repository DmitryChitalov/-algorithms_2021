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

test_list = [i for i in range(1000, 15000)]
test_deque = deque(test_list)


def list_add_end(_list, val=0):
    _list.append(val)
    return _list


def deque_add_end(_deque, val=0):
    _deque.append(val)
    return _deque


def list_add_start(_list, val=0):
    _list.insert(0, val)


def deque_add_start(_deque, val=0):
    _deque.appendleft(val)


def list_reverse(_list):
    return _list.reverse()


def deque_reverse(_deque):
    return _deque.reverse()


def list_pop(_list):
    return _list.pop()


def deque_pop(_deque):
    return _deque.pop()


def list_popleft(_list):
    return _list.pop(0)


def deque_popleft(_deque):
    return _deque.popleft()


value = 10000
index = 5000

temp_list = test_list.copy()
temp_deque = test_deque.copy()

print(list_pop(temp_list))

print('list_add_end',
      timeit(
          'list_add_end(temp_list, value)',
          setup='from __main__ import list_add_end, temp_list, value',
          number=10000))
print('deque_add_end',
      timeit(
          'deque_add_end(temp_deque, value)',
          setup='from __main__ import deque_add_end, temp_deque, value',
          number=10000))

temp_list = test_list.copy()
temp_deque = test_deque.copy()

print('list_add_start',
      timeit(
          'list_add_start(temp_list, value)',
          setup='from __main__ import list_add_start, temp_list, value',
          number=10000))
print('deque_add_start',
      timeit(
          'deque_add_start(temp_deque, value)',
          setup='from __main__ import deque_add_start, temp_deque, value',
          number=10000))

temp_list = test_list.copy()
temp_deque = test_deque.copy()

print('list_reverse()',
      timeit(
          'list_reverse(temp_list)',
          setup='from __main__ import list_reverse, temp_list',
          number=10000))
print('deque_reverse()',
      timeit(
          'deque_reverse(temp_deque)',
          setup='from __main__ import deque_reverse, temp_deque',
          number=10000))

temp_list = test_list.copy()
temp_deque = test_deque.copy()

print('list_pop:',
      timeit(
          'list_pop(temp_list)',
          setup='from __main__ import list_pop, temp_list',
          number=1000))
print('deque_pop:',
      timeit(
          'deque_pop(temp_deque)',
          setup='from __main__ import deque_pop, temp_deque',
          number=1000))

temp_list = test_list.copy()
temp_deque = test_deque.copy()

print('list_popleft:',
      timeit(
          'list_popleft(temp_list)',
          setup='from __main__ import list_popleft, temp_list',
          number=10000))
print('deque_popleft:',
      timeit(
          'deque_popleft(temp_deque)',
          setup='from __main__ import deque_popleft, temp_deque',
          number=10000))
