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


def get_time(func):

    def timer(*args, **kwargs):
        stat = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения операции {func.__name__}: {end - stat}')
    return timer

#a)
@get_time
def add_end_list(user_list, val):   #O(n)
    for i in range(val):            #O(n)
        user_list.append(i)         #O(1)


@get_time
def add_dict(user_dict, val):   #O(n)
    for i in range(val):        #O(n)
        user_dict[i] = i        #O(1)


@get_time
def insert_list(user_list, val):        #O(n)
    for i in range(val):                #O(n)
        user_list.insert(i, i)          #O(n)


@get_time
def insert_inception_list(user_list, val):      #O(n)
    for i in range(val):                        #O(n)
        user_list.insert(0, i)                  #O(n)


"""  
Время выполнения операции insert_inception_list: 0.04487800598144531
Время выполнения операции add_end_list: 0.000997781753540039
Время выполнения операции insert_list: 0.13862967491149902
Время выполнения операции add_dict: 0.000997304916381836

Из полученных результатов видно, что операция добавления елемента в словарь имеет сложность O(1), а ф-ия имеет
сложность O(n) и она выполняется быстрее, т.к. представляет собой хеш-таблицу
"""
a = []
b = {}
insert_inception_list(a, 10000)
add_end_list(a, 10000)
insert_list(a, 10000)
add_dict(b, 10000)

#b)
print('#' * 100)
user_list = [i for i in range(1000000)]
user_dict = {i: i for i in range(1000000)}

@get_time
def del_end_list(user_list, val):       #O(n)
    for i in range(val):                #O(n)
        user_list.pop()                 #O(1)


@get_time
def del_inception_list(user_list, val): #O(n)
    for i in range(val):                #O(n)
        user_list.pop(0)                #O(1)


@get_time
def del_index_list(user_list, val):     #O(n^2)
    for i in range(val):                #O(n)
        user_list.pop(i)                #O(n)


@get_time
def del_dict(user_dict, val):           #O(n)
    for i in range(val):                #O(n)
        user_dict.pop(i)                #O(1)

"""
Время выполнения операции del_inception_list: 5.632932186126709
Время выполнения операции del_end_list: 0.000995635986328125
Время выполнения операции del_index_list: 5.338723182678223
Время выполнения операции del_dict: 0.0009953975677490234

Из полученных результатов видно, что все операции удаления елемента из словаря имеет сложность O(1), а ф-ия имеет
сложность O(n) и она выполняется быстрее.
"""

del_inception_list(user_list, 10000)
del_end_list(user_list, 10000)
del_index_list(user_list, 10000)
del_dict(user_dict, 10000)