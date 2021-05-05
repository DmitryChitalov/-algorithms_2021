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


lst_result = []
dicts_result = {}


def lead_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        name = func(*args, **kwargs)
        end = time.time()
        return f'{name} - Время выполнения : {end - start} секунд.'
    return wrapper


@lead_time
def lst_app(lst):
    for el in range(99999):
        lst.append(el)
    return 'Заполнение списка'


@lead_time
def dict_app(dicts):
    for el in range(99999):
        dicts[el] = el
    return 'Заполнение словаря'


@lead_time
def list_search_lst(lst):
    i = 1
    while i < 10000:
        lst.index(i)
        i += 1
    return 'Поиск по индексу в списке'


@lead_time
def list_search_dict(dicts):
    i = 1
    while i < 10000:
        dicts[i]
        i += 1
    return 'Поиск по индексу в словаре'


@lead_time
def list_in(lst):
    count = len(lst)
    i = 1
    while i < 10000:
        lst.append(count+1)
        i += 1
    return 'Добавление в конец списка'


@lead_time
def dict_in(dicts):
    count = len(dicts)
    i = 1
    while i < 10000:
        dicts.update({count: count})
        count += 1
        i += 1
    return 'Добавление в конец словаря'


@lead_time
def list_del(lst):
    i = 0
    while i < 10000:
        lst.pop()
        i += 1
    return 'Удаление с конца списка'


@lead_time
def dict_del(dicts):
    i = 0
    while i < 10000:
        dicts.popitem()
        i += 1
    return 'Удаление с конца словаря'


@lead_time
def list_del_full(lst):
    lst.clear()
    return 'Удаление списка'


@lead_time
def dict_del_full(dicts):
    dicts.clear()
    return 'Удаление словаря'


print(lst_app(lst_result))
print(dict_app(dicts_result))
print('_______________________')
print(list_search_lst(lst_result))
print(list_search_dict(dicts_result))
print('_______________________')
print(list_in(lst_result))
print(dict_in(dicts_result))
print('_______________________')
print(list_del(lst_result))
print(dict_del(dicts_result))
print('_______________________')
print(list_del_full(lst_result))
print(dict_del_full(dicts_result))
print('_______________________')
print('a) Заполнение списка быстре так,как в словаре создаются ещё хеши')
print('б) 1) Поиск по словарю так, как он поддерживает произвольный доступ.\n 2) При добавлении в конец быстрее список так, как создаются хеши.\n 3) А в удаление с конца уже быстрее словарь так, как имеет произвольный доступ.\n 4) И наконец удаление быстрее у списка так,как словарь удаляет хеш.\n Итог стоит их комбинировать. Например вставить данные в середину словаря это тяжелая задача')

