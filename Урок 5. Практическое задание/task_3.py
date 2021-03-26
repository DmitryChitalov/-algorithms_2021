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

from collections import deque
from timeit import timeit


def chek_time(f):
    return timeit(f"{f}", globals=globals(), number=100000)


t_lst = [i for i in range(10000)]
t_dq = deque([i for i in range(10000)])

print("Добавляем в конец list:", chek_time("t_lst.append(0)"))
print("Добавляем в конец deque:", chek_time("t_dq.append(0)"))
print("Добавляем в начало list:", chek_time("t_lst.insert(0,0)"))
print("Добавляем в начало deque:", chek_time("t_dq.appendleft(0)"))
print("Извлекаем из конца list:", chek_time("t_lst.pop()"))
print("Извлекаем из конца deque:", chek_time("t_dq.pop()"))
print("Извлекаем из начала list:", chek_time("t_lst.pop(0)"))
print("Извлекаем из начала deque:", chek_time("t_dq.popleft()"))

"""
Аналитика:
Deque выполяет быстрее операции, использующие начало коллекции.
Различий в скорости работы операций с концом коллекции у Deque и List - нет. 
"""
