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
import random
import math

# Заполнение списка
def list_fill():
    """

    Выполняется медленнее,
    поскольку в основе списков лежат динамические массивы.
    """

    start_val = time.time()
    list_obj = [el for el in range(1, 11)]
    end_val = time.time()
    print(f'Время наполнения списка составило - {end_val - start_val}')
    return list_obj

# Заполнение словаря
def dict_fill():
    """

    Выполняется быстрее,
    поскольку реализуется через хеш-таблицу.
    """

    start_val = time.time()
    dict_obj = {el: random.randint(0,20) for el in range(1, 11)}
    end_val = time.time()
    print(f'Время наполнения словаря составило - {end_val - start_val}')
    return dict_obj

# Поиск элемента списка по индексу
def some_list_el(list_obj, i):
    """

    Реализуется медленнее,
    за линейное время - O(log n) -
    необходимо сравнивать индекс с каждым средним значением после отсекания половины.
    """

    start_val = time.time()
    start_point = 0
    end_point = len(list_obj) - 1
    result = 0
    while start_point <= end_point:
        mid = math.floor(int((start_point + end_point) / 2))
        if list_obj[mid] == i:
            result = i
            break
        elif list_obj[mid] < i:
            start_point = mid + 1
        else:
            end_point = mid - 1
    end_val = time.time()
    return result, end_val - start_val

# Поиск значения элемента словаря по ключу
def some_dict_el(dict_obj, k):
    """

    Реализуется быстрее,
    за константное время - O(1) - сразу возвращает значение по хешу ключа.
    """

    start_val = time.time()
    result = dict_obj.get(k)
    end_val = time.time()
    return result, end_val - start_val


if __name__ == '__main__':
    some_list = list_fill()
    some_dict = dict_fill()

    list_el, list_time = some_list_el(some_list, 3)
    dict_el, dict_time = some_dict_el(some_dict, 5)

    print(f'Элемент списка с индексом 5 - {list_el}, время выполнения операции - {list_time}')
    print(f'Значение элемента словаря с ключем 5 - {dict_el}, время выполнения операции - {dict_time}')

