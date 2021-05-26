"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from random import randint
import time
start = time.time()

def fill_list():
    n = 10000
    l = [randint(10, 100) for i in range(n)]
    return l

list1 = fill_list()
print(list1)

finish = time.time()
result = finish - start
print("Время: " + str(result) + " сек.")

from random import randint
import time
start = time.time()

def fill_dict():
    dict = {12: 13}
    i = 10000
    while i != 0:
        dict[randint(10, 100)] = randint(10, 100)
        i -= 1
    return dict

dict1 = fill_dict()
print(dict1)

finish = time.time()
result = finish - start
print("Время: " + str(result) + " сек.")

  # время заполнения словаря меньше списка

start = time.time()
dict1 = fill_dict()
dict1.__reversed__()
print(dict1)

finish = time.time()
result = finish - start
print("Время: " + str(result) + " сек.")


start = time.time()
list1 = fill_list()
list1.reverse()
print(list1)

finish = time.time()
result = finish - start
print("Время: " + str(result) + " сек.")

  # сложно сказать, но приблизительно равны