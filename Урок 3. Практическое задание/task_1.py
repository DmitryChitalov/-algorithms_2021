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
lst = []
dic = []
# a)


def time_count(callback):
    def wrapper(object_):
        start_in = time.perf_counter()
        callback(object_)
        end_in = time.perf_counter() - start_in
        print(f'{end_in:.10f}')
        return object_
    return wrapper


@time_count
def list_ap(lst_in):     #O(1)
    for i in range(5):     #O(1)
        lst_in.append(i)    #O(1)
    lst.append(lst_in)     #O(1)
    return lst_in          #O(1)


@time_count
def dic_ap(dic_in):              #O(1)
    for i in range(5):             #O(1)
        dic_in.update({i: i})       #O(1)
    dic.append(dic_in)             #O(1)
    return dic_in                  #O(1)


print(list_ap([]))
print(dic_ap({}))

# б)


@time_count
def list_in(lst_method):               #O(1)
    for el in range(len(lst_method)):    #O(1)
        lst_method.pop()                #O(1)
    return lst_method                   #O(1)


@time_count
def dic_in(dic_method):                #O(1)
    for el in range(len(dic_method)):      #O(1)
        dic_method.popitem()                 #O(1)
    return dic_method                      #O(1)


print(list_in(lst[0]))
print(dic_in(dic[0]))