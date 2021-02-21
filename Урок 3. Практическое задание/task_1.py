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


def time_func(func):
    def temp(n):
        start = time.time()
        res = func(n)
        end = time.time()
        return res, end - start

    return temp


@time_func
def func_to_list(val):
    res = []
    for i in range(val):
        for j in range(val):
            res.append(i * j)
    return res


@time_func
def func_to_dict(val):
    res = {}
    for i in range(val):
        for j in range(val):
            res.update({i: i * j})
    return res


@time_func
def oprt_to_list(lst):
    for i in range(len(lst)):
        if i == 98:
            print(lst[i])


@time_func
def oprt_to_dict(dct):
    res = dct[98]
    print(res)


obj_list_1, time_lst_1 = func_to_list(1000)
obj_dict_1, time_dct_1 = func_to_dict(1000)
obj_list_2, time_lst_2 = func_to_list(5000)
obj_dict_2, time_dct_2 = func_to_dict(5000)

print(f"Заполнение списка 1000: {time_lst_1}")
print(f"Заполнение словаря 1000: {time_dct_1}")
print(f"Заполнение списка 5000: {time_lst_2}")
print(f"Заполнение словаря 5000: {time_dct_2}")

# Заполнение словаря занимает больше времени ввиду того, что при создании словаря происходит хеширование

print(f"Поиск эемента списка 1000: {oprt_to_list(obj_list_1)[1]}")
print(f"Поиск эемента словаря 1000: {oprt_to_dict(obj_dict_1)[1]}")
print(f"Поиск эемента списка 5000: {oprt_to_list(obj_list_2)[1]}")
print(f"Поиск эемента словаря 5000: {oprt_to_dict(obj_dict_2)[1]}")

# Поиск элемента словаря по ключу происходит быстрее, чем поиск элемента по индексу в списке
