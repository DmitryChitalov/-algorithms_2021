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

import random
import time


def timer(func):
    def wrapped(*args):
        start = time.perf_counter_ns()
        res = func(*args)
        print(f'{(time.perf_counter_ns() - start) / 1000000}ms')
        return res

    return wrapped


# Сложность O(n), т.к. для заполнения используется цикл.
# Время выполнения обеих функций примерно одинаковое, но при малом количестве элементов заполнение словаря происходит
# чуть медленнее, видимо из-за того, что это хэш-таблица.
@timer
def dict_fill(length):
    return {idx: random.randint(0, 100) for idx in range(length)}


# Сложность O(n).
@timer
def list_fill(length):
    return [random.randint(0, 100) for _ in range(length)]


# O(1)
@timer
def dict_get(dict, idx):
    return dict[idx]


# O(1)
@timer
def list_get(list, idx):
    return list[idx]


# O(n)
@timer
def dict_del(dict, count):
    for i in range(count):  # O(n)
        del dict[i]  # O(1)
    return dict


# O(n^2)
@timer
def list_del(list, count):
    for i in range(count):  # O(n)
        del list[i]  # O(n)
    return list


# O(n)
@timer
def dict_add(dict, count):
    last_el = list(new_dict)[-1]
    for i in range(count):
        dict[last_el + i] = random.randint(0, 100)
    return dict


# O(n)
@timer
def list_add(list, count):
    for _ in range(count):
        list.append(random.randint(0, 100))
    return list


delimiter = '\n----------------------------------------------------------------------'

new_dict = dict_fill(2000)
print(f'Заполнение словаря:\n{new_dict}{delimiter}')

new_list = list_fill(2000)
print(f'Заполнение списка:\n{new_list}{delimiter}')

print(f'Получение элемента словаря:\n{dict_get(new_dict, 7)}{delimiter}')
print(f'Получение элемента списка:\n{list_get(new_list, 7)}{delimiter}')
print(f'Добавление элемента словаря:\n{dict_add(new_dict, 2000)}{delimiter}')
print(f'Добавление элемента списка:\n{list_add(new_list, 2000)}{delimiter}')
print(f'Удаление элемента словаря:\n{dict_del(new_dict, 2000)}{delimiter}')
print(f'Удаление элемента списка:\n{list_del(new_list, 2000)}{delimiter}')
