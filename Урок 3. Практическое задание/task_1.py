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

import random
import time

def time_cut(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        end = time.time_ns()
        print(f'[*] Время выполнения функции <{func.__name__}>: {(end -start)} нс.')
        return res
    return wrapper

@time_cut
def fill_dict(range_start, range_end):
    my_dict = {x: random.randint(1, 100) for x in range(range_start, range_end)}
    return my_dict

@time_cut
def fill_list(range_num):
    my_list = [random.randint(1, 100) for i in range(range_num)]
    return my_list

@time_cut
def extend_list(my_list, ext_list):
    my_list.extend(ext_list)
    return my_list

@time_cut
def extend_dict(my_dict, ext_dict):
    my_dict.update(ext_dict)
    return my_dict

@time_cut
def del_from_list(my_list, num):
    print(my_list.pop(num))
    return my_list

@time_cut
def del_from_dict(my_dict, key):
    print(my_dict.pop(key))
    return my_dict


print("Создаем словарь и список")
first_dict = fill_dict(1, 1000000)
first_list = fill_list(1000000)

print("Создаем словарь и список для добавления")
ext_dict = fill_dict(1, 1000000)
ext_list = fill_list(1000000)

print("Объяединяем словари")
first_dict = extend_dict(first_dict, ext_dict)

print("Объединяем списоки")
first_list = extend_list(first_list, ext_list)

print("Удаление из словаря/списка элемента с ключом 30000/индексом 30000")
first_dict = del_from_dict(first_dict, 30000)
first_list = del_from_list(first_list, 30000)


'''
Операции со словорями занимают немногим больше времени из-за необходимости добавления ключа,сложность одинаковая
Объединение словарей происходит обычно справа налево,если есть общий ключ,то значение второго словаря перезаписывает
значение первого
Удаление из списка дольше (O(N))
Удаление из словаря (О(1))
От сложности наверное и разница во времени
'''