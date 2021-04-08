"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def get_time(func):
    def inner(*args, **kwargs):
        try:
            t0 = time.time()
            return func(*args, **kwargs)
        finally:
            t1 = time.time()
            print('Время выполнения функции ', func.__name__, ' равен', '{:.6f}ms'.format(1000 * (t1 - t0)), )

    return inner


@get_time
def get_list_1(number):
    items = []
    for i in range(number):
        items.append(i)
    return items


@get_time
def get_dict_1(number):
    result = {}
    for i in range(number):
        result[i] = i
    return result

#Search

data_list = [i for i in range(1000000)]
data_dict = {i: i for i in range(1000000)}


@get_time
def search_list(data):
    data.index(999998)


@get_time
def search_dict(data):
    data.get(5668999)


#delete

@get_time
def pop_list(data):
    for i in range(50000):
        data.pop(i)

@get_time
def pop_dict(data):
    for i in range(50000):
        data.pop(i)

get_list_1(10000000)
get_dict_1(10000000)

search_list(data_list)
search_dict(data_dict)


pop_list(data_list)

pop_dict(data_dict)

# списки представлены в виде массивов. Наибольшие затраты происходят при необходимости дополнить список
#Операции со словарями и их временная сложность
#Получение элемента: O(1).
#Установка элемента: O(1).
#Удаление элемента: O(1).

#Операции списка и их временная сложность
#Вставка: O(n).
#Получение элемента: O(1).
#Удаление элемента: O(n).


#Время выполнения функции  get_list_1  равен 1042.395830ms
#Время выполнения функции  get_dict_1  равен 963.671446ms
#Время выполнения функции  search_list  равен 12.993097ms
#Время выполнения функции  search_dict  равен 0.000000ms
#Время выполнения функции  pop_list  равен 26881.711006ms
#Время выполнения функции  pop_dict  равен 4.995108ms