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


def decorator_func(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        return_val = func(*args, **kwargs)
        t2 = time.time()
        print("Время работы {}".format(t2 - t1))
        return return_val

    return wrapper


# заполнение списка и словаря програмно
@decorator_func
def create_lst():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst


@decorator_func
def create_dict():
    dict_val = {}
    for i in range(1000000):
        dict_val[str(i)] = i
    return dict_val


lst_val = create_lst()
dict_val = create_dict()
"""
Список выполняется быстрее примерно в 4,5 раза быстрее, т.к словарь требует гернерации хэшей
"""


######################################################################
# обновление списка и словаря
@decorator_func
def update_lst(val):
    for i in range(100000):
        val[i] = i + 10


def update_dict(val):
    for i in range(100000):
        val[str(i)] = i + 10


print("*" * 100)
print("Время обновления")
update_lst(lst_val)

t1 = time.time()
update_dict(dict_val)
print("Время обновления словаря {}".format(time.time() - t1))


# перебор списка и словаря
@decorator_func
def enum_lst_dict(val):
    for i in val:
        pass


print("*" * 100)
print("Время перебора")
enum_lst_dict(lst_val)
enum_lst_dict(dict_val)


# удаление списка и словаря
@decorator_func
def del_lst(val):
    for __ in range(100000):
        val.pop()


def del_dict(val):
    for i in range(100000):
        val.pop(str(i))


print("*" * 100)
print("Время удаления")
del_lst(lst_val)

t1 = time.time()
del_dict(dict_val)
print("Время удаления словаря {}".format(time.time() - t1))

"""
При обновление или удалении словаря или списка при константной сложности - список работает быстрее, так как у него нет хэша
При переборе список примерно в 2 раза быстрее, т.к в словаре идет генерация хэша при запросе.
Итог: работа со списком происходит быстрее!
"""
