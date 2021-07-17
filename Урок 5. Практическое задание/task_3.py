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


def extendleft_list():
    for index in extend_list:
        sample_list.insert(0, index)


def start_timeit(desc, deque_func, list_func, repeat_value):
    print(f'Замер для функции {desc}:\n'
          f'DEQUE: {timeit(deque_func, globals=globals(), number=repeat_value)}\n'
          f'LIST: {timeit(list_func, globals=globals(), number=repeat_value)}\n')


sample_list = [index for index in range(100)]
sample_deque = deque(sample_list)
extend_list = [len(sample_list) + index for index in range(10)]

start_timeit('appendleft', 'sample_deque.appendleft(1)', 'sample_list.insert(0,1)', 100000)
start_timeit('popleft', 'sample_deque.popleft()', 'sample_list.pop(0)', 100000)
start_timeit('extendleft', 'sample_deque.extendleft(extend_list)', 'extendleft_list()', 10000)

# Встроенные функции:
start_timeit('append', 'sample_deque.append(100)', 'sample_list.append(100)', 100000)
start_timeit('count', 'sample_deque.count(100)', 'sample_list.count(100)', 1000)
start_timeit('copy', 'sample_deque.copy()', 'sample_list.copy()', 1000)
start_timeit('reverse', 'sample_deque.reverse()', 'sample_list.reverse()', 10000)
start_timeit('clear', 'sample_deque.clear()', 'sample_list.clear()', 100000)

"""
Результаты замеров. Как и говорится в документации, deque лучше использовать, когда необходимо выполнить быстрые операции
для начала списка (добавить, удалить, расширить начало списка), все остальные (стандартные) функции работают на списках
кратно быстрее, на некоторых (например копирование или переворот) замечается замедление в х2 раза.

Замер для функции appendleft:
DEQUE: 0.0047723
LIST: 1.7979942

Замер для функции popleft:
DEQUE: 0.006290499999999977
LIST: 0.9168669

Замер для функции extendleft:
DEQUE: 0.00145660000000003
LIST: 1.7845771000000004

Замер для функции append:
DEQUE: 0.004595899999999986
LIST: 0.006454200000000299

Замер для функции count:
DEQUE: 1.2867816999999997
LIST: 0.9134903999999997

Замер для функции copy:
DEQUE: 1.9750294999999998
LIST: 1.0869406999999995

Замер для функции reverse:
DEQUE: 11.696242199999999
LIST: 6.838313599999999

Замер для функции clear:
DEQUE: 0.004647100000003235
LIST: 0.003777799999998166

"""
