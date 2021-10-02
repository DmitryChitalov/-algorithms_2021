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
import timeit

my_list = []
my_deque = deque([])


def app(array):
    return array.append('1')


print('List append', timeit.timeit("app(my_list)", globals=globals(), number=100000))
# от 0.0071005 до 0.0095636
print('Deque append',timeit.timeit('app(my_deque)', globals=globals(), number=100000))
# от 0.0075005 до 0.0080855
print()
"""
В заполнении списка нет однозначного фаворита, хоть в среднем deque заполняется быстрее, чем list, иногда list
заполнялся быстрее, чем deque.
"""


def dq_app_left():
    return my_deque.appendleft("1")


def ls_app_left():
    return my_list.insert(0, '1')


# print('List insert(0,)',timeit.timeit("ls_app_left()", globals=globals(), number=100000))
## от 4.7347473 до 4.7954783
# print('Deque appendleft', timeit.timeit("dq_app_left()", globals=globals(), number=100000))
## от  0.0055680 до 0.00735250
print()


def dq_pop_left():
    return my_deque.popleft()


def ls_pop_left():
    return my_list.pop(0)


# print('List pop(0)',timeit.timeit("ls_pop_left()", globals=globals(), number=100000))
## от 0.8534139 до 0.879123
# print('Deque popleft', timeit.timeit("dq_pop_left()", globals=globals(), number=100000))
## от 0.0055680 до 0.0067514
print()


def dq_extend_left():
    return my_deque.extendleft(['1', '2', '3'])


def ls_extend_left():
    a = ['1', '2', '3']
    for _ in range(len(a)):
        my_list.insert(0, a.pop())
    return my_list


# print('List extendleft',timeit.timeit("ls_extend_left()", globals=globals(), number=100000))
## от 23 секунд
# print('Deque extendleft', timeit.timeit("dq_extend_left()", globals=globals(), number=100000))
## от 0.013111

"""
ВЫВОД: Специализированные методы объекта deque (appendleft, popleft, extendleft) справляются с операциями
гораздо быстрее, чем их в ручную созданные аналоги объекта list. Чем больше элементов хранится в списке, тем дольше 
list обрабатывает операции, с которыми deque справляется гораздо быстрее. Из-за того что в list не предусмотрена вставка 
последователности в начало, эта операция занимает слишко ммного времени, по сравнению с deque. Хотя, возможно, есть более
эффективый способ вставки последовательности в list.Если ситуация требует от нас опертивного использования
элементов из начала и конца списка, а именно добавления, удаления, или вставки другой последовательности, 
для эффективности стоит использовать именно объект deque.
"""
