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

from time import time
from datetime import timedelta
import random
from collections import deque

def log_time(func):  # O(1)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения ф-ции {func.__name__} составило: {timedelta(seconds=end_time - start_time)}")
        return result
    return wrapper


@log_time
def create_list(count):  # O(n)
    new_list = [random.randint(0, 100) for _ in range(count)]
    return new_list

@log_time
def create_deque(count):
    return deque([random.randint(0, 100) for _ in range(count)])


@log_time
def list_append(list, elem):
    for i in range(15000):
        list.insert(0, elem)
    return list

@log_time
def deque_append(deque, elem):
    for i in range(15000):
        deque.appendleft(elem)
    return deque

@log_time
def list_popleft(list):
    for i in range(10000):
        list.pop(0)
    return list

@log_time
def deque_popleft(deque):
    for i in range(10000):
        deque.popleft()
    return deque

@log_time
def list_extendleft_1(list, list_ext):
    for elem in list_ext[0:100]:
        list.insert(0, elem)
    return list

@log_time
def list_extendleft_2(list, list_ext):
    list_ext.extend(list)
    return list_ext

@log_time
def deque_extendleft(deque, deque_ext):
    deque.extendleft(deque_ext)
    return deque
#  popleft, extendleft

length = 100000
list_1 = create_list(length)
deque_1 = create_deque(length)
# список создается дольше, чем очередь

# list_append(list_1, 'word')
list_2 = list_append(list_1, 'word')
# print(list_2)
# print(len(list_2))
deque_2 = deque_append(deque_1, 'word')
print(deque_2)
''' 
добавление элемента в дек в начало гораздо быстрее, чем в начало списка.
Добавление 10 000 элементов
     Время выполнения ф-ции list_append составило: 0:00:00.679185
    Время выполнения ф-ции deque_append составило: 0:00:00.001000   
    
Добавление 15 000 элементов
     Время выполнения ф-ции list_append составило: 0:00:01.219707
    Время выполнения ф-ции deque_append составило: 0:00:00.002039'''

list_3 = list_popleft(list_2)
# print(list_3)
# print(len(list_3))
deque_3 = deque_popleft(deque_1)
# аналогично, дек работает гораздо бытсрее, чем словарь

list_extendleft_1(list_2, list_1)
list_extendleft_2(list_2, list_1)
deque_extendleft(deque_2, deque_1)
print(len(deque_1))
# добавление даже 100 элементов в начало списка дольше дека, но
# можно похитрить и добавлять не в начало нашего списка список, а в добавляющийся список наш список,
# либо использовать reverse(), но у него сложность O(n), что тоже долго