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
from time import time as time


def timer(func):
    def temporary(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        return result

    return temporary


@timer
def list_creating(n):
    func_list = [i for i in range(n)]
    return func_list


@timer
def dict_creating(n):
    func_dict = {i: '' for i in range(n)}
    return func_dict


@timer
def search_in_list(func_list, n):
    if n - 1 in func_list:
        return True
    else:
        return False


@timer
def search_in_dict(func_dict, n):
    if n - 1 in func_dict:
        return True
    else:
        return False


@timer
def remove_from_list(func_list, n):
    for i in range(n):
        func_list.remove(i)


@timer
def pop_from_list(func_list, n):
    for i in range(n):
        func_list.pop()


@timer
def pop_from_dict(func_dict, n):
    for i in range(n):
        func_dict.pop(i)


@timer
def pop_item_from_dict(func_dict, n):
    for i in range(n):
        func_dict.popitem()


@timer
def list_copy(func_list):
    return func_list.copy()


@timer
def dict_copy(func_dict):
    return func_dict.copy()


n_for_timer = 1000000

list_for_timer = list_creating(n_for_timer)
dict_for_timer = dict_creating(n_for_timer)
# Словарь создаётся дольше, так как набор входящих данных больше. К каждому ключу создаётся хэш.
search_in_list(list_for_timer, n_for_timer)
search_in_dict(dict_for_timer, n_for_timer)
# Поиск в словаре осуществляется быстрее за счёт хэш-таблицей. В подавляющем числе случаев имеет константу равную нулю.
list_for_timer_copy = list_copy(list_for_timer)
dict_for_timer_copy = dict_copy(dict_for_timer)
# Словарь создаётся дольше, так как набор входящих данных больше. К каждому ключу создаётся хэш.
n_for_timer = 1000
# Для удаления из списка элемента по значению затрачивается гораздо больше времени,
# чем удаление последнего элемента с возвращением значения, так как в последнем не происходит поиска по значению,
# и длиннее по времени чем изъятие по ключу или изъятие последней пары ключ-значение из словаря.
remove_from_list(list_for_timer, n_for_timer)
pop_from_list(list_for_timer_copy, n_for_timer)
pop_from_dict(dict_for_timer, n_for_timer)  # высокая скорость благодаря хэшам
pop_item_from_dict(dict_for_timer_copy, n_for_timer)
'''При замерах последние три способа выдавали константу равную нулю.
При установлении большего значения n (=1000000, с небольшим отрывом самым быстрым оказывается pop_from_list
благодаря изъятию одного всегда последнего параметра, затем pop_item_from_dict и pop_from_dict,
которые имели очень близкие друг к другу значения времени.'''
