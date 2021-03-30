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


def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return func.__name__, (t2 - t1), res
    return wrapper


@timing_val
def create_list(count_el):
    my_list = []
    for i in range(count_el):
        my_list.append(i)
    return my_list

@timing_val
def create_dict(count_el):
    my_dict = {}
    for i in range(count_el):
        my_dict[i] = "#" + str(i)
    return my_dict


@timing_val
def check_dict_value(dict_obj):
    el = dict_obj[77777]
    return el


@timing_val
def check_list_value(list_obj):
    for i in range(len(list_obj)):
        if i == 77777:
            return list_obj[i]


my_list = create_list(1000000)
my_dict = create_dict(1000000)

if my_list[1] > my_dict[1]:
    print('лист заполняется медленнее на:', my_list[1] - my_dict[1])
else:
    print('словать заполняется медленнее на: ', my_list[1] - my_dict[1],
          '\nиз за необходимости создавать хеш для ключей')

print(check_dict_value(my_dict[2]))
print(check_dict_value(my_list[2]))
"не могу сравнить скорость поиска так-как получаю значения 0.0," \
" но поиск по ключу в словаре должен работать быстрее в теории"
