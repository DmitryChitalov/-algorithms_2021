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
        val = i * 99
        new_dict[i] = val
    return new_dict


@time_counter
def list_pop(obj, number):
    if number > len(obj):
        number = len(obj)
    for i in range(0, number):
        obj.pop()


@time_counter
def dict_pop(obj, number):
    if number > len(obj):
        number = len(obj)
    for i in range(0, number):
        obj.pop(i)


my_list = fill_list(10000000)  # Время выполнения функции - 1.7269349098205566.
my_dict = fill_dict(10000000)  # Время выполнения функции - 3.7117152214050293.

# Заполнение списка происходит быстрее, так как при заполнении словаря происходит расчет хэша.

list_pop(my_list, 100000)
dict_pop(my_dict, 100000)
