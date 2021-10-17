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
import collections
from timeit import timeit


lst = ['a', 'b', 'c']
dq = collections.deque(['a', 'b', 'c'])


def app_left1(dq: collections.deque):
    dq.appendleft('a')


def app_left2(lst: list):
    lst.insert(0, 'a')


def app_right1(dq: collections.deque):
    dq.append('a')


def app_right2(lst: list):
    lst.append('a')


def pop_left1(dq: collections.deque):
    dq.popleft()


def pop_left2(lst: list):
    lst.pop(0)


def pop_right1(dq: collections.deque):
    dq.popleft()


def pop_right2(lst: list):
    lst.pop()


def ext_left1(dq: collections.deque):
    dq.extendleft(['a', 'b', 'c'])


def ext_left2(lst: list):
    lst = ['a', 'b', 'c'] + lst


def ext_right1(dq: collections.deque):
    dq.extend(['a', 'b', 'c'])


def ext_right2(lst: list):
    lst.extend(['a', 'b', 'c'])


print('Добавление слева:')
print(timeit('app_left1(dq)', globals=globals(), number=10000))
print(timeit('app_left2(lst)', globals=globals(), number=10000))

print('Добавление справа:')
print(timeit('app_right1(dq)', globals=globals(), number=10000))
print(timeit('app_right2(lst)', globals=globals(), number=10000))

print('Выброс слева:')
print(timeit('pop_left1(dq)', globals=globals(), number=10000))
print(timeit('pop_left2(lst)', globals=globals(), number=10000))

print('Выброс справа:')
print(timeit('pop_right1(dq)', globals=globals(), number=10000))
print(timeit('pop_right2(lst)', globals=globals(), number=10000))

print('Расширение слева:')
print(timeit('ext_left1(dq)', globals=globals(), number=10000))
print(timeit('ext_left2(lst)', globals=globals(), number=10000))

print('Расширение справа:')
print(timeit('ext_right1(dq)', globals=globals(), number=10000))
print(timeit('ext_right2(lst)', globals=globals(), number=10000))

'''
Добавление слева:
0.001067000000000002
0.0268104
Добавление справа:
0.0009995999999999963
0.0010893999999999973
Выброс слева:
0.0009783000000000014
0.029682799999999995
Выброс справа:
0.0010228999999999933
0.0010505999999999988
Расширение слева:
0.001866699999999999
0.0014789999999999942
Расширение справа:
0.0017201000000000022
0.001547699999999999

Операции по добавлению/изъятию слева ожидаемо быстрее в десятки раз у дека

'''