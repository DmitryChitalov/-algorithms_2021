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

test_list = []
test_deque = deque()
lst_nums = [-10, 20, 3, 4, 5, 6, 7]


def app_list(n):
    test_list = []
    for i in range(len(n)):
        test_list.append(i)


def app_deque(n):
    test_deque = deque()
    for i in range(len(n)):
        test_deque.append(i)


print(timeit('app_list(lst_nums)', globals=globals()))
print(timeit('app_deque(lst_nums)', globals=globals()))
'''
Добавление в деку выполняется соизмеримо добавлению в список
'''


def insert_list(n):
    test_list = []
    for i in range(len(n)):
        test_list.insert(0, i)


def app_left_deque(n):
    test_deque = deque()
    for i in range(len(n)):
        test_deque.appendleft(i)


print(timeit('insert_list(lst_nums)', globals=globals()))
print(timeit('app_left_deque(lst_nums)', globals=globals()))

'''
Операция appendleft в деке выполняется быстрее операции insert в списке
'''


def pop_list():
    n = [-10, 20, 3, 4, 5, 6, 7]
    n.pop()


def pop_deque():
    n = deque(lst_nums)
    n.pop()


def pop_list_0():
    n = [-10, 20, 3, 4, 5, 6, 7]
    n.pop(0)


def pop_deque_0():
    n = deque(lst_nums)
    n.popleft()


print(timeit('pop_list()', globals=globals()))
print(timeit('pop_deque()', globals=globals()))
print(timeit('pop_list_0()', globals=globals()))
print(timeit('pop_deque_0()', globals=globals()))

'''
Удаление первого и последнего элемента быстрее в деке
'''


def extend_list():
    n = [-10, 20, 3, 4, 5, 6, 7]
    n.extend([3, 2, 1])


def extend_deque():
    n = deque(lst_nums)
    n.extendleft([3, 2, 1])


print(timeit('extend_list()', globals=globals()))
print(timeit('extend_deque()', globals=globals()))

'''
Метод расширения списка через extend занимает меньше времени чем расширение деки.
Использование списка тут целесообразней
'''