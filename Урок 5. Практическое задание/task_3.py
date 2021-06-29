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

lists = []
deque_lists = deque([])


def insert_list(numb, new_list):
    for i in range(numb):
        new_list.insert(0, i)
        return new_list


def appendleft_deque(numb, new_deque_list):
    for i in range(numb):
        new_deque_list.appendleft(i)
        return new_deque_list


def pop_list(numb, new_list):
    for i in range(numb):
        new_list.pop()
        return new_list


def pop_deque(numb, new_deque_list):
    for i in range(numb):
        new_deque_list.popleft()
        return new_deque_list


def append_list(numb, new_list):
    for i in range(numb):
        new_list.append(i)
        return new_list


def append_deque(numb, new_deque_list):
    for i in range(numb):
        new_deque_list.append(i)
        return new_deque_list


def reverse_list(new_list):
    return new_list[::-1]


def reverse_deque(new_deque_list):
    return new_deque_list.reverse()


print(f"Время работы функции {appendleft_deque.__name__} составило "
      f"{timeit('insert_list(100000, lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {insert_list.__name__} составило "
      f"{timeit('appendleft_deque(100000, deque_lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {pop_list.__name__} составило "
      f"{timeit('pop_list(80000, lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {pop_deque.__name__} составило "
      f"{timeit('pop_deque(80000, deque_lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {append_list.__name__} составило "
      f"{timeit('append_list(100000, lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {append_deque.__name__} составило "
      f"{timeit('append_deque(100000, deque_lists)', globals=globals(), number=100000)} сек.")

print(f"Время работы функции {reverse_list.__name__} составило "
      f"{timeit('reverse_list(lists)', globals=globals(), number=10000)} сек.")

print(f"Время работы функции {reverse_deque.__name__} составило "
      f"{timeit('reverse_deque(deque_lists)', globals=globals(), number=10000)} сек.")

"""
Отчет teimeit:
Время работы функции appendleft_deque составило 9.2882043 сек.
Время работы функции insert_list составило 0.10372669999999928 сек.
Время работы функции pop_list составило 0.10164280000000048 сек.
Время работы функции pop_deque составило 0.1138659999999998 сек.
Время работы функции append_list составило 0.10319720000000032 сек.
Время работы функции append_deque составило 0.10816499999999962 сек.
Время работы функции reverse_list составило 11.114633199999998 сек.
Время работы функции reverse_deque составило 2.5829828 сек.
Исходя из отчета модуля timeit, видно, что при втавке знначений в начала списка с deque, очень большое время вставки -
9.2882043 сек, а у простых списков, эта операция заняла всего 0.10372669999999928 сек. Хотя вставки в конец списка, 
разнца совсем не значительная.
Но зато по реверсу списка наоборот выигрыает deque почти в 5 раз, по сравнению со спискам.
В целом по всем остальным операциям, разница не значительна. 
Вывод: для вставки значений В НАЧАЛА СПИСКА лучше работать со списками,а вот если надо сделать реверс списка, то лучше
deque...
"""
