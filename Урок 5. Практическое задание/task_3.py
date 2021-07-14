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

my_list = [i for i in range(100)]
my_deque = deque([i for i in range(100)])

# Заполнение
print('my_list ', timeit('my_list = [i for i in range(100)]', globals=globals(), number=100000))
print('my_deque ', timeit('my_deque = deque([i for i in range(100)])', globals=globals(), number=100000))
'''
my_list  0.4248206 my_deque  0.4772226
Список заполняется быстрее.
'''

# appendleft, popleft, extendleft дека и для их аналоги у списка
my_list.insert(0, 11)
my_deque.appendleft(11)
print('my_list ', timeit('my_list.insert(0,11)', globals=globals(), number=100000))
print('my_deque ', timeit('my_deque.appendleft(11)', globals=globals(), number=100000))

'''
my_list  2.3169739999999996 my_deque  0.0039037999999997908
'''

my_list.pop(0)
my_deque.popleft()
print('my_list ', timeit('my_list.pop(0)', globals=globals(), number=100000))
print('my_deque ', timeit('my_deque.popleft()', globals=globals(), number=100000))

'''
my_list  0.8048216999999998 my_deque  0.006398299999999857
'''


# не нашла аналога для extendleft в обычном списке
def extendleft_for_list(lst):
    my_list.reverse()
    my_list.extend(lst)
    my_list.reverse()


my_deque.extendleft([1, 20, 30])
print('my_list ', timeit('extendleft_for_list([1, 20, 30])', globals=globals(), number=100000))
print('my_deque ', timeit('my_deque.extendleft([1, 20, 30])', globals=globals(), number=100000))

'''
my_list  10.2898358
my_deque  0.010224599999999029
'''

'''
Операции с обычным списком выполняются дольше, чем с deque.
'''
