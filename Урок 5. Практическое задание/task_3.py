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


def fill_list(cnt):
    return list(range(cnt))


def fill_deque(cnt):
    return deque(list(range(cnt)))


def append_left_list(lst: list, elem):
    lst.insert(0, elem)
    return lst


def append_left_deque(deq: deque, elem):
    deq.appendleft(elem)
    return deq


def pop_left_list(lst: list):
    lst.pop(0)
    return lst


def pop_left_deque(deq: deque):
    deq.popleft()
    return deq


def extend_left_list(lst: list, elem):
    lst.reverse()
    lst.extend(elem)
    lst.reverse()
    return lst


def extend_left_deque(deq: deque, elem):
    deq.extendleft(elem)
    return deq


lst = fill_list(10)
deq = fill_deque(10)

print('Work demonstration:')
print(f'List: {lst}')
print(f'Append left list: {append_left_list(lst, 98765)}')
print(f'Pop left list: {pop_left_list(lst)}')
print(f'Extend left list: {extend_left_list(lst, [111, 222, 333, 444, 555])}')

print(f'Deque: {deq}')
print(f'Append left deque: {append_left_deque(deq, 98765)}')
print(f'Pop left deque: {pop_left_deque(deq)}')
print(f'Extend left deque: {extend_left_deque(deq, [111, 222, 333, 444, 555])}')

print('Timing:')
print(f'fill_list(1000):  {timeit("fill_list(1000)", globals=globals(), number=1000)}')
print(f'fill_deque(1000): {timeit("fill_deque(1000)", globals=globals(), number=1000)}')
print(f'append_left_list(lst, 98765):  {timeit("append_left_list(lst, 98765)", globals=globals(), number=1000)}')
print(f'append_left_deque(deq, 98765): {timeit("append_left_deque(deq, 98765)", globals=globals(), number=1000)}')
print(f'pop_left_list(lst):  {timeit("pop_left_list(lst)", globals=globals(), number=1000)}')
print(f'pop_left_deque(deq): {timeit("pop_left_deque(deq)", globals=globals(), number=1000)}')
print(
    f'extend_left_list(lst, [111, 222, 333, 444, 555]):  '
    f'{timeit("extend_left_list(lst, [111, 222, 333, 444, 555])", globals=globals(), number=1000)}')
print(
    f'extend_left_deque(deq, [111, 222, 333, 444, 555]): '
    f'{timeit("extend_left_deque(deq, [111, 222, 333, 444, 555])", globals=globals(), number=1000)}')

"""
Timing:
fill_list(1000):  0.077328867   - Заполнение немного быстрее у списка
fill_deque(1000): 0.08055979200000002
append_left_list(lst, 98765):  0.0008111279999999943   - Добавление элемента слева быстрее у deque
append_left_deque(deq, 98765): 0.00032064599999998
pop_left_list(lst):  0.00047734700000001684   - Удаление элемента слева быстрее у deque
pop_left_deque(deq): 0.00025226000000000415
extend_left_list(lst, [111, 222, 333, 444, 555]):  0.004241323000000019   - Добавление элементов слева быстрее у deque
extend_left_deque(deq, [111, 222, 333, 444, 555]): 0.0005439219999999745
"""