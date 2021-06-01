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

from time import time

idx = 670000


def check_time(function):
    def current_function(value):
        start_time = time()
        result = function(value)
        end_time = time()
        print(f"Время выполнения: {end_time - start_time} сек")
        return result
    return current_function


@check_time
def filling_list(length):
    print("Заполнение списка")
    filled_list = [i for i in range(length)]
    return filled_list


@check_time
def filling_dict(length):
    print("Заполнение словаря")
    filled_dict = {i: i for i in range(length)}
    return filled_dict


@check_time
def value_in_list(lst):
    print("Получение элемента из списка по индексу")
    return lst.index(idx)


@check_time
def value_in_dict(dct):
    print("Получение элемента из списка по индексу")
    return dct.get(idx)


@check_time
def delete_element_list(lst):
    for _ in range(200000):
        lst.pop()
    print("Удаление последнего элемента из списка")
    return


@check_time
def delete_element_dict(dct):
    for _ in range(200000):
        dct.popitem()
    print("Удаление последнего элемента из словаря")
    return


@check_time
def clear_list(lst):
    print("Удаление всех элементов из списка")
    return lst.clear()


@check_time
def clear_dict(dct):
    print("Удаление всех элементов из словаря")
    return dct.clear()


my_list = filling_list(10000000)
my_dict = filling_dict(10000000)
print("_"*50)

value_in_list(my_list)
value_in_dict(my_dict)
print("_"*50)

delete_element_list(my_list)
delete_element_dict(my_dict)
print("_"*50)

clear_list(my_list)
clear_dict(my_dict)
"""
Заполнение словаря происходит медленнее, потому что необходимо посчитать хеш, но получение элемента по индексу 
у словаря быстрее благодаря тому же хешу. Время удаления элементов почти всегда одинаково
"""