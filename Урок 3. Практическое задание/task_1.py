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


def time_func(fun):
    def func_number(n):
        start = time.time()
        result = fun(n)
        end = time.time()
        return result, end - start

    return func_number


@time_func
def dict_insert(n):
    items = {}
    for i in range(1, n):
        items.update({i: i + 5})
    return items


@time_func
def list_insert(n):
    items = []
    for i in range(1, n):
        items.append(i)
    return items


@time_func
def search_item_dict(search_dict):
    return search_dict[55555]


@time_func
def search_item_list(search_list):
    for item in range(len(search_list)):
        if item == 55555:
            return item


items_dict, time_dict = dict_insert(500000)
items_list, time_list = list_insert(500000)
print(f'Заполнение словаря на 500000 элементов, время: {time_dict}')
print(f'Заполнение списка на 500000 элементов, время: {time_list}')
print('Заполнение словаря происходит дольше т.к. при создании элементов словаря происходит хеширование ключей\n')
print(search_item_dict(items_dict))
print(search_item_list(items_list))
print('Поиск элементов списка по индексу происходит дольше,\n'
      'чем элементов словаря по ключу т.к. опять же отсутвует хеширование для более быстрого поиска')

