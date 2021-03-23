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


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start

    return timer


@time_decorator
def list_func(length):
    result = []
    for i in range(length):
        result.append(i)
    return result


@time_decorator
def dict_func(length):
    result = {}
    for i in range(length):
        result[i] = f'number {i}'
    return result


@time_decorator
def check_dict_key(dict_obj):
    v = dict_obj[1234]
    print(v)


@time_decorator
def check_list_index(list_obj):
    for i in range(len(list_obj)):
        if i == 1234:
            print(list_obj[i])


@time_decorator
def check_dict_value(dict_obj):
    for v in dict_obj.values():
        if v == 'number 1234':
            print(v)


@time_decorator
def check_list_value(list_obj):
    for v in list_obj:
        if v == 1234:
            print(v)


new_list_1, list_time_1 = list_func(10000)
new_dict_1, dict_time_1 = dict_func(10000)
print('list 100000', list_time_1)
print('dict 100000', dict_time_1)

new_list_2, list_time_2 = list_func(10000)
new_dict_2, dict_time_2 = dict_func(10000)
print('list 100000', list_time_2)
print('dict 100000', dict_time_2)

new_list_3, list_time_3 = list_func(10000)
new_dict_3, dict_time_3 = dict_func(10000)
print('list 100000', list_time_3)
print('dict 100000', dict_time_3)

print('*****')

print('index list 100000', check_list_index(new_list_1)[1])
print(' keys dict 100000', check_dict_key(new_dict_1)[1])
print('index list 10000000', check_list_index(new_list_2)[1])
print(' keys dict 10000000', check_dict_key(new_dict_2)[1])
print('index list 10000000', check_list_index(new_list_3)[1])
print(' keys dict 10000000', check_dict_key(new_dict_3)[1])

print('****')

print('values list 100000', check_list_value(new_list_1)[1])
print('values dict 100000', check_dict_value(new_dict_1)[1])
print('values list 10000000', check_list_value(new_list_2)[1])
print('values dict 10000000', check_dict_value(new_dict_2)[1])
print('values list 10000000', check_list_value(new_list_3)[1])
print('values dict 10000000', check_dict_value(new_dict_3)[1])

# добавление в словарь проходит дольше, из-за необходимости добавки хеш-ключа
# поиск элемента из словаря по ключу идет быстрей, чем поиск по индексу
# поиск по значениям в словаре идет дольше, чем поиск по значениям в списке
