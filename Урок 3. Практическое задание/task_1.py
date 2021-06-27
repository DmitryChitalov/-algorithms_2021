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


def check_time_dict(n):  # -> O(N), время заполнения словаря медленнее списка
    global new_dict
    start_val = time.time()
    for i in range(1, n + 1):
        new_dict[i] = str(i)
    end_val = time.time()
    return end_val - start_val, new_dict


def check_time_list_1(n):  # -> O(N), заполнение списка быстрее словаря
    global new_list
    start_val = time.time()
    new_list = [str(i) for i in range(0, n + 1)]
    end_val = time.time()
    return end_val - start_val, new_list


def check_time_list_2(n):  # -> O(N), заполнение списка быстрее словаря
    start_val = time.time()
    for i in range(1, n + 1):
        new_list.append(str(i))
    end_val = time.time()
    time_fill_list_2 = end_val - start_val
    return time_fill_list_2


def time_edit_dict(dict):  # -> O(N), сортировка словаря быстрее списка
    start_val = time.time()
    top_dict = sorted(dict, key=dict.get, reverse=True)
    end_val = time.time()
    return end_val - start_val, top_dict


def time_edit_list(list):  # -> O(N)
    start_val = time.time()
    list.sort(reverse=True)
    end_val = time.time()
    return end_val - start_val


value = 1000000
new_dict = {}
new_list = []
print(f'заполнению словаря заняла: {check_time_dict(value)[0]} сек')
print(f'заполнению списка (list comprehention) заняла: {check_time_list_1(value)[0]} сек')
print(f'заполнению списка (append) заняла: {check_time_list_2(value)} сек')
print(f'сортировке словаря заняла: {time_edit_dict(new_dict)[0]} сек')
print(f'сортировке списка заняла: {time_edit_list(new_list)} сек')


"""
Время выполнения добавления элементов в словарь больше, чем в список,
из-за расчёта хеша для эллементов. 
"""