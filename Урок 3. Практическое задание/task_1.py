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

import time


def decor_time(func):
    def wrapper(*args):
        begin_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f'Для {str(func).split(" ")[1]} время выполнения составило: {end_time - begin_time} сек.')
        return result

    return wrapper


@decor_time
def list_add(list_add):
    list_temp = []
    for i in list_add:
        list_temp.append(i)


@decor_time
def dict_add(dict_add):
    dict_temp = {}
    for key, value in dict_add.items():
        dict_temp[key] = value


@decor_time
def list_find(list_find):
    list_find.index(100000)


@decor_time
def dict_find(dict_find):
    dict_find.get(100000, 0)


@decor_time
def list_clear(list_clear):
    return list_clear.clear()


@decor_time
def dict_clear(dict_clear):
    return dict_clear.clear()


test_dict = dict((int(n), int(n)) for n in range(10000000))
test_list = list((int(n)) for n in range(10000000))

print(list_add(test_list))  # 0.04064822196960449
print(dict_add(test_dict))  # 0.08363580703735352 Словарь заполняется дольше
print(list_find(test_list))  # 0.004428863525390625
print(dict_find(test_dict))  # 2.6226043701171875e-06 ~(0,00000262)
# Поиск по словарю быстрее из-за хеша
print(list_clear(test_list))  # 0.009126424789428511
print(dict_clear(test_dict))  # 0.008687973022460938