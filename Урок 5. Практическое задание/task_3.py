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
from collections import deque

number_cycles = 100000    # количество циклов
list_obj = []
deque_obj = deque([])


def fill_list():    # заполнить обычный массив
    list_obj = [i for i in range(1000)]
    return list_obj


def fill_deque():    # заполнить контейнер deque
    deque_obj = [j for j in range(1000)]
    return deque_obj


def add_list():    # добавим элемент в массив
    list_obj.insert(0, 1)
    return list_obj


def add_deque():    # добим элемент в deque контейнер
    deque_obj.appendleft(1)
    return deque_obj


def del_list():    # удалим элемент 0 позиции
    list_obj.pop(0)
    return list_obj


def del_deque():    # удалим элемент слева
    deque_obj.popleft()
    return deque_obj


print(f'Заполнение массива: '
      f'{timeit("fill_list()", globals=globals(), number=number_cycles)}')    # 5.258377099991776
print(f'Заполнение контейнера: '
      f'{timeit("fill_deque()", globals=globals(), number=number_cycles)}')    # 5.306759900006
print(f'Добавление элемента в массив: '
      f'{timeit("add_list()", globals=globals(), number=number_cycles)}')    # 4.352013099996839
print(f'Добавление элемента в контейнер: '
      f'{timeit("add_deque()", globals=globals(), number=number_cycles)}')    # 0.02476639999076724
print(f'Удаление элемента из массива: '
      f'{timeit("del_list()", globals=globals(), number=number_cycles)}')    # 1.4185422000009567
print(f'Удаление элемента из контейнера: '
      f'{timeit("del_deque()", globals=globals(), number=number_cycles)}')    # 0.02342400001361966


"""В данном случае видно, что используя модуль deque,
работа с массивами происходит гораздо быстрее, чем стандартными методами.
лишь заполнение массива примерно одинаково по времени (и там и там LC используется)"""
