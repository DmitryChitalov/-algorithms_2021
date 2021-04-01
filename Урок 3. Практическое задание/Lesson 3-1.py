"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def time_decor(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start

    return timer


@time_decor
def list_filling(quantity):
    result = []
    for i in range(quantity):
        result.append(i)
    return result


@time_decor
def dict_filling(quantity):
    result = {}
    for i in range(quantity):
        result[i] = i
    return result


@time_decor
def list_value(list_obj):
    for j in list_obj:
        if j == 148888:
            return j


@time_decor
def dict_value(dict_obj):
    for j in dict_obj.values():
        if j == '148888':
            return j


@time_decor
def list_index(list_ind):
    for i in range(len(list_ind)):
        if i == 148888:
            return list_ind[i]


@time_decor
def dict_key(dict_k):
    v = dict_k[148888]
    return v


my_list, list_timer = list_filling(1000000)
my_dict, dict_timer = dict_filling(1000000)
print('-----------------------------------------------------------------------------')
print('Произведём замер времени по заполнению списка и словаря:')
print('Результат заполнения списка: ', list_timer)
print('Результат заполнения словаря: ', dict_timer)
print('********** Вывод: список заполняется быстрее, чем словарь')
print('-----------------------------------------------------------------------------')
print('Произведём замер времени поиска по значению в списке и словаре:')
print('Результат поиска по значению в списке: ', list_value(my_list))
print('Результат поиска по значению в словаре: ', dict_value(my_dict))
print('********** Вывод: поиск по значению в списке быстрее поиска по значению в словаре')
print('-----------------------------------------------------------------------------')
print('Произведём замер времени поиска по индексу в списке и по ключу в словаре:')
print('Результат поиска по индексу в списке: ', list_index(my_list))
print('Результат поиска по ключу в словаре: ', dict_key(my_dict))
print('********** Вывод: в случае со взятием элемента по индексу в списке и по ключу в словаре быстрее оказался словарь')
