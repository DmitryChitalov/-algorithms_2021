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


from timeit import timeit
from collections import deque

lst = [i for i in range(10000)]
deq = deque(lst)
elem = 10000


def append_left_list(check_list, el):
    check_list.insert(0, el)


def append_left_deque(check_deque, el):
    check_deque.appendleft(el)


def pop_left_list(check_list):
    check_list.pop(0)


def pop_left_deque(check_deque):
    check_deque.popleft()


def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


print('append_left_list: ' + str(timeit('append_left_list(lst, elem)', globals=globals(), number=10000)))
print('append_left_deque: ' + str(timeit('append_left_deque(deq, elem)', globals=globals(), number=10000)) + '\n')

print('pop_left_list: ' + str(timeit('pop_left_list(lst)', globals=globals(), number=10000)))
print('pop_left_deque: ' + str(timeit('pop_left_deque(deq)', globals=globals(), number=10000)) + '\n')

print('pop_list: ' + str(timeit('pop_list(lst)', globals=globals(), number=10000)))
print('pop_deque: ' + str(timeit('pop_deque(deq)', globals=globals(), number=10000)))


"""
Добавление елемента в начало - очередь быстрее
Удаление первого элемента - очередь быстрее
Удаление последнего элемента - одинаково
"""
