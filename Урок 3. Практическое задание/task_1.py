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

import time
import uuid


def count_time(f):
    def g(*args):
        start = time.time()
        result = f(*args)
        print(time.time() - start)
        return result
    return g

# a) Для заполнения словаря уходит больше времени.
# По всей видимости, дело это связано с вычислением и присвоением хэша.

@count_time
def fill_dict(*args):
    result = dict()
    for ar in args:  # O(n)
        result[ar] = 0  # O(1)
    return result


@count_time
def fill_list(*args):
    result = list()
    for ar in args:  # O(n)
        result.append(ar)  # O(1)
    return result

data = [uuid.uuid4() for a in range(1, 100000)]

my_dict = fill_dict(*data)
my_list = fill_list(*data)

# b) Удаление значенией из списка занимает намного больше времени

to_delete = data[:50000]

@count_time
def delete_from_dict(dict_ob, keys):
    """сложность O(n)"""
    for k in keys:
        del dict_ob[k]


@count_time
def delete_from_list(list_ob, keys):
    """сложность O(n^2)"""
    for k in keys:
        list_ob.remove(k)

delete_from_dict(my_dict, to_delete)
delete_from_list(my_list, to_delete)

# Аналогично метод pop для списка по индексу занимает больше времени, чем pop для словаря по ключу

@count_time
def pop_from_dict(dict_ob, keys):
    """сложность O(n)"""
    for k in keys:
        dict_ob.pop(k)


@count_time
def pop_from_list(list_ob, keys):
    """сложность O(n^2)"""
    for k in keys:
        list_ob.pop(k)


to_pop_dict = data[-10000:]
to_pop_list = [a for a in range(10000)]

pop_from_dict(my_dict, to_pop_dict)
pop_from_list(my_list, to_pop_list)

