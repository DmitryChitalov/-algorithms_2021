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
from timeit import default_timer


def measure_exec_time(func):
    def wrapper(*args):
        start = default_timer()
        func(*args)
        end = default_timer()
        print('Exec time:', (end-start) * 10 ** 6, 'x 10^-6 s')
    return wrapper


@measure_exec_time
def fill_list(n):  # O(N)
    my_list = []
    i = 1
    while i <= n:
        my_list.append(i)
        i += 1
    return my_list

@measure_exec_time
def fill_dict(n):  #O(N)
    my_dict = {}
    i = 1
    while i <= n:
        my_dict.update({str(i): i})
        i += 1
    return my_dict


my_list = []
my_dict = {}


@measure_exec_time
def list_append(ls: list, *args):  # O(1) для одного arg и O(N) в общем случае
    for arg in args:
        ls.append(arg)


@measure_exec_time
def list_insert(ls: list, pos: int, arg):  # O(N)
    ls.insert(pos, arg)


@measure_exec_time
def list_pop(ls: list, pos: int):  # O(N)
    ls.pop(pos)


@measure_exec_time
def dict_update(dt: dict, new_dt: dict):  # O(N)
    dt.update(new_dt)


@measure_exec_time
def dict_values(dt: dict):  # O(1)
    return dt.values()


@measure_exec_time
def dict_pop(dt: dict):  # O(1)
    return dt.popitem()


fill_list(100)
fill_dict(100)
fill_list(1000)
fill_dict(1000)
fill_list(10000)
fill_dict(10000)
fill_list(100000)
fill_dict(100000)
'''
    Как и ожидалось, заполнение словаря примерно в 4 раза медленнее. При изменении N соотношение времен не меняется.
    Возможно, влияет хеширование словаря и два значения key-value вместо одного value.
'''

print('List operations:')
list_append(my_list, 1)
list_append(my_list, 1)
list_insert(my_list, 0, 1)
list_insert(my_list, 1, 1)
list_pop(my_list, 0)

new_my_list = []
for i in range(1000):
    new_my_list.append(i)

list_append(my_list, *new_my_list)

list_append(my_list, 1)
list_insert(my_list, 0, 1)
list_insert(my_list, 1, 1)
list_pop(my_list, 0)

print('Dict operations:')
dict_update(my_dict, {'one': 1})
dict_values(my_dict)
dict_pop(my_dict)

new_my_dict = {}
for i in range(1000):
    new_my_dict.update({str(i): i})

dict_update(my_dict, new_my_dict)
'''
    У списков append выполняется быстро для одного элемента, остальные операции зависят от N. 
    Интересно что первая из однотипных операций выполняется медленнее остальных, каждый раз пересматривается весь массив
    У словарей за счет уникальности ключей все происходит за константное время, кроме добавления элементов, 
    чтобы их обработать, требуются ресурсы
'''