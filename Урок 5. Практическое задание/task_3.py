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


def get_list():
    return test_list.copy()


def get_deque():
    return test_deque.copy()


def list_append(_list, val=0):
    _list.append(val)
    return _list


def deque_append(_deque, val=0):
    _deque.append(val)
    return _deque


def list_appendleft(_list, val=0):
    _list.insert(0, val)


def deque_appendleft(_deque, val=0):
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

print(type(deque))

value = 10000
index = 5000

temp_list = get_list()
temp_deque = get_deque()

print('get_list',
      timeit(
          'get_list()',
          setup='from __main__ import get_list, get_list',
          number=10000))
print('get_deque',
      timeit(
          'get_deque()',
          setup='from __main__ import get_deque, get_deque',
          number=10000))

print('list_append',
      timeit(
          'list_append(temp_list, value)',
          setup='from __main__ import list_append, temp_list, value',
          number=10000))
print('deque_append',
      timeit(
          'deque_append(temp_deque, value)',
          setup='from __main__ import deque_append, temp_deque, value',
          number=10000))

temp_list = get_list()
temp_deque = get_deque()

print('list_appendleft',
      timeit(
          'list_appendleft(temp_list, value)',
          setup='from __main__ import list_appendleft, temp_list, value',
          number=10000))
print('deque_appendleft',
      timeit(
          'deque_appendleft(temp_deque, value)',
          setup='from __main__ import deque_appendleft, temp_deque, value',
          number=10000))

temp_list = get_list()
temp_deque = get_deque()

print('list_reverse',
      timeit(
          'list_reverse(temp_list)',
          setup='from __main__ import list_reverse, temp_list',
          number=10000))
print('deque_reverse',
      timeit(
          'deque_reverse(temp_deque)',
          setup='from __main__ import deque_reverse, temp_deque',
          number=10000))

temp_list = get_list()
temp_deque = get_deque()

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

temp_list = get_list()
temp_deque = get_deque()

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

"""
Результаты:

get_list 0.368733378
get_deque 1.082350129
list_append 0.0012524099999999816
deque_append 0.0010660239999999988
list_appendleft 0.12246638799999987
deque_appendleft 0.0010945759999998472
list_reverse 0.05054520299999998
deque_reverse 0.0917512250000001
list_pop: 8.6295000000014e-05
deque_pop: 8.854099999999754e-05
list_popleft: 0.013675779000000166
deque_popleft: 0.0008591070000001366

Результаты измерений подтверждают приведенные в документации области применения для deque и list
Коллекция deque хорошо подходит для извления/вставки элементов в начало и в конец такого объекта, 
однако требует больше времени для его создания. Также функция reverse в deque работает медленнее.

"""