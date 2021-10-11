"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать,
   так и отличаться.
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

my_list_1 = []
my_list_2 = []
my_dict = {}


def check_time(fn):
    def wrapper(*args):
        start_val = time.time()
        fn(*args)
        end_val = time.time()
        print(f'{fn.__name__}, Операция заняла {end_val - start_val} сек')

    return wrapper


# O(n)
@check_time
def filling_list_append(n):
    for i in range(n):  # O(n)
        my_list_1.append(i)  # O(1)


# O(n*2)
@check_time
def filling_list_insert(n):
    for i in range(n):  # O(n)
        my_list_2.insert(0, i)  # O(n)


# O(n)
@check_time
def filling_dict_setdefault(n):
    for i in range(n):  # O(n)
        my_dict.setdefault(i, i)  # O(1)


filling_list_append(100000)
filling_list_insert(100000)
filling_dict_setdefault(100000)

"""
filling_list_append, Операция заняла 0.010479927062988281 сек
filling_list_insert, Операция заняла 4.127015829086304 сек
filling_dict_setdefault, Операция заняла 0.02166271209716797 сек
Заполнение списка выполняется быстрее чем словаря т.к. для словаря еще необходимо 
заполнять хеш таблицу. Но также заполнение списка методом append выполняется быстрее
чем методом insert при котором при каждом добавлении элемента необходимо сдвигать
последующие элементы
"""


# O(n)
@check_time
def change_list(n):
    for i in range(n):  # O(n)
        my_list_1[i] = 'new_data'  # O(1)


# O(n)
@check_time
def change_dict(n):
    for i in range(n):  # O(n)
        my_dict[i] = 'new_data'  # O(1)


change_list(100000)
change_dict(100000)

"""
change_dict, Операция заняла 0.019768714904785156 сек
change_list, Операция заняла 0.017672061920166016 сек
Изменение и поиск элементов в словаре и списке происходят с константной сложностью 
по ключу и индексу соответственно
"""


# O(n*2)
@check_time
def del_list_begin(n):
    for i in range(n):  # O(n)
        my_list_1.pop(0)  # O(n)


# O(n)
@check_time
def del_list_end(n):
    for i in range(n):  # O(n)
        my_list_2.pop()  # O(1)


# O(n)
@check_time
def del_dict(n):
    for i in range(n):  # O(n)
        my_dict.pop(i)  # O(1)


del_list_begin(100000)
del_list_end(100000)
del_dict(100000)

"""
del_list_begin, Операция заняла 2.6510438919067383 сек
del_list_end, Операция заняла 0.007825374603271484 сек
del_dict, Операция заняла 0.028162240982055664 сек
Удаление элементов списка выполняется быстрее чем словаря но только если они удаляются с конца списка
"""
print(my_list_1)
print(my_list_2)
print(my_dict)
