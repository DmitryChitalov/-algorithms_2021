import time
import random

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


def get_func_time_decorator(func):
    def wrapper(arg1):
        start_time = time.time()
        r = func(arg1)
        return time.time() - start_time, r

    return wrapper


@get_func_time_decorator
def filling_list(num_of_el):
    return [i for i in range(num_of_el)]


@get_func_time_decorator
def filling_dict(num_of_el):
    return {f'key{i}': i for i in range(num_of_el)}


@get_func_time_decorator
def search_in_dict(my_dict):
    arr = []
    for i in range(10000):
        key = f'key{random.randint(1, 1000000)}'
        arr.append(my_dict.get(key))
    return arr


@get_func_time_decorator
def search_in_list(my_list):
    arr = []
    for i in range(10000):
        key = random.randint(1, 1000000)
        arr.append(my_list.index(key))
    return arr


num_of_el = 1000000
filling_list_time, my_list = filling_list(num_of_el)
filling_dict_time, my_dict = filling_dict(num_of_el)

print(f'Время заполнения списка - {filling_list_time}')
print(f'Время заполнения словаря - {filling_dict_time}')

# Время заполнения списка - 0.07813692092895508
# Время заполнения словаря - 0.5624675750732422
# заполнение  списка происходит быстрее
# добавление нового элемента в список O(n), где n - колличество элементов, могу предположить, что для словаря
# это составляет O(n*2) так как приходистя создавать пару ключ-значение

search_list_time, search_list_result = search_in_list(my_list)
search_dict_time, search_dict_result = search_in_dict(my_dict)

print(f'Время поиска в списке - {search_list_time}')
print(f'Время поиска в словаре - {search_dict_time}')

# Время поиска в списке - 66.74320721626282
# Время поиска в словаре - 0.015579938888549805
# поиск в словаре происходит гораздо быстрее, в словаре O(n) где n - колличество ключей,
# О(1) для одного ключа
# (но если поиск в списке проводить по индексу, то скорость даже быстрее чем в словаре)