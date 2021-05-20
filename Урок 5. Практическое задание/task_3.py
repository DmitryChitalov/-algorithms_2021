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
from random import randint
from timeit import timeit

some_list = [i for i in range(10000)]
some_deque = deque(some_list)

def list_fill_start():
    """Создает список и добавляет элементы в начало списка"""
    s_list = []
    for i in range(10000):
        s_list.insert(0, i)
    return s_list

def deque_fill_start():
    """Создает очередь и добавляет элементы в начало очереди"""
    s_deque = deque()
    for i in range(10000):
        s_deque.appendleft(i)
    return s_deque

def list_fill_end():
    """Создает список и добавляет элементы в конец списка"""
    e_list = []
    for i in range(10000):
        e_list.append(i)
    return e_list

def deque_fill_end():
    """Создает очередь и добавляет элементы в начало очереди"""
    e_deque = deque()
    for i in range(10000):
        e_deque.append(i)
    return e_deque

def list_change(list_obj):
    for i in range(5000):
        list_obj[randint(1, 9000)] = randint(0, 200)
    return list_obj

def deque_change(deque_obj):
    for i in range(5000):
        deque_obj[randint(1, 9000)] = randint(0, 200)
    return deque_obj


if __name__ == '__main__':
    # Измеряем время заполнения списка и очереди с начала
    time_fill_list = timeit('list_fill_start()', globals=globals(), number=10)
    time_fill_deque = timeit('deque_fill_start()', globals=globals(), number=10)

    print(f'Время заполнения списка с добавлением в начало: {time_fill_list}')
    print(f'Время заполнения очереди с добавлением в начало: {time_fill_list}')
    print('=' * 100)

    # Измеряем время заполнения списка и очереди с конца    
    time_fill_list = timeit('list_fill_end()', globals=globals(), number=10)
    time_fill_deque = timeit('deque_fill_end()', globals=globals(), number=10)

    print(f'Время заполнения списка с добавлением в конец: {time_fill_list}')
    print(f'Время заполнения очереди с добавлением в конец: {time_fill_list}')
    print('=' * 100)

    """
    Наполнение списка и очереди происходит за равное время,
    независимо добавляется элемент в начало или в конец.
    """

    # Измеряем время изменения списка и очереди (вставка элементов в начало)
    time_chg_list = timeit('list_change(some_list)', globals=globals(), number=100)
    time_chg_deque = timeit('deque_change(some_deque)', globals=globals(), number=100)

    print(f'Время изменения списка: {time_chg_list}')
    print(f'Время изменения очереди: {time_chg_deque}')
    print('=' * 100)

    """
    Время изменения очереди несколько больше по сравнению с изменением списка.
    """

