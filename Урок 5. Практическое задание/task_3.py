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

И добавить аналитику, так ли это или нет!
"""
from collections import deque
from timeit import timeit


deq_obj = deque([])
list_obj = list()


def app_in_deq():
    for el in range(100):
        deq_obj.append(el)


def applef_deq():
    for el in range(100, 130):
        deq_obj.appendleft(el)


def pop_left_deq():
    for el in range(50):
        deq_obj.popleft()


def app_in_list():
    for el in range(100):
        list_obj.append(el)


def app_left_list():
    for el in range(100, 130):
        list_obj.insert(0, el)


def pop_list():
    for el in range(50):
        list_obj.pop(0)


print('app_in_deq\n', timeit("app_in_deq()", 'from __main__ import app_in_deq', number=1000))
print('app_in_list\n', timeit("app_in_list()", globals=globals(),  number=1000))
print()
print('applef_deq\n', timeit("applef_deq()", globals=globals(),  number=1000))
print('app_left_list\n', timeit("app_left_list()", globals=globals(),  number=1000))
print()
print('pop_left_deq\n', timeit("pop_left_deq()", globals=globals(), number=1000))
print('pop_list\n', timeit("pop_list()", globals=globals(), number=1000))


"""
app_in_deq
 0.004905900000000001
app_in_list
 0.006530499999999998

applef_deq
 0.0015674999999999994
app_left_list
 2.0956601

pop_left_deq
 0.002141199999999621
pop_list
 1.1196848

Если нас интеерсуется вставка в начало или удаление из начала массива, то рациональнее использовать дек, 
т.к. appendleft и popleft имеют сложность О(1). В то время как в списке требуется пересчет индексов, 
и сложность будет О(n). Если мы работаем с рандомным элементом массива, то большого выигрыша по времени мы не получим,
смысла в деке нет. Получаем, что информация в документации соответствует дейстивтельности.
"""

