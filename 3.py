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

lister = [i for i in range(1000000)]
my_l = deque(lister)


def ret_l():
    return lister[0]


def ret_d():
    return my_l[0]


def pop_l():
    lister.pop(0)


def pop_d():
    my_l.popleft()


def append_l():
    lister.append(12)


def append_d():
    my_l.append(12)


def insert_l():
    lister.insert(0, 17)


def insert_d():
    my_l.appendleft(17)


def ex_l():
    lister.extend([1, 2, 3, 4])


def ex_d():
    my_l.extend([1, 2, 3, 4])


print('return')
print(timeit('ret_l()', number=1000000, globals=globals()))
print(timeit('ret_d()', number=1000000, globals=globals()))

print('append')
print(timeit('append_l()', number=1000000, globals=globals()))
print(timeit('append_d()', number=1000000, globals=globals()))

print('append_left')
print(timeit('insert_l()', number=1000, globals=globals()))
print(timeit('insert_d()', number=1000, globals=globals()))

print('pop_left')
print(timeit('pop_l()', number=1000, globals=globals()))
print(timeit('pop_d()', number=1000, globals=globals()))

print('extend')
print(timeit('ex_l()', number=1000, globals=globals()))
print(timeit('ex_d()', number=1000, globals=globals()))
'''
Вывод : в документации Python всё верно сказано,
если вам нужно что-то быстро дописать или вытащить, используйте deque,
за исключением 'extend'(при 'extend' list быстрее').
Если вам нужен быстрый случайный доступ, используйте list,
что мы видим при многочисленных вызовах ('return')
'''