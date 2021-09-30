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
from timeit import default_timer
from collections import deque

EXT = 100  # константа для extended
NUMBER = 1000
obj_list = list()
obj_deque = deque()


def measure(cnt):
    def time_it(func):
        def wrapper(arg):
            start = default_timer()
            tmp = arg
            for i in range(cnt):
                res = func(tmp)
            runtime = default_timer() - start
            print(f'{func.__name__:<15s} {runtime:10.5f}')
            return res

        return wrapper

    return time_it


@measure(NUMBER)
def list_appendleft(obj: list):
    for i in range(EXT):
        obj.insert(0, i)
    return obj


@measure(NUMBER)
def list_popleft(obj: list):
    while obj:
        obj.pop(0)


@measure(NUMBER)
def list_extendleft(obj: list):
    to_insert = (i for i in range(EXT))
    for i in to_insert:
        obj.insert(0, i)
    return obj


@measure(NUMBER)
def deque_appendleft(obj: deque):
    for i in range(EXT):
        obj.appendleft(i)
    return obj


@measure(NUMBER)
def deque_popleft(obj: deque):
    while obj:
        obj.popleft()


@measure(NUMBER)
def deque_extendleft(obj: deque):
    to_extend = (i for i in range(EXT))
    obj.extendleft(to_extend)
    return obj


if __name__ == '__main__':
    tmp = list_appendleft(obj_list)
    list_popleft(tmp)
    list_extendleft(tmp)

    tmp = deque_appendleft(obj_deque)
    deque_popleft(tmp)
    deque_extendleft(tmp)


'''
list_appendleft    5.69510
list_popleft      13.00844
list_extendleft    5.73981
deque_appendleft    0.01464
deque_popleft      0.01182
deque_extendleft    0.01216

выводы:
1. стандартные append, pop, extend не замерялись, скорее всего их скорости сопоставимы
2. на операциях left* объекты типа deque() от 2 до 3 порядков превосходят операции с 
типом данных list()
3. 2-3 порядка - это СУЩЕСТВЕННЫЙ ПРИРОСТ ПРОИЗВОДИТЕЛЬНОСТИ
'''
