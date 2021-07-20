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
my_list = []
my_dict = {}
val_range = 1234565


def time_note(func):
    def timing(*args, **kwargs):
        time_start = time.time()
        actions = func(*args, **kwargs)
        print(time.time() - time_start)
        return actions
    return timing


# a)
@time_note
def apply_list(lst, values):   #Сложность: O(1)
    for i in range(values):
        lst.append(i)


apply_list(my_list, val_range)



@time_note
def apply_dict(dct, values):   #Сложность: O(1)
    for i in range(values):
        dct[i] = i


apply_dict(my_dict, val_range)

# Вывод: словарь заполняется быстрее, так как он является хеш-тфблицей и его сложность константная - O(1)


# b)
@time_note
def update_list(lst): # O(n)
    for i in range(2000): # Сложность: O(n)
        lst.remove(i)
    for j in range(1000): # Сложность: O(1)
        lst.pop()


update_list(my_list)


@time_note
def update_dict(dct): # O(n)
    for i in range(2000): # Сложность: O(n)
        my_dict.pop(i)
    for j in range(1000): # Сложность: O(1)
        my_dict.popitem()


update_dict(my_dict)


# Изменения в словаре так же происходят быстрее (по той же причине, что и заполнение)
