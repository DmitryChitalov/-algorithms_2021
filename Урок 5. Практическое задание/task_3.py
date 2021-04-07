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
import timeit


def append_list(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def append_deque(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def append_left_list(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def append_left_deque(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def pop_list(lis):
    for i in range(len(lis)):
        lis.pop()


def pop_left_list(lis):
    for i in range(len(lis)):
        lis.pop(0)


def pop_deque(deq):
    for i in range(len(deq)):
        deq.pop()


def pop_left_deque(deq):
    for i in range(len(deq)):
        deq.popleft()


def reverse_deque(deq):
    deq.reverse()


def reverse_list(lis):
    lis.reverse()


num_time = 1000
my_list = [el for el in range(num_time)]
my_deque = deque(my_list)
append_list(num_time)
append_deque(num_time)
append_left_list(num_time)
append_left_deque(num_time)
pop_deque(my_deque)
pop_left_deque(my_deque)
pop_list(my_list)
pop_left_list(my_list)
reverse_list(my_list)
reverse_deque(my_deque)

print('\n================', num_time, '==============\n'
                                      '=================== ВСТАВКА =================')
print("append_list:",
      timeit.timeit("append_list(num_time)", globals=globals(), number=10000))
print("append_deque:",
      timeit.timeit("append_deque(num_time)", globals=globals(), number=10000))
print("append_left_list:",
      timeit.timeit("append_left_list(num_time)", globals=globals(), number=10000))
print("append_left_deque:",
      timeit.timeit("append_left_deque(num_time)", globals=globals(), number=10000))
print('=================== ВЫРЕЗКА =================')
print("pop_list:",
      timeit.timeit("pop_list(my_list)", globals=globals(), number=10000))
print("pop_deque:",
      timeit.timeit("pop_deque(my_deque)", globals=globals(), number=10000))
print("pop_left_list:",
      timeit.timeit("pop_left_list(my_list)", globals=globals(), number=10000))
print("pop_left_deque:",
      timeit.timeit("pop_left_deque(my_deque)", globals=globals(), number=10000))
print('=================== РЕВЕРС =================')
print("reverse_list:",
      timeit.timeit("reverse_list(my_list)", globals=globals(), number=10000))
print("reverse_deque:",
      timeit.timeit("reverse_deque(my_deque)", globals=globals(), number=10000))

num_time = 10000
my_list = [el for el in range(num_time)]
my_deque = deque(my_list)
append_list(num_time)
append_deque(num_time)
append_left_list(num_time)
append_left_deque(num_time)
pop_deque(my_deque)
pop_left_deque(my_deque)
pop_list(my_list)
pop_left_list(my_list)
reverse_list(my_list)
reverse_deque(my_deque)
print('\n================', num_time, '==============\n'
                                      '=================== ВСТАВКА =================')
print("append_list:",
      timeit.timeit("append_list(num_time)", globals=globals(), number=10000))
print("append_deque:",
      timeit.timeit("append_deque(num_time)", globals=globals(), number=10000))
print("append_left_list:",
      timeit.timeit("append_left_list(num_time)", globals=globals(), number=10000))
print("append_left_deque:",
      timeit.timeit("append_left_deque(num_time)", globals=globals(), number=10000))
print('=================== ВЫРЕЗКА =================')
print("pop_list:",
      timeit.timeit("pop_list(my_list)", globals=globals(), number=10000))
print("pop_deque:",
      timeit.timeit("pop_deque(my_deque)", globals=globals(), number=10000))
print("pop_left_list:",
      timeit.timeit("pop_left_list(my_list)", globals=globals(), number=10000))
print("pop_left_deque:",
      timeit.timeit("pop_left_deque(my_deque)", globals=globals(), number=10000))
print('=================== РЕВЕРС =================')
print("reverse_list:",
      timeit.timeit("reverse_list(my_list)", globals=globals(), number=10000))
print("reverse_deque:",
      timeit.timeit("reverse_deque(my_deque)", globals=globals(), number=10000))

"""
Результат выполнения на моей машине

================ 1000 ==============
=================== ВСТАВКА =================
append_list: 0.4310349
append_deque: 0.35798329999999995             тут видим небольшой перекос в пользу DEQUE
append_left_list: 1.6831570999999999
append_left_deque: 0.35241149999999966         тут видим перекос в пользу DEQUE
=================== ВЫРЕЗКА =================
pop_list: 0.0014248000000001149
pop_deque: 0.001489900000000155
pop_left_list: 0.0014236999999996947
pop_left_deque: 0.0013768999999999032
=================== РЕВЕРС =================
reverse_list: 0.0007862999999996845
reverse_deque: 0.0007457999999997966

================ 10000 ==============
=================== ВСТАВКА =================
append_list: 3.7507195999999996
append_deque: 3.8265601
append_left_list: 131.0005852          тут видим сильный перекос в пользу DEQUE
append_left_deque: 4.06654309999999
=================== ВЫРЕЗКА =================
pop_list: 0.0020390999999904125
pop_deque: 0.0020968000000038955
pop_left_list: 0.0022178000000110387
pop_left_deque: 0.0024879999999996016
=================== РЕВЕРС =================
reverse_list: 0.0010883999999862226
reverse_deque: 0.0008531000000004951    тут видим сильный перекос в пользу DEQUE

очередь намного лучше себя показала в операции добавления элемента в начало
и реверсе на больших массивах
"""
