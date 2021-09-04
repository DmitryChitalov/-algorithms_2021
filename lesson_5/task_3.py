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


def left_list_extend(t_list, ext_part):
    for el in ext_part:
        t_list.insert(0, el)
    return t_list


def left_deque_extend(t_deque, ext_part):
    t_deque.extendleft(ext_part)
    return t_deque


test_list = ['a', 'b', 'c']
test_deque = deque('abc')
extend_part = 'lbk'

print('Создание')
print('list:  ', timeit("test_list = ['a', 'b', 'c']", number=10000))
print('deque: ', timeit("test_deque = deque('abc')", globals=globals(), number=10000))
print('\nДобавление элемента в начало')
print('list:  ', timeit("test_list.insert(0, 'k')", globals=globals(), number=10000))
print('deque: ', timeit("test_deque.appendleft('k')", globals=globals(), number=10000))
print('\nУдаление элемента из начала')
print('list:  ', timeit("test_list.pop(0)", globals=globals(), number=10000))
print('deque: ', timeit("test_deque.popleft()", globals=globals(), number=10000))
print('\nВключение нескольких элементов в начало')
print('list:  ', timeit("left_list_extend(test_list, extend_part)", globals=globals(), number=10000))
print('deque: ', timeit("left_deque_extend(test_deque, extend_part)", globals=globals(), number=10000))

# результат работы программы
#
# Создание
# list:   0.0005015999999999979
# deque:  0.0015453000000000064
#
# Добавление элемента в начало
# list:   0.029218600000000004
# deque:  0.0005967000000000056
#
# Удаление элемента из начала
# list:   0.014078599999999997
# deque:  0.0005533999999999956
#
# Включение нескольких элементов в начало
# list:   0.2918233
# deque:  0.0019951000000000274
#
# Создание и заполнение дека занимает больше времени, чем создание списка
# Любые операции по работе с элементами в начале у дека в сотни раз быстрее чем у списка
