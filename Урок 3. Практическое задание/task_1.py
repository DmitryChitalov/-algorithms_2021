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
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time

VAL = 100000


def time_search(func):
    def wrapper(*args):
        start_val = time.time()
        # time.sleep(3)
        for arg in args:
            result = func(arg)
        end_val = time.time()
        return f'время на выполение функции "{func.__name__}"' \
               f' составило -> {end_val - start_val} '

    return wrapper


###############################################################################
"""
1. Заполнение.
Быстрее выполнятется заполнение списка методом "append". Наверное, это из-за
того, что при каждой операции заполнения в словарь заносится только 1 элемент, 
а в словарь 2 элемента (ключ и значение). При этом, метод "insert" в 240 раз
дольше.
"""


@time_search
def fill_append_list(n):  # Сложность O(n) - линейная (по циклу for in)
    lst = []
    for num in range(n):
        lst.append(num)  # Сложность самой вставки O(1) - константа
    return lst


@time_search
def fill_insert_list(n):  # Сложность O(n) - линейная (по циклу for in и
    lst = []  # сложности вставки)
    for num in range(n):
        lst.insert(0, num)


@time_search
def fill_dict(n):  # Сложность O(n) - линейная (по циклу for in)
    dictionary = {}
    for num in range(n):
        dictionary[num] = num  # Сложность самой вставки O(1) - константа


# print(fill_append_list(VAL))
# print(fill_insert_list(VAL))
# print(fill_dict(VAL))

###############################################################################
"""
2. Вставка элементов.
В 4 раза быстрее выполнятется вставка 1000 элементов в наполненный словарь, чем
в список по индексу. Это правильно, так как словарь представляет собой 
хеш-таблицу.
"""
insert_list = []
for num in range(VAL):
    insert_list.append(num)

insert_dict = {}
for num in range(VAL):
    insert_dict[num] = num


@time_search
def insert_elem_list(lst):  # Сложность O(n) - линейная (по циклу for in)
    for num in range(1000):
        lst.insert(100, num)  # Сложность вставки O(n) - линейная


@time_search
def setdefault_dict(d):  # Сложность O(n) - линейная (по циклу for in)
    for num in range(100000, 200000):
        d.setdefault(num, num)  # Сложность самой вставки O(1) - константа


# print(insert_elem_list(insert_list))
# print(setdefault_dict(insert_dict))
##############################################################################
"""
3. Удаление элементов.
Почему-то элементы из списка удаляются немного быстрее. Возможно, тратится время
на поиск произвольного элемента в словаре
"""
delete_list = []
for num in range(1000000):
    delete_list.append(num)

delete_dict = {}
for num in range(1000000):
    delete_dict[num] = num


@time_search
def delete_pop_list(lst):  # Сложность O(1) - константа
    while lst:
        lst.pop()  # Сложность O(1) - константа


@time_search
def delete_pop_dict(d):  # Сложность O(1) - константа
    while d:
        d.popitem()  # Сложность O(1) - константа

# print(len(delete_list))
# print(len(delete_dict))
# print(delete_pop_list(delete_list))
# print(delete_pop_dict(delete_dict))
