from collections import OrderedDict
from timeit import timeit

"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


def my_values(some):
    return some.values()


def my_keys(some):
    return some.keys()


def my_items(some):
    return some.items()


def my_popitem(some):
    return some.popitem()


def my_copy(some):
    return some.copy()


def my_update(dict_1, dict_2):
    return dict_1.update(dict_2)


usr_dict = {'Key_' + str(i-999): i for i in range(1000, 5000)}
usr_ord_dict = OrderedDict(usr_dict)

dict_1 = my_copy(usr_dict)
dict_2 = my_copy(usr_dict)
ord_dict_1 = my_copy(usr_ord_dict)
ord_dict_2 = my_copy(usr_ord_dict)

print(f"my_values(dict): {timeit('my_values(usr_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_values(ord_dict): {timeit('my_values(usr_ord_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_keys(dict): {timeit('my_keys(usr_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_keys(ord_dict): {timeit('my_keys(usr_ord_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_items(dict): {timeit('my_items(usr_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_items(ord_dict): {timeit('my_items(usr_ord_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_copy(dict): {timeit('my_copy(usr_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_copy(ord_dict): {timeit('my_copy(usr_ord_dict)', globals=globals(), number=10000)} sec.\n"
      f"my_update(dict): {timeit('my_update(dict_1, dict_2)', globals=globals(), number=10000)} sec.\n"
      f"my_update(ord_dict): {timeit('my_update(ord_dict_1, ord_dict_2)', globals=globals(), number=10000)} sec.\n")

"""
Необходимисти в OrderedDict так, как в Python 3.6+ библиотеки и так упорядоченные. Все функции выполняются примерно
одинакого(по времени), кроме функций copy и update, в OrderedDict они выпоняются существенно дольше
"""