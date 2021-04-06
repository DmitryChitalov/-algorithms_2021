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
import random

simple_list = [1, 2, 3, 4, 5, 5]
deq_obj = deque(simple_list)


def add_end_el_lst():
    for i in range(100):
        simple_list.append(i)


def add_end_el_deq():
    for i in range(100):
        deq_obj.append(i)


def add_beg_el_lst():
    for i in range(100):
        simple_list.insert(0, i)


def add_beg_el_deq():
    for i in range(100):
        deq_obj.appendleft(i)


# добавление в конец списка
print('Добавление элемента в конец списка:', end=' ')
print(timeit('simple_list.append(987655)', globals=globals(), number=1000000))  # для одной операции
# print(timeit('add_end_el_lst()', globals=globals(), number=10000))  # для 100 операций

# добавление в конец deque
print('Добавление элемента в конец deque:', end=' ')
print(timeit('deq_obj.append(987655)', globals=globals(), number=1000000))
# print(timeit('add_end_el_deq()', globals=globals(), number=10000))  # для 100 операций

# добавление в начало списка

print('Добавление элемента в начало списка:', end=' ')
print(timeit('simple_list.insert(1, 987655)', globals=globals(), number=100))
# print(timeit('add_beg_el_lst()', globals=globals(), number=1))

print('Добавление элемента в начало deque:', end=' ')
print(timeit('deq_obj.appendleft(str(987655))', globals=globals(), number=100))
# print(timeit('add_beg_el_deq()', globals=globals(), number=1))

# удаление последнего элемента (pop)
print('Удаление последнего  элемента из deque:', end=' ')
print(timeit('deq_obj.pop', 'from __main__ import deq_obj', number=1000000))
print('Удаление последнего  элемента из списка:', end=' ')
print(timeit('simple_list.pop', globals=globals(), number=1000000))

# доступ к случайному элементу

print('Доступ к случайному  элементу из deque:', end=' ')
print(timeit('d = deq_obj[random.randint(0, 100)]', globals=globals(), number=1000))
print('Доступ к случайному  элементу из списка:', end=' ')
print(timeit('s = simple_list[random.randint(0, len(simple_list))]', globals=globals(), number=1000))

print('Реверс deque:', end=' ')
print(timeit('deq_obj.reverse()', globals=globals(), number=100))
print('Реверс  списка:', end=' ')
print(timeit('simple_list.reverse()', globals=globals(), number=100))

"""
Добавление элемента в конец списка: 0.110459069
Добавление элемента в конец deque: 0.10340053399999999
Добавление элемента в начало списка: 0.25380015899999997
Добавление элемента в начало deque: 4.456799999996708e-05
Удаление последнего  элемента из deque: 0.07132246599999997
Удаление последнего  элемента из списка: 0.08425566100000004
Доступ к случайному  элементу из deque: 0.001297942999999968
Доступ к случайному  элементу из списка: 0.0014579410000000737
Реверс deque: 0.11530376999999992
Реверс  списка: 0.09029625600000002

вывод: операции с первым и последним элементами (добавление, удаление) быстрее выполняются для deque
доступ к случайному элементу списка в моем случае получился примерно одинаковым, а операция обращения (реверс) 
для списка быстрее. 



"""