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

my_deque = deque(range(1, 100000))
my_list = list(range(1, 100000))
new_list = ['qwer']


def app_list(my_list):
    my_list.insert(0, 5)
    return my_list


print('app_list')
print(timeit("app_list(my_list)", "from __main__ import app_list, my_list", number=100000))


def app_deque(my_deque):
    my_deque.appendleft(5)
    return my_deque


print('app_deque')
print(timeit("app_deque(my_deque)", "from __main__ import app_deque, my_deque", number=100000))


def pop_list(my_list):
    my_list.pop(0)
    return my_list


print('pop_list')
print(timeit("pop_list(my_list)", "from __main__ import pop_list, my_list", number=100000))


def pop_deque(my_deque):
    my_deque.popleft()
    return my_deque


print('pop_deque')
print(timeit("pop_deque(my_deque)", "from __main__ import pop_deque, my_deque", number=100000))


def ext_list(my_list):
    my_list = new_list + my_list
    return my_list


print('ext_list')
print(timeit("ext_list(my_list)", "from __main__ import ext_list, my_list", number=100000))


def ext_deque(my_deque):
    my_deque.extendleft(new_list)
    return my_deque


print('ext_deque')
print(timeit("ext_deque(my_deque)", "from __main__ import ext_deque, my_deque", number=100000))

'''
 При добавление элементов deque обладает большей скоростью за счет метода appendleft
 При удалении элементов deque в начале списка через индекс медленнее чем метод очереди popleft
 При добавлении элементов с другого списка метод extendleft работает быстрее
 Благодаря методам которыми обладает deque в определенных задачах можно сильно ускорить процесс
'''
#app_list
#11.915838
#app_deque
#0.020406099999998872
#pop_list
#4.788198099999999
#pop_deque
#0.012374900000001077
#ext_list
#108.1519635
#ext_deque
#0.01503449999999873
