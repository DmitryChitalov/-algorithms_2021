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
import string
from collections import deque

print('Заполнение. list быстрее deque')
print('deque time', timeit("NEW_DEQUE = deque(string.ascii_uppercase)", globals=globals()))
print('list time', timeit("NEW_LIST = list(string.ascii_uppercase)", globals=globals()))
print('---')
NEW_DEQUE = deque(string.ascii_uppercase)
NEW_LIST = list(string.ascii_uppercase)
print('Добавление слева. deque намного быстрее чем list')
print('deque time', timeit("NEW_DEQUE.appendleft('left')", globals=globals(), number=10000))
print('list time', timeit("NEW_LIST.insert(0, 'left')", globals=globals(), number=10000))
print('---')
print('Извлечение слева. deque намного быстрее чем list')
print('deque time', timeit("left = NEW_DEQUE.popleft()", globals=globals(), number=10000))
print('list time', timeit("left = NEW_LIST.pop(0)", globals=globals(), number=10000))
print('---')
print('Включение слева. list быстрее чем deque')
print('deque time', timeit("""
NEW_DEQUE_1 = deque('1234567890')
NEW_DEQUE.extendleft(NEW_DEQUE_1)
""", globals=globals()))
print('list time', timeit("""
NEW_LIST_1 = list('1234567890')
NEW_LIST_1.reverse()
NEW_LIST_1.extend(NEW_LIST)
""", globals=globals()))
