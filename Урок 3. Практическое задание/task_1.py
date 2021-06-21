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
from random import randint, random, choice
import string

def get_time_count(f): # создание функции для замеров времени и использования в качестве декоратора
    def t(obj):
        start_time = time.time()
        f(obj)
        end_time = time.time()
        return end_time - start_time, type(obj)
    return t

# a) заполнение списка и словаря:

# Заполнение списка (несколько вариантов):
# с использованием randint для заполнения числовыми значениями:
@get_time_count
def get_list_filled_1(list_obj, n=10000):  # n - количество элементов списка
    list_obj = [randint(-n, n) for _ in range(n)]
    return list_obj

list_1 = []

print('Заполнение списка:')
print(get_list_filled_1(list_1))  # каждый вызов показвает разное время разное время

# с использованием random для заполнения числовыми значениями:
@get_time_count
def get_list_filled_2(list_obj, n=10000):
    for _ in range(n):
        new = int(random() * 1000 + 1)
        list_obj.append(new)
    return list_obj

list_2 = []
print((get_list_filled_2(list_2)))# каждый вызов показвает разное время разное время


# с использованием choice для заполнения строковыми значениями и random для определения длины строки:
@get_time_count
def get_list_filled_3(list_obj, n=10000):
    l = string.ascii_lowercase
    for _ in range(n):
        str_el_len = int(random() * 5 + 1)
        new_str_el = ''.join(choice(l) for i in range(str_el_len))
        list_obj.append(new_str_el)
    return list_obj

list_3 = []

print(get_list_filled_3(list_3))
print()


# Заполнение словаря:
# использую choice для генерации ключей, random - для длины ключа и для генерации значений словаря:
@get_time_count
def get_dict_filled(dict_obj, n=10000):
    l = string.ascii_lowercase
    for _ in range(n):
        str_key_len = int(random() * 5 + 1)
        new_dict_el = dict.fromkeys([''.join(choice(l) for i in range(str_key_len))], int(random() * 1000 + 1))
        dict_obj.update(new_dict_el)
    return dict_obj

dict_1 = {}

print('Заполнение словаря:')
print(get_dict_filled(dict_1))
print()

# Примечание: отказалась от вывода заполненных списков и словаря, так как на значениях n <= 2000
# результат затраченного времени часто был -  0.0. На больших n этой проблемы не стало, однако
# количество выводимых элементов делает вывод не информативным.

# Вывод: на заполнение словарей уходит гораздо больше времени, и если даже сложить время на создание
# списка строковых значений и списка числовых значений (2 и 3 вариант заполнения словаря),
# полученное время будет почти в 2 раза меньше, чем на создание словаря с таким же количеством элементов.
# это связано с тем, что словарь реализован в виде хеш-таблицы, с открытой адресацией и
# встроенным методом разрешения коллизий, и требует больше памяти,
# т.к. хеш-таблица должна быть достаточно большой.


# b) выполние операций со списком, словарем:
# операции со списком:

@get_time_count
def get_list_modified(list_obj): # с выводом результатов изменений
    list_test = list_obj.copy()
    list_test.clear()
    list_obj.sort()
    list_obj.append(int(random() * 1000 + 1))
    list_obj.extend([1,400])
    list_obj.insert(int(random() * len(list_obj)), 'gffh')
    list_obj.remove('gffh')
    print(list_obj.pop(list_obj.index(400)))
    print(list_obj.index(list_obj[int(random() * len(list_obj))]))
    print(list_obj.count(list_obj[0]))
    list_obj.reverse()
    print(list_obj)
    return list_obj


@get_time_count
def get_list_modified_1(list_obj): # без вывода результатов изменений
    list_test = list_obj.copy()
    list_test.clear()
    list_obj.sort()
    list_obj.append(int(random() * 1000 + 1))
    list_obj.extend([1,400])
    list_obj.insert(int(random() * len(list_obj)), 'gffh')
    list_obj.remove('gffh')
    list_obj.pop(list_obj.index(400))
    list_obj.index(list_obj[int(random() * len(list_obj))])
    list_obj.count(list_obj[0])
    list_obj.reverse()
    return list_obj

print('Изменение списка: операции со списком: ')
print(get_list_modified(list_2))
print(get_list_modified_1(list_2))
print()

# операции со словарем:
@get_time_count
def get_dict_modified(dict_obj): # с выводом результатов изменений
    dict_test = dict_obj.copy()
    dict_test.clear()
    dict_obj.update([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
    print(dict_obj.items())
    print(dict_obj.keys())
    print(dict_obj.values())
    print(dict_obj.pop('two'))
    print(dict_obj.popitem()) # удаляет и возвращает ключ-значение с конца словаря
    print(dict_obj.setdefault('three'))
    print(dict_obj)
    return dict_obj

print('Изменение словаря: операции со словарем: ')

print(get_dict_modified(dict_1))

@get_time_count
def get_dict_modified_1(dict_obj): # без вывода результатов изменений
    dict_test = dict_obj.copy()
    dict_test.clear()
    dict_obj.update([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
    dict_obj.items()
    dict_obj.keys()
    dict_obj.values()
    dict_obj.pop('two')
    dict_obj.popitem() # удаляет и возвращает ключ-значение с конца словаря
    dict_obj.setdefault('three')
    return dict_obj

print()
print(get_dict_modified_1(dict_1))

# Вывод: операции со словарями требуют гораздо меньше времени, чем операции со списками
# (если не требуется выводить результаты!!!!), так как благодаря константной сложности и применении хеша
# для быстрого сравнения ключей  в словарях обеспечивается быстрый поиск по ключу.