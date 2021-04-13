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


def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        temp_obj = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции - {end_time - start_time}.')
        return temp_obj
    return wrapper


@time_counter
def fill_list(number):
    new_list = []
    for i in range(0, number):
        new_list.append(i)
    return new_list


@time_counter
def fill_dict(number):
    new_dict = {}
    for i in range(0, number):
        new_dict[i] = f'{i}'
    return new_dict


@time_counter
def list_index_search(list_obj):
    for i in range(0, len(list_obj)):
        if i == 666:
            print(list_obj[i])


@time_counter
def dict_index_search(dict_obj):
    print(dict_obj[666])


@time_counter
def list_value_search(list_obj):
    for i in list_obj:
        if i == 666:
            print(i)


@time_counter
def dict_value_search(dict_obj):
    for i in dict_obj.values():
        if i == 666:
            print(i)


my_list = fill_list(1000000)  # Время выполнения функции - 0.24684977531433105.
my_dict = fill_dict(1000000)  # Время выполнения функции - 0.6905722618103027.

"""
Заполнение списка происходит быстрее, так как при заполнении словаря происходит расчет хэша.
"""

list_index_search(my_list)  # Время выполнения функции - 0.12991976737976074.
dict_index_search(my_dict)  # Время выполнения функции - 0.0.

"""
Поиск по индексу работает быстрее в словаре, т.к. словарь это хэш-таблица, и алгоритм поиска по хэш-таблице
работает быстрее, чем простой перебор списка.
"""

list_value_search(my_list)  # Время выполнения функции - 0.06896185874938965.
dict_value_search(my_dict)  # Время выполнения функции - 0.10792994499206543.

"""
Поиск по значению работает быстрее в списке. 
"""