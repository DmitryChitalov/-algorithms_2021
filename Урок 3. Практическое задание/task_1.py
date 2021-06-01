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

# Вывод а: Заполнение списка и словаря каждый раз происходит за разное время, и быстрее заполняется то список,
# то словарь. Невозможно корректно определить что именно выполянется быстрее
# Вывод б: Выполнение всех операций также происходит за разное время, их выполнение быстрее то у списка, то у словаря.

import time


def time_tracker(func):
    def time_tracker_wrapper(*args, **kwargs):
        start_val = time.time()
        func_res = func(*args, **kwargs)
        time.sleep(1)
        print(time.time() - start_val, ' sec')
        return func_res
    return time_tracker_wrapper


@time_tracker
def list_append(*args, **kwargs):
    lst = []
    for i in range(len(args)):
        lst.append(args[i])
    return lst


@time_tracker
def dict_append(*args, **kwargs):
    test_dict = {}
    for i in range(len(args)):
        test_dict[i+1] = args[i]
    return test_dict


@time_tracker
def find_list(test_list):
    one_element = test_list[1]
    return one_element


@time_tracker
def find_dict(test_dict):
    one_element = test_dict[1]
    return one_element


@time_tracker
def len_list(test_list):
    len_of_list = len(test_list)
    return len_of_list


@time_tracker
def len_dict(test_dict):
    len_of_dict = len(test_dict)
    return len_of_dict


@time_tracker
def pop_list(test_list):
    pop_element = test_list.pop(1)
    return pop_element


@time_tracker
def pop_dict(test_dict):
    pop_element = test_dict.pop(1)
    return pop_element


print('Заполнение списка и словаря')
print('Список ', list_append(1, 2, 3, 4, 5))
print('Словарь ', dict_append(1, 2, 3, 4, 5), '\n')
print('Поиск элемента в списке и словаре')
print('Список ', find_list([1, 2, 3, 4, 5]))
print('Словарь ', find_dict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}), '\n')
print('Определение длины списка и словаря')
print('Список ', len_list([1, 2, 3, 4, 5]))
print('Словарь ', len_dict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}), '\n')
print('Удаление элемента из списка и словаря')
print('Список ', pop_list([1, 2, 3, 4, 5]))
print('Словарь ', pop_dict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))
