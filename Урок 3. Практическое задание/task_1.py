#!/usr/bin/env python3

import time

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

l = list()
d = dict()

size = 100000000


def work_time(function):
    def wrapper(obj):
        start = time.time()
        function(obj)
        print(f'Время выполнения ({function.__name__}): {time.time() - start}')

    return wrapper


@work_time
def fill_list(obj):  # O(1)
    for i in range(size):  # O(1)
        obj.append(i)  # O(1)


@work_time
def fill_dict(obj):  # O(1)
    for i in range(size):  # O(1)
        obj[i] = i  # O(1)


@work_time
def change_list(obj):  # O(1)
    for i in range(size):  # O(1)
        obj[i] = i + 1  # O(1)


@work_time
def change_dict(obj):  # O(1)
    for i in range(size):  # O(1)
        obj[i] = i + 1  # O(1)


@work_time
def clear_list(obj):  # O(1)
    for _ in range(size):  # O(1)
        obj.pop()  # O(1)


@work_time
def clear_dict(obj):  # O(1)
    for i in range(size):  # O(1)
        obj.pop(i)  # O(1)


def main():
    fill_list(l)
    fill_dict(d)

    change_list(l)
    change_dict(d)

    clear_list(l)
    clear_dict(d)


if __name__ == '__main__':
    main()

# Время выполнения (fill_list): 8.182948350906372
# Время выполнения (fill_dict): 21.779764413833618
# Время выполнения (change_list): 12.790605545043945
# Время выполнения (change_dict): 25.57871103286743
# Время выполнения (clear_list): 8.809998035430908
# Время выполнения (clear_dict): 11.237062454223633
# Алгоритмическая сложность в обоих случаях одинакова но работа с list происходит быстрее
