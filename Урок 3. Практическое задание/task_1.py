"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time
from datetime import timedelta

import random


def log_time(func):  # O(1)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Время выполнения ф-ции {func.__name__} составило: {timedelta(seconds=end_time - start_time)}")
        return result
    return wrapper


@log_time
def full_list(count):  # O(n)
    new_list = []
    for idx in range(count):
        new_list.append(random.randint(0, 100))
    return new_list

@log_time
def fill_list(count):  # O(n)
    new_list = [random.randint(0, 100) for _ in range(count)]
    return new_list

@log_time
def fill_dict(count):  # O(n)
    return {idx: random.randint(0, 100) for idx in range(count)}

@log_time
def create_dict(number):
    return {random.randint(100000, 200000): idx for idx in range(number)}

print("Создание структуры:")
list_1 = full_list(100000)
list_2 = fill_list(100000)
dict_1 = fill_dict(100000)
dict_2 = create_dict(100000)

list_2 = fill_list(63136)

'''
Время выполнения ф-ции full_list составило: 0:00:00.204481
Время выполнения ф-ции fill_list составило: 0:00:00.139124
Время выполнения ф-ции fill_dict составило: 0:00:00.179278

При одинаковом числе элементов, быстрее всех заполнился словарь через генератор списков - List Comprehension, 
далее по сложности заполнение словаря full_dict, 
и самое долгое full_list, с доабвлением элемента в конец списка через append()

'''
@log_time
def list_append(list, elem):  # O(n)
    for i in range(10000):
        list.append(elem)  # O(1)

@log_time
def dict_append(dict, elem):
    for i in range(10000, 20000):
        dict[i] = elem

print('add to structure:')
list_append(list_1, 55)
dict_append(dict_1, 'Russia')
''' добавление в словарь чаще всего быстрее
    Время выполнения ф-ции list_append составило: 0:00:00.002038
    Время выполнения ф-ции dict_append составило: 0:00:00.001036
'''

@log_time
def add_list_elem(lst, el):  # O(n)
    lst.extend(el)
    return lst


@log_time
def add_dict_elem(dct, el):  # O(n)
    dct.update(el)
    return dct


print("расширение структуры")
len_list_1 = len(list_1)
add_list_elem(list_1, list_2)
print(f"Расширение спика на {len(list_1) - len_list_1}")

len_dict_1 = len(dict_1)
add_dict_elem(dict_1, dict_2)
# add_dict_elem(dict_1, y)
print(len(dict_1))
# print(len(list_1))
print(f"Расширение словаря на {len(dict_1) - len_dict_1}")

'''
расширение структуры
Время выполнения ф-ции add_list_elem составило: 0:00:00.000997
Расширение спика на 63136
Время выполнения ф-ции add_dict_elem составило: 0:00:00.004981
163117
Расширение словаря на 63117


Добавление в словарь проиходят дольше, при равных колличествах добавленных эллементов,
 по сколько првоеряется если ли ключ уже в словаре
'''
