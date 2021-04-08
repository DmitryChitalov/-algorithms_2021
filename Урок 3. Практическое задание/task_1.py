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


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Время выполнения {function.__name__}: {(time.perf_counter() - start_time):.4f} ')
        return res

    return wrapped


#  Есть несколько функций для манипуляций со списком и словарем
#  Каждую функцию обрамляем декоратором, тогда при вызове функции она увидит наличие декоратора и попытается его вызвать
@time_of_function
def fill_list(no_elements):
    l = [i for i in range(no_elements)]
    return l


@time_of_function
def fill_dict(no_elements):
    d = {i: 'some value' for i in range(no_elements)}
    return d


@time_of_function
def sel_list(lst, from_index, to_index):
    for i in range(from_index, to_index):
        elem = lst[i]


@time_of_function
def sel_dict(dct, from_index, to_index):
    for i in range(from_index, to_index):
        elem = dct[i]


@time_of_function
def del_list(lst, from_index, to_index):
    for _ in range(from_index, to_index):
        del lst[from_index]  # Удаляем всегда тот же элемент, т.к. список схлопывается после каждого удаления.
    return lst


@time_of_function
def del_dict(dct, from_index, to_index):
    for i in range(from_index, to_index):
        del dct[i]
    return dct


my_list = fill_list(1000000)
print(f'Длина списка: {len(my_list)}')
my_dict = fill_dict(1000000)
print(f'Длина словаря: {len(my_dict)}')
sel_list(my_list, 300000, 800000)
sel_dict(my_dict, 300000, 800000)
del_list(my_list, 300000, 800000)
print(f'Длина списка после удвления элементов: {len(my_list)}')
del_dict(my_dict, 300000, 800000)
print(f'Длина словаря после удвления элементов: {len(my_dict)}')

"""
Время выполнения fill_list: 0.0780 
Длина списка: 1000000
Время выполнения fill_dict: 0.0958 
Длина словаря: 1000000
Время выполнения sel_list: 0.0194 
Время выполнения sel_dict: 0.0265 
Время выполнения del_list: 70.0027 
Длина списка после удвления элементов: 500000
Время выполнения del_dict: 0.0377 
Длина словаря после удвления элементов: 500000


ВЫВОДЫ: 
1) Операции формирования списка и словаря практически сравнимы по времени, что интересно. Получается, 
что формирование хэш-таблицы плюс запись значения атрибута для кэш-значеия ключа не занимает много времени. 
2) Чтение списка и словаря практически олинаково быстры, но у списка чуть лучше, т.к. не надо тратить время 
на вычисление хэша 
3) С удалением мы видим катастрофическое преимущество словаря, т.к. сложности удаления элементов для списка и словаря 
соотносятся как O(n) к O(1) 
"""
