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


def measure_time(func):
    def f(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        end_time = time.perf_counter_ns()
        return res, end_time - start_time

    return f


@measure_time
def fill_list_1(n):
    """
    Сложность О(1), так как n заранее известна
    """
    res = []
    for i in range(n):
        res.append(f'value {i}')
    return res


@measure_time
def fill_dict_1(n):
    """
    Сложность О(1), так как n заранее известна
    """
    res = {}
    for i in range(n):
        res[f'value {i}'] = i
    return res


@measure_time
def fill_list_2(n):
    """
    Сложность О(1), так как n заранее известна
    """
    return [f'value {i}' for i in range(n)]


@measure_time
def fill_dict_2(n):
    """
    Сложность О(1), так как n заранее известна
    """
    return {f'value {i}': i for i in range(n)}


@measure_time
def insert_el_list(data, el, pos):
    data.insert(pos, el)  # O(N)


@measure_time
def insert_el_dict(data, key, value):
    data.update(key=value)  # O(1)


@measure_time
def get_el_list(data, pos):
    return data[pos]  # O(1)


@measure_time
def get_el_dict(data, key):
    return data.get(key)  # O(1)


@measure_time
def remove_el_list(data, pos):
    data.pop(pos)  # O(N)


@measure_time
def remove_el_dict(data, key):
    data.pop(key)  # O(1)


N = 10000

_, timer_list = fill_list_1(N)
_, timer_dict = fill_dict_1(N)
print('Словарь наполняется быстрее') if timer_dict < timer_list else print('Список наполняется быстрее')

list_data, timer_list = fill_list_2(N)
dict_data, timer_dict = fill_dict_2(N)
print('Словарь наполняется быстрее') if timer_dict < timer_list else print('Список наполняется быстрее')
# Список наполняется быстрее при одинаковой сложности функций, при одинаковых данных,
# так как для наполнения словаря необходимо вычисление хеш-фунцкций

timer_list = insert_el_list(list_data, 'value', 500)
timer_dict = insert_el_dict(dict_data, 'key', 'value')
print('В словарь данные вставляются быстрее') if timer_dict < timer_list else print(
    'В список данные вставляются быстрее')

_, timer_list = get_el_list(list_data, 777)
_, timer_dict = get_el_dict(dict_data, 'value 777')
print('Из словаря данные получаются быстрее') if timer_dict < timer_list else print(
    'Из списка данные получаются быстрее')
# Из списка быстрее, так как получается элемент по индексу, т.е. О(1), как и у dict.get()

timer_list = remove_el_list(list_data, 777)
timer_dict = remove_el_dict(dict_data, 'value 777')
print('Из словаря данные удаляются быстрее') if timer_dict < timer_list else print(
    'Из списка данные удаляются быстрее')
