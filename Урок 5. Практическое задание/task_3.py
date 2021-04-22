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

import random
import collections
from timeit import timeit

# Создаем две логическ одинаковые последовательности
v_list = [random.randint(1, 10000) for _ in range(1, 100000)]
v_deque = collections.deque(v_list)
v_attempts = 100000


def append_list():
    v_list.append(random.randint(1, 10000))


def append_deque():
    v_deque.append(random.randint(1, 10000))


def appendleft_list():
    v_list.insert(0, random.randint(1, 10000))


def appendleft_deque():
    v_deque.appendleft(random.randint(1, 10000))


def popleft_list():
    v_list.pop(0)


def popleft_deque():
    v_deque.popleft()


def popright_list():
    v_list.pop()


def popright_deque():
    v_deque.pop()


def getitem_list():
    v_list.__getitem__(random.randint(1, 10000))


def getitem_deque():
    v_deque.__getitem__(random.randint(1, 10000))


def reverse_list():
    v_list.reverse()


def reverse_deque():
    v_deque.reverse()


print('timeit append_list',
      round(
          timeit(
              'append_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit append_deque',
      round(
          timeit(
              'append_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit appendleft_list',
      round(
          timeit(
              'appendleft_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit appendleft_deque',
      round(
          timeit(
              'appendleft_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit popleft_list',
      round(
          timeit(
              'popleft_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit popleft_deque',
      round(
          timeit(
              'popleft_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit popright_list',
      round(
          timeit(
              'popright_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit popright_deque',
      round(
          timeit(
              'popright_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit getitem_list',
      round(
          timeit(
              'getitem_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit getitem_deque',
      round(
          timeit(
              'getitem_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit reverse_list',
      round(
          timeit(
              'reverse_list()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

print('timeit reverse_deque',
      round(
          timeit(
              'reverse_deque()',
              globals=globals(),
              number=v_attempts)
          , 4),
      'seconds')

"""
timeit append_list 0.1256 seconds
timeit append_deque 0.1032 seconds
timeit appendleft_list 16.9107 seconds
timeit appendleft_deque 0.0798 seconds
timeit popleft_list 5.5443 seconds
timeit popleft_deque 0.01 seconds
timeit popright_list 0.0105 seconds
timeit popright_deque 0.0106 seconds
timeit getitem_list 0.0817 seconds
timeit getitem_deque 0.1067 seconds
timeit reverse_list 3.9507 seconds
timeit reverse_deque 8.6239 seconds

ВЫВОД:
Согласно документации Deques поддерживают поточно-ориентированные, эффективные по памяти операции добавления 
и выталкивания с любой стороны deque с примерно одинаковой производительностью O(1) в любом направлении.
Мы видим подтверждение этому в тестах: процедура "добавление слева" для deque работает существенно быстрее аналогичной 
для списка.  Аналогично, процедура удаления элемента слева также гораздо эффективнее у deque. 
Процедуры добавления или удаления элементов справа сравнимы по производительности.
Методы доступа по индексу к списку и deque сравнимы по производительности.
Обращение списка существенно быстрее, чем обращение deque.
Полученные результаты  соответствуют описанию в документации
"""
