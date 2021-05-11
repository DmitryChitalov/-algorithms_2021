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
import string
from collections import deque
from timeit import timeit
from random import random


def get_deque():
    return deque(string.ascii_uppercase)


def deque_append(some_deque, val='end'):
    some_deque.append(val)
    return some_deque


def deque_append_left(some_deque, val='start'):
    some_deque.appendleft(val)
    return some_deque


def deque_rotate_from_begin(some_deque, moving_elements=3):
    some_deque.rotate(-moving_elements)
    return some_deque


def deque_rotate_from_end(some_deque, moving_elements=3):
    some_deque.rotate(moving_elements)
    return some_deque


def deque_pop_left(some_deque):
    return some_deque.popleft()


def deque_pop_right(some_deque):
    return some_deque.pop()


def deque_random_el(some_deque):
    return some_deque[round(random() * len(string.ascii_uppercase)) - 1]


# ------------------------------------------


def get_list():
    return [string.ascii_uppercase]


def list_append(some_list, val='end'):
    some_list.append(val)
    return some_list


def list_append_left(some_list, val='start'):
    some_list.insert(0, val)
    return some_list


def list_rotate_from_begin(some_list, moving_elements=3):
    return some_list[moving_elements:len(some_list)] + some_list[:moving_elements]


def list_rotate_from_end(some_list, moving_elements=3):
    return some_list[len(some_list) - moving_elements:len(some_list)] + some_list[:len(some_list) - moving_elements]


def list_pop_left(some_list):
    return some_list.pop(0)


def list_pop_right(some_list):
    return some_list.pop()


def list_random_el(some_list):
    return some_list[round(random() * len(some_list)) - 1]


explore_list = get_list()

explore_deque = get_deque()

deque_functions = ('get_deque()',
                   'deque_append(explore_deque)',
                   'deque_append_left(explore_deque)',
                   'deque_rotate_from_begin(explore_deque)',
                   'deque_rotate_from_end(explore_deque)',
                   'deque_pop_left(explore_deque)',
                   'deque_pop_right(explore_deque)',
                   'deque_random_el(explore_deque)')

list_functions = ('get_list()',
                  'list_append(explore_list)',
                  'list_append_left(explore_list)',
                  'list_rotate_from_begin(explore_list)',
                  'list_rotate_from_end(explore_list)',
                  'list_pop_left(explore_list)',
                  'list_pop_right(explore_list)',
                  'list_random_el(explore_list)')


for function in deque_functions:
    print(f'{function}:', round(timeit(f'{function}', globals=globals(), number=10000), 5), 'sec')

print('\n')

for function in list_functions:
    print(f'{function}:', round(timeit(f'{function}', globals=globals(), number=10000), 5), 'sec')


# Создание списков происходит быстрее на основе имеющегося итерирующего объекта в сравнении с деком.
# Операции добавления/удаления элемента с конца происходят прмерно одинаково, с начала дек обрабатывает быстрее
# По перемещению нескольких элементов с один конец в другой дек насомненный лидер
# По поиску рандомного элемента по индексу лучше справляется список, но незначительно

# get_deque(): 0.01273 sec                                        get_list(): 0.00279 sec
# deque_append(explore_deque): 0.00408 sec                        list_append(explore_list): 0.00391 sec
# deque_append_left(explore_deque): 0.00448 sec                   list_append_left(explore_list): 0.14436 sec
# deque_rotate_from_begin(explore_deque): 0.00472 sec             list_rotate_from_begin(explore_list): 3.84989 sec
# deque_rotate_from_end(explore_deque): 0.00535 sec               list_rotate_from_end(explore_list): 3.83353 sec
# deque_pop_left(explore_deque): 0.00382 sec                      list_pop_left(explore_list): 0.03214 sec
# deque_pop_right(explore_deque): 0.00404 sec                     list_pop_right(explore_list): 0.00272 sec
# deque_random_el(explore_deque): 0.01086 sec                     list_random_el(explore_list): 0.00893 sec

