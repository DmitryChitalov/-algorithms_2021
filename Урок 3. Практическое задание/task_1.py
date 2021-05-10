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


import time
from random import randint


def timer(function):
    def captured_function(value):
        start = time.time()
        result = function(value)
        print(f'Выполнено за: {time.time() - start} сек.')
        return result
    return captured_function


@timer
def list_filling(num):
    print("Добавление в лист: ")
    func_lst = [el for el in range(num)]
    return func_lst


@timer
def dict_filling(num):
    print("Добавление в словарь: ")
    func_dict = {el: el for el in range(num)}
    return func_dict


@timer
def list_value(lst):
    print('Индекс элемента списка: ')
    return lst.index(randint(0, num_el))


@timer
def dict_value(dct):
    print('Индекс элемента словаря: ')
    return dct.get(randint(0, num_el))


@timer
def list_add(lst):
    count = len(lst)
    i = 1
    while i < num_el:
        lst.append(count+1)
        i += 1
    print("Добавление в список: ")
    return


@timer
def dict_add(dicts):
    count = len(dicts)
    i = 1
    while i < num_el:
        dicts.update({count: count})
        count += 1
        i += 1
    print("Добавление в словарь: ")
    return


@timer
def list_pop(lst):
    i = 0
    while i < num_el:
        lst.pop()
        i += 1
    print("Удаление из списка: ")
    return


@timer
def dict_pop(dct):
    i = 0
    while i < num_el:
        dct.popitem()
        i += 1
    print("Удаление из словаря: ")
    return


@timer
def list_clear(lst):
    print('Очищение списка: ')
    return lst.clear()


@timer
def dict_clear(dct):
    print('Очищение словаря: ')
    return dct.clear()


num_el = 1000000
my_list = list_filling(num_el)
my_dict = dict_filling(num_el)
print("---------------------------------------")


list_value(my_list)  # 0.02 сек.
dict_value(my_dict)  # 0.0 сек.
print("---------------------------------------")


list_add(my_list)
dict_add(my_dict)
print("---------------------------------------")


list_pop(my_list)
dict_pop(my_dict)
print("---------------------------------------")


list_clear(my_list)
dict_clear(my_dict)

"""
Добавление в лист: 
Выполнено за: 0.04100918769836426 сек.
Добавление в словарь: 
Выполнено за: 0.07501697540283203 сек.
---------------------------------------
Индекс элемента списка: 
Выполнено за: 0.008002281188964844 сек.
Индекс элемента словаря: 
Выполнено за: 0.0 сек.
---------------------------------------
Добавление в список: 
Выполнено за: 0.19205260276794434 сек.
Добавление в словарь: 
Выполнено за: 0.3760850429534912 сек.
---------------------------------------
Удаление из списка: 
Выполнено за: 0.19404339790344238 сек.
Удаление из словаря: 
Выполнено за: 0.1690385341644287 сек.
---------------------------------------
Очищение списка: 
Выполнено за: 0.008002281188964844 сек.
Очищение словаря: 
Выполнено за: 0.011002540588378906 сек.
Практически все операции быстрее проходят со списком, причина в хешах, которые создает для себя словарь.
Но в тот же момент эти хеши позволяют выигрывать словарю в поиске элементов. Еще интересный момент с 
удалением элемента с конца, даже с учетом удаления хеша время практически одинаковое видимо связянно
это с темм, что величина постоянна а сама операция .pop является константной.
"""