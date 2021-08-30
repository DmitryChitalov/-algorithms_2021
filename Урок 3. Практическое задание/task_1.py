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

my_list = []
my_dict = {}
value_range = 1234565


def time_note(func):
    def timing(*args, **kwargs):
        time_start = time.time()
        actions = func(*args, **kwargs)
        print(time.time() - time_start)
        return actions

    return timing


# 1)
@time_note
def apply_list(lst, values):  # O(1)
    for i in range(values):
        lst.append(i)


apply_list(my_list, value_range)


@time_note
def apply_dictionary(dictionary, values):  # O(1)
    for i in range(values):
        dictionary[i] = i


apply_dictionary(my_dict, value_range)


# Вывод: Поскольку словарь является хеш-таблицей и его сложность константная(O(1)), заполнение словаря
# производится быстрее.

# 2)
@time_note
def update_list(lst):  # O(n)
    for i in range(2000):  # O(n)
        lst.remove(i)
    for j in range(1000):  # O(1)
        lst.pop()


update_list(my_list)


@time_note
def update_dictionary(dictionary):  # O(n)
    for i in range(2000):  # O(n)
        dictionary.pop(i)
    for j in range(1000):  # O(1)
        dictionary.popitem()


update_dictionary(my_dict)

# Вывод: Изменения в словаре производятся быстрее, т.к. словарь является хеш-таблицей,
# а сложность словаря - константная.
