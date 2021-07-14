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
from collections import deque
from timeit import timeit
from copy import copy

test_lst = [i for i in range(100000)]
test_dq = deque([i for i in range(100000)])
test_ext = [1, 2, 3, 'str', False]


# Создание списка и заполнение справа
def fill_left_lst():
    lst = []
    for i in range(1000):
        lst.append(i)


# Создание списка и заполнение слева
def fill_right_lst():
    lst = []
    for i in range(1000):
        lst.insert(0, i)


# Создание deque и заполнение справа
def fill_left_dq():
    dq = deque()
    for i in range(1000):
        dq.append(i)


# Создание deque и заполнение слева
def fill_right_dq():
    dq = deque()
    for i in range(1000):
        dq.appendleft(i)


# Удаление элементов списка слева
def pop_right_lst(lst: list):
    for i in range(10):
        lst.pop()


# Удаление элементов списка справа
def pop_left_lst(lst: list):
    for i in range(10):
        lst.pop(0)


# Удаление элементов deque слева
def pop_left_dq(dq: deque):
    for i in range(10):
        dq.pop()


# Удаление элементов deque справа
def pop_right_dq(dq: deque):
    for i in range(10):
        dq.popleft()


# extend  списка слева
def extend_left_lst(lst: list, ext: list):
    for el in ext:
        lst.insert(0, el)


# extend списка справа
def extend_right_lst(lst: list, ext: list):
    lst.extend(ext)


# extend deque слева
def extend_left_dq(dq: deque, ext: list):
    dq.extend(ext)


# extend deque справа
def extend_right_dq(dq: deque, ext: list):
    dq.extendleft(ext)


# Замеры
print('Заполнение списка слева: ',
      timeit(
          "fill_right_lst()",
          globals=globals(),
          number=100))

print('Заполнение deque слева: ',
      timeit(
          "fill_left_dq()",
          globals=globals(),
          number=100))

print('Заполнение списка справа: ',
      timeit(
          "fill_left_lst()",
          globals=globals(),
          number=100))

print('Заполнение deque справа: ',
      timeit(
          "fill_right_dq()",
          globals=globals(),
          number=100))

print('Удаление элементов списка слева: ',
      timeit(
          "pop_left_lst(test_lst)",
          globals=globals(),
          number=10))

print('Удаление элементов deque слева: ',
      timeit(
          "pop_left_dq(test_dq)",
          globals=globals(),
          number=10))

print('Удаление элементов списка справа: ',
      timeit(
          "pop_right_lst(test_lst)",
          globals=globals(),
          number=10))

print('Удаление элементов deque справа: ',
      timeit(
          "pop_right_dq(test_dq)",
          globals=globals(),
          number=10))


print('extend списка слева: ',
      timeit(
          "extend_left_lst(test_lst, test_ext)",
          globals=globals(),
          number=10))

print('extend deque слева: ',
      timeit(
          "extend_left_dq(test_dq, test_ext)",
          globals=globals(),
          number=10))

print('extend списка справа: ',
      timeit(
          "extend_right_lst(test_lst, test_ext)",
          globals=globals(),
          number=10))

print('extend deque справа: ',
      timeit(
          "extend_right_dq(test_dq, test_ext)",
          globals=globals(),
          number=10))

# Результаты
# Заполнение списка слева:  0.018198
# Заполнение deque слева:  0.004079300000000008
# Заполнение списка справа:  0.004329399999999997
# Заполнение deque справа:  0.004032999999999995
# Удаление элементов списка слева:  7.900000000005125e-06
# Удаление элементов deque слева:  9.799999999990372e-06
# Удаление элементов списка справа:  0.001786800000000005
# Удаление элементов deque справа:  6.499999999992623e-06
# extend списка слева:  0.001610399999999998
# extend deque слева:  3.5000000000035003e-06
# extend списка справа:  1.799999999996249e-06
# extend deque справа:  6.900000000004125e-06

# Получились весьма ожидаемые результаты: со стандартными для списка операциями он работает сопоставимо или быстрее,
# чем deque,но что касается операций слева, то deque бесспорно выигрывает и по скорости и по лаконичности кода
