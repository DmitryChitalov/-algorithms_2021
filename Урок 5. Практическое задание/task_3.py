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

simple_list = [el for el in range(100)]
deque_list = deque([el for el in range(100)])

copy_simple_list = simple_list.copy()
copy_deque_list = deque(deque_list)

print(f'{"~"*40}Time for creating{"~"*40}\n'
      f'Simple list: {timeit("simple_list", globals=globals(), number=10)}\n'
      f'Deque list: {timeit("deque_list", globals=globals(), number=10)}\n'
      f'\n{"~"*40}Time for operating{"~"*40}\n'
      f'Insert to simple list: {timeit("copy_simple_list.insert(0, 1)", globals=globals(), number=10)}\n'
      f'Insert to deque list: {timeit("copy_deque_list.appendleft(1)", globals=globals(), number=10)}\n'
      f'Pop from simple list: {timeit("copy_simple_list.pop(0)", globals=globals(), number=10)}\n'
      f'Pop from deque list: {timeit("copy_deque_list.popleft()", globals=globals(), number=10)}\n'
      f'Insert to end simple list: '
      f'{timeit("copy_simple_list.extend(copy_simple_list)", globals=globals(), number=10)}\n'
      f'Insert to end deque list: '
      f'{timeit("copy_deque_list.extend(copy_deque_list)", globals=globals(), number=10)}\n'
      f'Insert simple list: {timeit("copy_simple_list.insert(0, copy_simple_list)", globals=globals(), number=10)}\n'
      f'Insert deque list: {timeit("copy_deque_list.extendleft(copy_deque_list)", globals=globals(), number=10)}\n')

"""
Заполнение: 
Заполнение списка происходит быстрее, чем очереди многократно. 
      Simple list: 1.6530000266357092e-06
      Deque list: 6.020000000717118e-07

Действия со списком и очередью: (Для чистоты работа с копиями сгенерированных очереди и списка)
Вставка единичного элемента в начало списка происходит дольше, чем вставка в очередь
      Insert to simple list: 2.525000127207022e-06
      Insert to deque list: 1.7840000055002747e-06
      
Удаление первого элемента через popleft происходит быстрее, чем через pop с указанием индекса первого элемента
      Pop from simple list: 2.795000000332948e-06
      Pop from deque list: 2.0129999711571145e-06

Вставка в конец через extend в обоих случаях прошла быстро
      Insert to end simple list: 0.0005052530000284605
      Insert to end deque list: 0.0012414679999892542
      
Для замера вставки элементов в начало списка пришлось воспользоваться insert, т.к у методов extend и append списка нет
возможности указать начальный индекс. 
В данном случае, insert отработал быстрее, чем extendleft у deque 
      Insert simple list: 0.00046510300001045835
      Insert deque list: 1.8120082780000075
      
Основной вывод:
Deque полезна только в том случае, если нужно работать с элементами в начале или конце очереди. 
Плюсом, дополнительные возможности в виде reverse() и rotate(). Через Deque отлично можно реализвоать Kanban 
и похожие задачи, в остальном лучше использовать list. 
"""
