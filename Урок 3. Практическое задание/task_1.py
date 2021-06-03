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
import random


def time_check(function):
    """
    Decorator function for measuring the time of a function.
     We fix the time cutoffs before and after the execution of the main logic
     : param function: pass the executable function to the decorator
     : return: tuple of function result and elapsed time
    """
    def wrapped(*args):
        start_val = time.time()
        result = function(*args)
        end_val = time.time()
        return result, end_val - start_val
    return wrapped


@time_check
def dict_fill(quantity: int):
    origin_dict = {}
    for i in range(quantity):
        origin_dict[i] = random.randint(0, 25000)
    return origin_dict


@time_check
def list_fill(quantity: int):
    origin_list = [random.randint(0, 25000) for i in range(quantity)]
    return origin_list


@time_check
def dict_elem_remove(user_dict: dict):
    """
    remove elements from the dictionary: first get a list of keys, and then remove half of them
    """
    keys = list(user_dict.keys())
    print('Remove half elements from the dictionary')
    for key in keys[:(len(user_dict)) // 2]:
        user_dict.pop(key)


@time_check
def list_elem_remove(user_list: list):
    print('Delete half of the list')
    for i in range(len(user_list) // 2):
        user_list.pop(i)


@time_check
def dict_update(user_dict: dict, new_dict: dict):
    print('Let\'s update the dictionary by adding 25,000 new entries to it')
    user_dict.update(new_dict)


@time_check
def list_update(user_list: list, new_list: list):
    print('Let\'s update the list by adding 25,000 new entries to it')
    user_list.extend(new_list)


@time_check
def find_values_list(user_list, quantity: int, start_val: int):
    result = []
    for i in range(start_val, start_val + quantity):
        for el in user_list:
            if el == i:
                result.append(i)
    return result


@time_check
def find_values_dict(dict1, quantity: int, start_val: int):
    result = {}
    for i in range(start_val, start_val + quantity):
        for key, el in dict1.items():
            if el == i:
                result[key] = el
    return result

# Input elements.
elem_quantity = int(input('Enter the number of elements: '))
print('Let\'s go...')
my_dict_1 = dict_fill(elem_quantity)
my_list = list_fill(elem_quantity)
print(f'The operation of filling the dictionary took {my_dict_1 [1]} seconds. Number of items entered: {elem_quantity}')
print(f'The operation of filling the list took {my_dict_1 [1]} seconds. Number of items entered: {elem_quantity}')
print(len(my_dict_1[0]), len(my_list[0]))

''' The dictionary takes longer to fill than the list, since the keys are written to the dictionary, which are hashed,
and their meanings.
'''
#  Delete elements.
dict_after_remove = dict_elem_remove(my_dict_1[0])
print(f'The operation of removing elements from the dictionary took {dict_after_remove [1]} seconds.')
list_after_remove = list_elem_remove(my_list[0])
print(f'The operation of removing elements from the list took {dict_after_remove [1]} seconds.')
print(len(my_dict_1[0]), len(my_list[0]))
'''
Removal in the dictionary is much faster due to the fact that the search
by a key in a dictionary is much faster than searching by an index in a list.
'''
'''
Update elements.
Let's prepare a new dictionary and list to add
'''
added_dict = {i: random.random() for i in range(5000, 10000)}
added_list = [elem for elem in range(5000)]

dict_after_update = dict_update(my_dict_1[0], added_dict)
print(f'The operation of adding elements to the dictionary took {dict_after_update [1]} seconds.')
list_after_update = list_update(my_list[0], added_list)
print(f'The operation of adding elements to the list took {dict_after_update [1]} seconds.')
print(len(my_dict_1[0]), len(my_list[0]))

'''
Adding to the dictionary is slower because keys have to be hashed again
'''
'''
Search by value
to search by values, prepare a list with the necessary keys
'''

my_find_dict = find_values_dict(my_dict_1[0], 100, 1500)
print(f'Search by value in the dictionary took {my_find_dict [1]}')
my_find_list = find_values_list(my_list[0], 100, 1500)
print(f'Search by value in the list took {my_find_dict [1]}')

'''
Search by value in the dictionary takes longer than in the list
'''
