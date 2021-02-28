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
from timeit import timeit

# Взятие элемента по индексу

setup_deque = """
from collections import deque
NEW_DEQUE = deque(range(1000000))
"""
setup_list = """
NEW_LIST = list(range(1000000))
"""

print('Взятие элемента по индексу')
print(f"deque: {timeit('a = NEW_DEQUE[9999]', setup_deque)}")
print(f"list: {timeit('a = NEW_LIST[9999]', setup_list)}")

#  Перемещение элементов

setup_deque = """from collections import deque
NEW_DEQUE = deque(range(1000000))
NEW_DEQUE.rotate(100)
"""
setup_list = """NEW_LIST = list(range(1000000))
for i in range(100):
    NEW_LIST.insert(0, NEW_LIST[-1])
    NEW_LIST.pop(-1)"""

print('\nПермещение элементов с конца в начало')
print(f'deque: {timeit(setup_deque, number=100)}')
print(f'list: {timeit(setup_list, number=100)}')

# Метод append

setup_deque = """
import string
from collections import deque
NEW_DEQUE = deque(range(1000000))
NEW_DEQUE.append('x')
"""
setup_list = """
NEW_LIST = list(range(1000000))
NEW_LIST.append('x')
"""

print('\nМетод append')
print(f'deque: {timeit(setup_deque, number=100)}')
print(f'list: {timeit(setup_list, number=100)}')

# Insert, appendleft

setup_deque = """
from collections import deque
NEW_DEQUE = deque(range(1000000))
NEW_DEQUE.appendleft('x')
"""
setup_list = """
NEW_LIST = list(range(1000000))
NEW_LIST.insert(0, 'x')
"""

print('\nInsert, appendleft')
print(f'deque: {timeit(setup_deque, number=100)}')
print(f'list: {timeit(setup_list, number=100)}')


"""Документация не врёт. Простое взятие элемента по индексу в списке работает значительно быстрее
Добавление слева и справа и, особенно, перемещение из одного конца в другой - быстрее работают в деке"""