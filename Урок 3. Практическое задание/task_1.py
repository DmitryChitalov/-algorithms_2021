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


def check_time(func):
    def g(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        return result, end_time - start_time
    return g


@check_time
def full_list(n):
    result_list = [el for el in range(n)]
    return result_list


@check_time
def full_dict(n):
    result_dict = {el: el for el in range(n)}
    return result_dict


@check_time
def del_values_list(list1, how_much, n_from):
    for i in range(n_from, n_from + how_much):
        list1[0].pop(i)
    return list1


@check_time
def del_values_dict(dict1, how_much, n_from):
    for i in range(n_from, n_from + how_much):
        dict1[0].pop(i)
    return dict1


@check_time
def find_values_list(list1, how_much, n_from):
    result = []
    for i in range(n_from, n_from + how_much):
        for el in list1[0]:
            if el == i:
                result.append(i)
    return result


@check_time
def find_values_dict(dict1, how_much, n_from):
    result = {}
    for i in range(n_from, n_from + how_much):
        for key, el in dict1[0].items():
            if el == i:
                result[key] = el
    return result


# 1. Создание списка и словаря
number_of_items = 1000000
print(f'Возьмем {number_of_items} значений')
my_list1 = full_list(number_of_items)
my_dict1 = full_dict(number_of_items)

print(f'Список создается за {my_list1[1]} с')
print(f'Словарь создается за {my_dict1[1]} с')

# Вывод №1: Словарь заполняется дольше, чем список, так как помимо данных в словарь
# записываются ключи, которые хэшируются.


# 2. Поиск и удаление значений
my_list2 = del_values_list(my_list1, 10000, 10000)
print(f'Поиск по списку занял {my_list1[1]} с')

my_dict2 = del_values_dict(my_dict1, 10000, 10000)
print(f'Поиск по словарю занял {my_dict2[1]} с')

# Вывод №2: Удаление в словаре происходит намного быстрее за счет того, что поиск
# по ключу в словаре работает гораздо быстрее, чем поиск по индексу в списке.


# 3. Поиск по значению
my_list3 = find_values_list(my_list1, 10, 5000)
print(f'Поиск по значению в списке занял {my_list3[1]} с')
my_dict3 = find_values_dict(my_dict1, 10, 5000)
print(f'Поиск по значению в словаре занял {my_dict3[1]} с')

# Вывод №3: Поиск по значению в словаре осуществляется гораздо дольше, чем в списке
