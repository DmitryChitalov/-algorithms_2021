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


from timeit import timeit
from collections import deque


def my_func_deque_1(n=100):
    for i in range(n):
        deq_obj.appendleft('a')


def my_func_deque_2(n=100):
    for i in range(n):
        deq_obj.popleft()


def my_func_deque_3(n=100):
    for i in my_gen:
        deq_obj.extendleft(my_gen)


def my_func_list_1(n=100):
    for i in range(n):
        list_obj.insert(0, 'a')


def my_func_list_2(n=100):
    for i in range(n):
        list_obj.pop(0)


def my_func_list_3(n=100):
    for i in range(len(my_gen)-1, -1, -1):
        list_obj.insert(0, my_gen[i])


simple_lst = []
my_gen = [str(i) for i in range(100)]
deq_obj = deque(simple_lst)
list_obj = []
print(f'Сравнение appendleft("a") и insert(0, "a")\n'
      f'appendleft("a"): {timeit("my_func_deque_1()", globals=globals(), number=1000)}'
      f' vs ' 
      f'insert(0, "a"): {timeit("my_func_list_1()", globals=globals(), number=1000)}\n')

print(f'Сравнение deq_obj.popleft() и list_obj.pop(0)\n'
      f'popleft(): {timeit("my_func_deque_2()", globals=globals(), number=1000)}'
      f' vs ' 
      f'pop(0): {timeit("my_func_list_2()", globals=globals(), number=1000)}\n')

print(f'Сравнение deq_obj.extendleft(my_gen) и list_obj.insert(0, my_gen[i]) reverse\n'
      f'extendleft(my_gen): {timeit("my_func_deque_3()", globals=globals(), number=1000)}'
      f' vs ' 
      f'insert(0, my_gen[i]) reverse: {timeit("my_func_list_3()", globals=globals(), number=1000)}\n')

"""
Аналитика:
Сравнение appendleft("a") и insert(0, "a")
appendleft("a"): 0.027140899999999996 vs insert(0, "a"): 7.5443498

Сравнение deq_obj.popleft() и list_obj.pop(0)
popleft(): 0.020905299999999905 vs pop(0): 3.4002418999999993

Сравнение deq_obj.extendleft(my_gen) и list_obj.insert(0, my_gen[i]) reverse
extendleft(my_gen): 0.38004510000000025 vs insert(0, my_gen[i]) reverse: 7.104012900000001


deque на порядки быстрее при работе с функциями appendleft, popleft, extendleft, чем list с аналогичными функциями
"""
