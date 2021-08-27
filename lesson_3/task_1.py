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
    def inner(storage):
        start_time = time()
        result = func(storage)
        ent_time = time()
        print(f'Время работы функции {func} составило {ent_time - start_time}')
        return result

    return inner


@time_logger
def fill_dict(dict_for_fill):
    for i in range(100000):
        dict_for_fill[i] = randint(0, 100000)  # сложность d[k] = v константная O(1)


@time_logger
def fill_list(list_for_fill):
    for i in range(100000):
        list_for_fill.append(randint(0, 100000))  # сложность .append константная O(1)


@time_logger
def test_dict_read(dict_to_test):
    for i in range(len(dict_to_test)):
        _ = dict_to_test.get(i)  # O(1)


@time_logger
def test_dict_update(dict_to_test):
    for i in range(len(dict_to_test)):
        dict_to_test[i] += 1  # O(1)


@time_logger
def test_dict_remove(dict_to_test):
    for i in range(len(dict_to_test)):
        dict_to_test.pop(i)  # O(1)


@time_logger
def test_list_read(list_to_test):
    for i in range(len(list_to_test)):
        _ = list_to_test[i]  # O(1)


@time_logger
def test_list_update(list_to_test):
    for i in range(len(list_to_test)):
        list_to_test[i] += 1  # O(1)


@time_logger
def test_list_remove(list_to_test):
    for i in range(len(list_to_test) - 1, 0, -1):
        list_to_test.pop(i)  # O(1)


random_numbers_dict = {}
random_numbers_list = []

fill_dict(random_numbers_dict)
fill_list(random_numbers_list)

"""
Время работы функции <function fill_dict at 0x7ffbb81354c0> составило 0.8702378273010254
Время работы функции <function fill_list at 0x7ffbb81355e0> составило 0.8394103050231934

Мы видим, что времена работы функций практически совпадают - это подтверждает равенство алгоритмических сложностей
Однако в случае работы со списком время работы меньше, это происходит из-за накладных расходов по вычислению хешей
"""

test_dict_read(random_numbers_dict)
test_list_read(random_numbers_list)

test_dict_update(random_numbers_dict)
test_list_update(random_numbers_list)

test_dict_remove(random_numbers_dict)
test_list_remove(random_numbers_list)

"""
Время работы функции <function test_dict_read at 0x7fa478135700> составило 0.052471160888671875
Время работы функции <function test_list_read at 0x7fa478135a60> составило 0.04150986671447754
Время работы функции <function test_dict_update at 0x7fa478135820> составило 0.11693596839904785
Время работы функции <function test_list_update at 0x7fa478135b80> составило 0.08494210243225098
Время работы функции <function test_dict_remove at 0x7fa478135940> составило 0.10662388801574707
Время работы функции <function test_list_remove at 0x7fa478135ca0> составило 0.07581901550292969
"""