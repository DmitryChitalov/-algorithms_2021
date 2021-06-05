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


from random import randint
from time import time


def lead_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        delta_time = end_time - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        return res, delta_time
    return wrapper


@lead_time
def fill_dict():
    dict_obj = {}
    for i in range(10000):       # По хорошему должна быть зависима от аргумента и иметь O(N), но сейчас O(1)
        dict_obj[i] = randint(1, 100)   # Сложность О(1)
    return dict_obj


@lead_time
def fill_list():
    list_obj = []
    for i in range(10000):       # По хорошему должна быть зависима от аргумента и иметь O(N), но сейчас O(1)
        list_obj.insert(i, randint(1, 100))    # Сложность О(N)
    return list_obj


@lead_time
def max_dict(dict_obj):     # Сложность O(N^2)
    for i in dict_obj.values():     # Сложность O(N)
        is_max = True
        for n in dict_obj.values():     # Сложность O(N)
            if i < n:
                is_max = False
        if is_max:
            return i


@lead_time
def max_list(list_obj):     # Сложность O(N^2)
    for i in list_obj:      # Сложность O(N)
        is_max = True
        for n in list_obj:      # Сложность O(N)
            if i < n:
                is_max = False
        if is_max:
            return i


@lead_time
def avg_dict(dict_obj: dict):
    res = [0, 1]
    for key in dict_obj.keys():     # Сложность O(N)
        res[0] += dict_obj[key]     # Сложность О(1)
        res[1] += 1     # Сложность О(1)
    return res[0]/res[1]


@lead_time
def avg_list(list_obj):
    res = [0, 1]
    for val in list_obj:        # Сложность O(N)
        res[0] += val        # Сложность О(1)
        res[1] += 1      # Сложность О(1)
    return res[0]/res[1]


@lead_time
def del_el_dict(dict_obj: dict):
    [dict_obj.popitem() for _ in range(9500)]       # O(N)
    return dict_obj


@lead_time
def del_el_list(list_obj: list):
    [list_obj.pop() for _ in range(9500)]       # O(N)
    return list_obj


my_dict, delta_time_dict = fill_dict()
my_list, delta_time_list = fill_list()
print(f'Разница по времени наполнения объекта list и dict составляет {delta_time_list - delta_time_dict}\n')
'''
Наполнение словаря должно происходить быстрее, поскольку добавление нового эллемента в словарь
происходит через append со сложностью O(1), а в список с помощью конструкции insert имеющей сложность O(N),
но на всех замерах видно, что скорости получаются идентичными (+-).
Данная ситуация происходит из-за того что обычно insert используют для вставки эл-та не в конец словаря,
а при вставке не в конец, происходит переписывание индексов (что, наверное, и приводит к усложнению функции)
Правильнее будет описывать insert по анлогии c pop(), pop(n)
Insert проверил на 4х сайтах, везде указывается сложность O(N)
'''
my_max_dict, delta_time_dict = max_dict(my_dict)
my_max_list, delta_time_list = max_list(my_list)
print(f'Разница по времени определения max для объекта list и dict составляет {delta_time_list - delta_time_dict}\n')
'''
Поиск max имеет в обоих случаях одинаковую сложность, но за счет того что словари являются хеш таблицами,
то и перебор всех эл-тов в словарях должен происходить быстрее
но опираясь на цифры, создается ощущение, что данное преимущество будет действовать только при фактическом обращении
по индексу/ключу эл-та, в данному же случае, не происходит использование хэш функций, 
а скорее всего банальный перебор всех значений по индексу,
ну или возможно что хеш функции задействованы, но перебор у нас настолько линейный, что преимущество не заметно
'''

my_avg_dict, delta_time_dict = avg_dict(my_dict)
my_avg_list, delta_time_list = avg_list(my_list)
print(f'Разница по времени определения avg для объекта list и dict составляет {delta_time_list - delta_time_dict}\n')
'''
Ситуация полностью аналогичная функции max
'''

my_dict, delta_time_dict = del_el_dict(my_dict)
my_list, delta_time_list = del_el_list(my_list)
print(f'Разница по времени удаления эллементов объекта list и dict составляет {delta_time_list - delta_time_dict}\n')
"""
Разница настолько мала, что скорее всего в ней виноваты фоновые процессы ОС
"""
