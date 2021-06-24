"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""

from collections import deque
from timeit import timeit


def ls_insertion():
    new_list = []
    for i in range(100):
        new_list.insert(0, i)
    return new_list


def deq_append_left():
    new_deque = deque()
    for i in range(100):
        new_deque.appendleft(i)
    return new_deque


def ls_pop():
    ls = [10, 20, 30]
    ls.pop(0)
    return ls


def deq_pop_left():
    deq_ = deque([10, 20, 30])
    deq_.popleft()
    return deq_


def ls_ext():
    ls = [10, 20, 30]
    ls.reverse()
    ls.extend([5, 3, 1])
    ls.reverse()
    return ls


def deq_ext_left():
    deq_ = deque([10, 20, 30])
    deq_.extendleft([5, 3, 1])
    return deq_


print(timeit("ls_insertion()", globals=globals(), number=100000))
print(timeit("deq_append_left()", globals=globals(), number=100000))
print('=========')
print(timeit("ls_pop()", globals=globals(), number=100000))
print(timeit("deq_pop_left()", globals=globals(), number=100000))
print('=========')
print(timeit("ls_ext()", globals=globals(), number=100000))
print(timeit("deq_ext_left()", globals=globals(), number=100000))
print('=========')

"""Аналитика:
1.1941622
0.5166793000000001
=========
0.020346799999999998
0.033561399999999963
=========
0.034291199999999966
0.04442769999999996
=========

Результаты замеров показали преимущество операции заполнения у дека(видно по первому блоку).
Вставка происходит быстрее у дека за счет константной сложности вставки против линейной - у списка.

В остальном время одинаковое, даже в третьем блоке, когда делали расширение слева.
У списка нет аналогичного метода, поэтому пришлось реверсировать, но сложность при этом
осталась линейной, поэтому время примерно равное.

Вывод: дек является очень крутой структурой, и в плане скорости работы, и в плане удобства,
а тут ещё и встроенный - просто подарок. Беру его на карандаш, и обязательно буду использовать в будущем.
"""