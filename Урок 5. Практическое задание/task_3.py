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

number_call = 100

my_lst = []
my_deq = deque()

"""Создание и наполнение списка"""
create_time_lst = timeit('my_lst = [i for i in range(1000)]', number=number_call, globals=globals())
create_time_deq = timeit('my_deq = deque(i for i in range(1000))', number=number_call, globals=globals())


"""Добавление в начало списка"""
left_app_lst = timeit('for i in reversed(range(1000, 0, -1)):\
    my_lst.insert(0, i)', number=number_call, globals=globals())
left_app_deq = timeit('for i in reversed(range(1000, 0, -1)):\
    my_deq.appendleft(i)', number=number_call, globals=globals())


"""Удаление с начала списка"""
left_pop_lst = timeit('for i in range(1000):\
    my_lst.pop(0)', number=number_call, globals=globals())
left_pop_deq = timeit('for i in range(1000):\
    my_deq.popleft()', number=number_call, globals=globals())


"""Расширение списка"""
exten_slt = timeit('my_lst = [i for i in range(1000)]', number=number_call, globals=globals())
exten_deq = timeit('my_deq.extendleft(reversed(range(1000, 0, -1)))', number=number_call, globals=globals())


print(f'Создание и наполнение обычного списка: {create_time_lst}\n'
      f'Создание и наполнения очереди (deque): {create_time_deq}\n'
      f'**********************************************\n'
      f'Добавление в начало списка: {left_app_lst}\n'
      f'Добавление в начало deque: {left_app_deq}\n'
      f'**********************************************\n'
      f'Удаление с начала списка: {left_pop_lst}\n'
      f'Удаление с начала deque: {left_pop_deq}\n'
      f'**********************************************\n'
      f'Расширение списка: {exten_slt}\n'
      f'Расширение deque: {exten_deq}')

'''
Операция наполнения списка происходит для list быстрее почти в 2 раза, а вот другие операции добавения, удаления,
расширения значительно быстрее выполяются в deque.

Создание и наполнение обычного списка: 0.0024635999999999963
Создание и наполнения очереди (deque): 0.004579399999999997
**********************************************
Добавление в начало списка: 2.6744369
Добавление в начало deque: 0.005488399999999949
**********************************************
Удаление с начала списка: 0.9208992
Удаление с начала deque: 0.005164799999999747
**********************************************
Расширение списка: 0.002256899999999895
Расширение deque: 0.0014283999999999963
'''