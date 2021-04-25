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

some_list = list(range(0, 10000))
some_deque = deque(range(0, 10000))

# добовление элемента в конец
print("#" * 100)
print("Добавление в конец")
print(timeit("some_list.append('1')", number=100000, globals=globals()))
print(timeit("some_deque.append('1')", number=100000, globals=globals()))

# добовление элемента в начало
print("#" * 100)
print("Добавление в начало")
print(timeit("some_list.insert(0,'1')", number=10000, globals=globals()))
print(timeit("some_deque.appendleft('1')", number=10000, globals=globals()))

# добовление элемента в начало
print("#" * 100)
print("Добавление в начало")
print(timeit("some_list.insert(0,'1')", number=10000, globals=globals()))
print(timeit("some_deque.insert(0,'1')", number=10000, globals=globals()))

# подсчитать элементы
print("#" * 100)
print("Подсчитать элементы")
print(timeit("some_list.count(1)", number=100, globals=globals()))
print(timeit("some_deque.count(1)", number=100, globals=globals()))

# удаляем посл эл
print("#" * 100)
print("удаляем последний элемент pop")
print(timeit("some_list.pop()", number=10, globals=globals()))
print(timeit("some_deque.pop()", number=10, globals=globals()))

# удаляем первый элемент
print("#" * 100)
print("удаляем первый элемент pop vs popleft")
print(timeit("some_list.pop(0)", number=10, globals=globals()))
print(timeit("some_deque.popleft()", number=10, globals=globals()))

# переворачиваем
print("#" * 100)
print("переворачиваем reverse")
print(timeit("some_list.reverse()", number=10000, globals=globals()))
print(timeit("some_deque.reverse()", number=10000, globals=globals()))

# очистка
print("#" * 100)
print("очистка")
print(timeit("some_list.clear()", number=100, globals=globals()))
print(timeit("some_deque.clear()", number=100, globals=globals()))

"""
 При добавление в конец методом append список работает быстрее
 list - 0.008865999999999999
 deque - 0.006389899999999997
 
 При добавление в начало insert и appendleft, deque работает намного быстрее
 list - 0.6246752999999999
 deque - 0.0006595999999999824
 
  При добавление в начало insert и insert, deque работает намного быстрее
  list - 0.6803818000000001
  deque - 0.0011079000000000505
  
  При подсчете элементов методом count примерно время работы одинаковое
  list - 0.22714070000000008
  deque - 0.2375235
  
  При удаление элементов методом pop, deque работает быстрее
  list - 2.5999999999637424e-06
  deque - 2.2000000001742848e-06
  
  При удаление элементов методом pop vs popleft, список работает намного быстрее
  list - 0.0005353999999999637
  deque - 1.7999999999407379e-06
  
  При использовании метода reverse, список работает быстрее
  list - 0.6526737000000002
  deque - 1.0643103999999997
  
  При использовании метода clear, список работает быстрее
  list - 0.0003957000000003319
  deque - 0.0007272999999998753
  
  Выражение в начале верно, при добавление и вытаскивание из конуца работает быстрее deque
  Если нужен быстрый случайный доступ, то list.
"""
