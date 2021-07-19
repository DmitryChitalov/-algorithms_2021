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

from time import time

my_list = []
my_dictionary = {}


def my_time(f):
    def count_time(n):
        start_val = time()
        name = f(n)
        end_val = time()
        return f'{name} {end_val - start_val}'

    return count_time


print('Заполнение')


# Константная
@my_time
def lst_fill(lst):
    # start_val = time.time()
    for i in range(10000000):  # O(1)
        lst.append(i)  # O(1)
    # end_val = time.time()
    return 'Список'  # O(1)


#  Константная
@my_time
def dict_fill(dictionary):
    # start_val = time.time()
    for i in range(10000000):
        dictionary[i] = i
    # end_val = time.time()
    return 'Словарь'


print(lst_fill(my_list))
print(dict_fill(my_dictionary))

print('Вывод элементов по индексу')


# Константная
@my_time
def lst_search(lst):
    for i in range(1, 10000):
        lst.index(i)
    return 'Список'


# Константная
@my_time
def dict_search(dictionary):
    for i in range(1, 10000):
        dictionary[i]
    return 'Словарь'


print(lst_search(my_list))
print(dict_search(my_dictionary))

#  Константная
print('Опустошение')


@my_time
def lst_empty(lst):
    lst.clear()
    return 'Список'


#  Константая
@my_time
def dict_empty(dictionary):
    dictionary.clear()
    return 'Словарь'


print(lst_empty(my_list))
print(dict_empty(my_dictionary))
