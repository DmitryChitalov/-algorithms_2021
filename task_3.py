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
import timeit


def push_deque():
    for el in range(1001):
        example_deque.appendleft(el)


def pop_deque():
    for el in range(1001):
        example_deque.popleft()


def extend_deque():
    extend_items = [1, 2, 3, 4, 5]
    for _ in range(1001):
        example_deque.extendleft(extend_items)


def push_list():
    for el in range(1001):
        example_list.insert(0, el)


def pop_list():
    for _ in range(1001):
        example_list.pop(0)


def extend_list():
    extend_items = [1, 2, 3, 4, 5]
    for _ in range(1001):
        example_list.extend(extend_items)


def test_deque():
    print(timeit.timeit('push_deque()', globals=globals(), number=100))
    print(timeit.timeit('pop_deque()', globals=globals(), number=100))
    print(timeit.timeit('extend_deque()', globals=globals(), number=100))


def test_list():
    print(timeit.timeit('push_list()', globals=globals(), number=100))
    print(timeit.timeit('pop_list()', globals=globals(), number=100))
    print(timeit.timeit('extend_list()', globals=globals(), number=100))


# Замеры:
# Вставка - collections: 0.004829199999999999, list: 1.9135442999999999
# Удаление - collections: 0.004624400000000001, list: 0.6632072
# Вставка списка - collections: 0.011286000000000004, list: 0.02245440000000043
# Вывод: deque гораздо быстрее list, особенно в вставке (insert довольно медленная функция).


if __name__ == '__main__':
    example_deque, example_list = collections.deque([]), []
    test_deque()
    test_list()
