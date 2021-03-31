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

def time_decor(func):
    def timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return timer

@time_decor
def list_f(lenght):
    result = []
    for i in range(length):
        result.append(i)
    return result

@time_decor
def dict_f(length):
    result = {}
    for i in range(length):
        result[i] = f'number {i}'
    return result

@time_decor
def check_d_key(d_obj):
    j = d_obj[4000]
    print(j)

@time_decor
def check_l_ind(l_obj):
    for i in range(len(l_obj)):
        if i == 4000:
            print(l_obj[i])

@time_decor
def check_d_val(d_obj):
    for j in d_obj.values():
        if j == 'number 4000':
            print(j)

@time_decor
def check_l_val(l_obj):
    for j in l_obj:
        if j == 4000:
            print(j)

list1, list1_time = list_f(5000)
dict1, dict1_time = dict_f(5000)
print('List time at 5000', list1_time)
print('Dictionary time at 5000', dict1_time)

list2, list2_time = list_f(50000)
dict1, dict2_time = dict_f(50000)
print('List time at 50000', list1_time)
print('Dictionary time at 50000', dict1_time)

#добавление элементов в словарь занимает больше времени так как к ним нужно посчитать хеш у ключей

print('Index in List 5000 time', check_l_ind(list1)[1])
print('Key in Dict 5000 time', check_d_key(dict1)[1])
print('Index in List 50000 time', check_l_ind(list2)[1])
print('Key in Dict 50000 time', check_d_key(list2)[1])

#поиск в словаре происходит быстрее так как он по ключу

print('Value in List 5000 time', check_l_val(list1)[1])
print('Value in Dict 5000 time', check_d_val(dict1)[1])
print('Value in List 50000 time', check_l_val(list2)[1])
print('Value in Dict 50000 time', check_d_val(list2)[1])

#искать через значения быстрее в списке
