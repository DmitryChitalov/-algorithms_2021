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


def time_measure(func):
    def start_measure(obj, desc):
        start = time.time()
        func(obj, desc)
        stop = time.time()
        print(f'{desc}\n{stop - start}')
        return obj

    return start_measure


@time_measure
def dict_add_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj[index] = str(index)  # O(1)
    return obj  # O(1)


@time_measure
def dict_change_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj[index] = str(index + index)  # O(1)
    return obj  # O(1)


@time_measure
def dict_delete_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj.pop(index)  # O(1)
    return obj  # O(1)


@time_measure
def list_add_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj.append(str(index))
    return obj


@time_measure
def list_change_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj.insert(index - 1, str(index))  # O(1)
    return obj  # O(1)


@time_measure
def list_delete_values(obj, desc):  # Сложность функции: O(1)
    for index in range(100000):  # O(1)
        obj.pop(index)  # O(1)
    return obj  # O(1)


new_dict = {}
dict_add_values(new_dict, 'Время выполнения добавления в словарь:')
dict_change_values(new_dict, 'Время выполнения замены значений словаря:')
dict_delete_values(new_dict, 'Время выполнения очистки словаря:')

new_list = []
list_add_values(new_list, 'Время выполнения добавления в список:')
list_change_values(new_list, 'Время выполнения замены значений словаря:')
list_delete_values(new_list, 'Время выполнения очистки словаря:')

# Вывод: При равных сложностях алгоритма, выполнение добавления в словарь происходит медленнее, чем добавление в список,
# операции замены значений, удаление значений происходят быстрее на словаре
