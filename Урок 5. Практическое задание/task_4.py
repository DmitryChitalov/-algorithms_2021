"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint


def copy_dict(_dict):
    return _dict.copy()


def dict_get_values(_dict):
    return _dict.values()


def odict_get_values(_odict):
    return _odict.values()


def dict_get_keys(_dict):
    return _dict.keys()


def odict_get_keys(_odict):
    return _odict.keys()


def dict_get_random_values(_dict, n=100):
    return [_dict[str(randint(0, 9999))] for _ in range(n)]


def odict_get_random_values(_odict, n=100):
    return [_odict[str(randint(0, 9999))] for _ in range(n)]


def update_dict(dict_1, dict_2):
    dict_1.update(dict_2)


def update_odict(odict_1, odict_2):
    odict_1.update(odict_2)


test_dict = {str(key): value for key, value in enumerate(range(15000, 25000))}
test_odict = OrderedDict(test_dict)
test_dict_2 = copy_dict(test_dict)
test_odict_2 = copy_dict(test_odict)


print('copy Dict',
      timeit('copy_dict(test_dict)', number=10000, globals=globals()))
print('copy OrderedDict',
      timeit('copy_dict(test_odict)', number=10000, globals=globals()))
print('dict_get_values',
      timeit('dict_get_values(test_dict)', number=10000, globals=globals()))
print('odict_get_values',
      timeit('odict_get_values(test_odict)', number=10000, globals=globals()))
print('dict_get_keys',
      timeit('dict_get_keys(test_dict)', number=10000, globals=globals()))
print('odict_get_keys',
      timeit('odict_get_keys(test_odict)', number=10000, globals=globals()))
print('dict_get_random_values',
      timeit('dict_get_random_values(test_dict)', number=10000, globals=globals()))
print('odict_get_random_values',
      timeit('odict_get_random_values(test_odict)', number=10000, globals=globals()))
print('update_dict',
      timeit('update_dict(test_dict_2, test_dict)', number=10000, globals=globals()))
print('update_odict',
      timeit('update_odict(test_odict_2, test_odict)', number=10000, globals=globals()))

"""
Результаты:

copy Dict 0.9430522
copy OrderedDict 7.617558999999999
dict_get_values 0.0007614000000000232
odict_get_values 0.0007603000000013793
dict_get_keys 0.0008195000000004171
odict_get_keys 0.0007652000000000214
dict_get_random_values 0.7443015000000006
odict_get_random_values 0.7398331000000002
update_dict 1.6115407000000008
update_odict 5.591816099999999

Операции для копирования и обновления OrderedDict  работают намного медленее чем аналогичные для встроенного Словаря.
Операции по получению значений или ключей выполняются примерно за одинаковое время для обоих типов.
В целом, в связи с тем что с версии Python 3.6 Словари стали упорядоченными и более оптимизированными,
необходимость в коллекции OrderedDict отпала.

"""