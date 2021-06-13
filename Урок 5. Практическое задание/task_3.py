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

#Заполнение списка и deque-списка
list_1 = []
deque_1 =deque([])

def fun_append(deqlist):
    for el in range(1000):
        deqlist.append(el)
    return list

time_1 = timeit("fun_append(list_1)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_1}')

time_2 = timeit("fun_append(deque_1)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_2}')

print(f'Относительная разница во времени составляет: {(time_1-time_2)/time_1*100} %')

#Время замера составило: 1.2275165
#Время замера составило: 0.8026691000000001
#Относительная разница во времени составляет: 34.61032092032978 %

#Заполнение списка с помощью insert() и deque-списка с помощью appendleft()
list_2= []
deque_2 =deque([])

def fun_appendleft(deq):
    for el in range(100):
        deq.appendleft(el)
    return deq


def fun_insert(list):
    for el in range(100):
        list.insert(0, el)
    return list

time_3 = timeit("fun_appendleft(deque_2)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_3}')
time_4 = timeit("fun_insert(list_2)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_4}')

print(f'Относительная разница во времени составляет: {(time_3-time_4)/time_3*100} %')

#Время замера составило: 0.06442380000000014
#Время замера составило: 504.9325975
#Относительная разница во времени составляет: -783667.1753296125 %

#Удаление первого элемента в очереди
list_3 = []
deque_3 = deque([])

def fun_popleft(deq):
    for el in range(len(deq)):
        a = deq.popleft()
        print(a)

def fun_pop(list):
    for el in range(len(list)):
        a = list.pop(0)
        print(a)

time_5 = timeit("fun_popleft(deque_3)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_5}')
time_6 = timeit("fun_pop(list_3)", globals=globals(), number= 10000)
print(f'Время замера составило: {time_6}')

print(f'Относительная разница во времени составляет: {(time_5-time_6)/time_5*100} %')

#Время замера составило: 0.001631500000030428
#Время замера составило: 0.0016388999999890075
#Относительная разница во времени составляет: -0.45357033150115944 %


#Вывод:
#deque работает значительно быстрее при операциях заполнения элементов, а при заполнении снчала работает
#существенно быстрее
