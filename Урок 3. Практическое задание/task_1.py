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


def get_time_diff(fn):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        ret_val = fn(*args, **kwargs)
        print(f'Время, затраченное на выполнение операции: {time.time() - start_time} сек')
        return ret_val

    return wrapped


# Это моя первая попытка сделать обертку, до сих пор не сталкивался.
# Мне в этом коде непонятная излишняя вложенность. Вопрос: почему нельзя обойтись без
# wrapped? Т.е. сделать так:
# def get_time_diff(fn):
#    start_time = time.time()
#    fn()
#    return time.time() - start_time
# Интерпретатор ругается на ошибку TypeError: 'float' object is not callable. А в чем суть ошибки?


@get_time_diff
def make_list(items_count):
    print(f'Формируем список из {items_count} элементов')
    test_lst = []

    for i in range(items_count):
        test_lst.append(random.randint(0, i))

    return test_lst


@get_time_diff
def make_dict(items_count):
    print(f'Формируем словарь из {items_count} элементов')
    test_dct = {}

    for i in range(items_count):
        test_dct[i] = random.randint(0, i)

    return test_dct


@get_time_diff
def get_value_from_list(lst, n):
    print(f'Ищем значение {n} в сформированном списке')
    try:
        index_n = lst.index(n)
    except ValueError:
        index_n = -1

    return index_n


@get_time_diff
def get_value_from_dict(dct, n):
    print(f'Ищем значение {n} в сформированном словаре')
    return dct.get(n, 'Not found')


loc_items_count = 1000000
loc_lst = make_list(loc_items_count)
loc_dct = make_dict(loc_items_count)

print()
print(f'Позиция искомого элемента в словаре: {get_value_from_list(loc_lst, random.randint(0, loc_items_count))}')
print(f'Позиция искомого элемента в словаре: {get_value_from_dict(loc_dct, random.randint(0, loc_items_count))}')

# Разница в скорости заполнения списка и словаря - несколько десятых секунды на 1 млн элементов.
# И не всегда в пользу словаря. Т.е. сделать однозначный вывод о том, что работает быстрее, я не могу

# В случае поиска элемента в списке и словаре - однозначно выигрывает словарь с разницей в 4 порядка
