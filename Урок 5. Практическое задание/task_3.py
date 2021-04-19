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
from random import randint

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


def list_insert(_list):
    return _list.insert(5000, 1000)


def get_random_values(_list, n=100):
    return [_list[randint(0, 13999)] for _ in range(n)]


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

temp_list = get_list()
temp_deque = get_deque()

print('List insert:',
      timeit(
          'list_insert(temp_list)',
          setup='from __main__ import list_insert, temp_list',
          number=10000))
print('Deque insert:',
      timeit(
          'list_insert(temp_deque)',
          setup='from __main__ import list_insert, temp_deque',
          number=10000))

temp_list = get_list()
temp_deque = get_deque()

print('Get random elements from List:',
      timeit(
          'get_random_values(temp_list)',
          setup='from __main__ import get_random_values, temp_list',
          number=1000))
print('Get random elements from Deque:',
      timeit(
          'get_random_values(temp_deque)',
          setup='from __main__ import get_random_values, temp_deque',
          number=1000))

"""
Результаты:

get_list 0.27492479999999997
get_deque 0.8092379000000001
list_append 0.0009094999999998965
deque_append 0.0008037999999999101
list_appendleft 0.09000499999999989
deque_appendleft 0.0007912000000001029
list_reverse 0.03735960000000005
deque_reverse 0.06579630000000014
list_pop: 6.999999999979245e-05
deque_pop: 6.879999999997999e-05
list_popleft: 0.012452099999999966
deque_popleft: 0.0006360999999999173
List insert: 0.06634799999999985
Deque insert: 0.05249389999999998
Get random elements from List: 0.05474690000000004
Get random elements from Deque: 0.0660113

Операции связанные со вставкой/извлечением элементов из начала коллекции для Deque выполняются намного быстрее 
чем для обычного списка. 
Операции с произвольными элементами и с элементами из конца выполняются за примерно  за одинаковое время.
Функции reverse и copy для deque выполняются медленее чем для встроенных списков.

"""
