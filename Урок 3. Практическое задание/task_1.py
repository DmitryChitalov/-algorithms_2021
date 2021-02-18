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


from sys import getsizeof
from time import time


def time_memory(func_to_check):
    def time_check(*args):
        start = time()
        func = func_to_check(*args)
        end = time()
        memory = getsizeof(func)
        return end - start, func, memory

    return time_check


@time_memory
def list_filler(a):
    my_list = []
    for i in range(1, a + 1):
        my_list.append(i)
    return my_list


@time_memory
def dict_filler(a):
    my_dict = {}
    for i in range(1, a + 1):
        my_dict[i] = f'{i}'
    return my_dict


n = 1000000
list_time, new_list, list_memory = list_filler(n)
dict_time, new_dict, dict_memory = dict_filler(n)

print(f'Время на список: {list_time}\nПамять на список: {list_memory}')
print(f'Время на словарь: {dict_time}\nПамять на словарь: {dict_memory}')


'''
Судя по полученным результатам, список и занимает меньше памяти, и быстрее выполняется,
так как словарь при заполнении генерирует хеши для своих ключей, что занимает как время,
так и память
'''


@time_memory
def find_list(obj, el):
    return obj.index(el)


@time_memory
def find_dict(obj, el):
    return obj.get(el)


el_ind = 984000
list_time, list_el, list_memory = find_list(new_list, el_ind)
dict_time, dict_el, dict_memory = find_dict(new_dict, el_ind)

print(f'Время на поиск в списке: {list_time}\nПамять на поиск в списке: {list_memory}')
print(f'Время на поиск в словаре: {dict_time}\nПамять на поиск в словаре: {dict_memory}')


@time_memory
def pop_list(obj, el):
    return obj.pop(el)


@time_memory
def pop_dict(obj, el):
    return obj.pop(el)


list_time, list_popped, list_memory = find_list(new_list, el_ind)
dict_time, dict_popped, dict_memory = find_dict(new_dict, el_ind)

print(f'Время на получение элемента в списке: {list_time}\nПамять на получение элемента в списке: {list_memory}')
print(f'Время на получение элемента в словаре: {dict_time}\nПамять получение элемента в словаре: {dict_memory}')

'''
Здесь мы видим, что поиск и взятие элемента в словаре так же занимает больше памяти, 
но по времени они происходят быстрее, так как имеются те самые хеши
'''
