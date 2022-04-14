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

from time import time
from random import randint


def time_logger(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        ent_time = time()
        print(f'Время работы функции {func.__name__} составило {ent_time - start_time}')
        return result

    return inner


@time_logger
def fill_dict(dict_for_fill):
    for i in range(100000):
        dict_for_fill[i] = randint(0, 100000)  # сложность d[k] = v константная O(1)


@time_logger
def fill_list(list_for_fill):
    for _ in range(100000):
        list_for_fill.append(randint(0, 100000))  # сложность .append константная O(1)


@time_logger
def test_dict_read(dict_to_test):
    for i in range(len(dict_to_test)):
        _ = dict_to_test.get(i)  # O(1)


@time_logger
def test_dict_update(dict_to_test):
    for i in range(len(dict_to_test)):
        dict_to_test[i] = 'test'  # O(1)


@time_logger
def test_dict_remove(dict_to_test):
    for i in range(20000, 30000):
        dict_to_test.pop(i)  # O(1)


@time_logger
def test_list_read(list_to_test):
    for i in range(len(list_to_test)):
        _ = list_to_test[i]  # O(1)


@time_logger
def test_list_update(list_to_test):
    for i in range(len(list_to_test)):
        list_to_test[i] = 'test'  # O(1)


@time_logger
def test_list_remove(list_to_test):
    for i in range(20000, 30000):
        list_to_test.pop(i)  # O(n)


random_numbers_dict = {}
random_numbers_list = []

fill_dict(random_numbers_dict)
fill_list(random_numbers_list)

"""
Время работы функции fill_dict составило 0.0969991683959961
Время работы функции fill_list составило 0.09162187576293945

Мы видим, что времена работы функций практически совпадают - это подтверждает равенство алгоритмических сложностей
Однако в случае работы со списком время работы несколько меньше, это происходит из-за накладных расходов по вычислению хешей
"""

test_dict_read(random_numbers_dict)
test_list_read(random_numbers_list)

test_dict_update(random_numbers_dict)
test_list_update(random_numbers_list)

test_dict_remove(random_numbers_dict)
test_list_remove(random_numbers_list)

"""
Время работы функции test_dict_read составило 0.007003307342529297
Время работы функции test_list_read составило 0.0039980411529541016
Время работы функции test_dict_update составило 0.0069658756256103516
Время работы функции test_list_update составило 0.005000591278076172
Время работы функции test_dict_remove составило 0.0010006427764892578
Время работы функции test_list_remove составило 0.16703534126281738

Операция удаления из середины списка занимает намного больше времени, чем операция удаления из середины словаря
Остальные операции работают примерно одинаково
"""