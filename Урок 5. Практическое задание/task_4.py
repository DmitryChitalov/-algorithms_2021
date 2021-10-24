"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint

test_dict = {}

test_ord_dict = OrderedDict()


def dict_app():
    for i in range(1000):
        test_dict[f'key{i}'] = i
    print(test_dict)


print(f"Время заполнения dict: {timeit('dict_app', globals=globals(), number=100000000)}")


def ord_dict_app():
    for i in range(1000):
        test_ord_dict[f'key{i}'] = i
    print(test_ord_dict)


print(f"Время заполнения OrderedDict: {timeit('ord_dict_app', globals=globals(), number=100000000)}")

dict_app()
ord_dict_app()


def get_key_ord_dict():
    get_ord_dict = test_ord_dict[f'key{randint(1, 900)}']
    return get_ord_dict


def get_key_dict():
    get_dict = test_ord_dict[f'key{randint(1, 900)}']
    return get_dict


print(f"Время получения рандомного значения dict: {timeit('get_key_dict()', globals=globals(), number=1000000)}")

print(
    f"Время получения рандомного значения OrderedDict: {timeit('get_key_ord_dict()', globals=globals(), number=1000000)}")


def del_key_ord_dict():
    key_ord_dict = test_ord_dict.pop[f'key{randint(1, 900)}']
    return key_ord_dict


def del_key_dict():
    key_dict = test_ord_dict.pop[f'key{randint(1, 900)}']
    return key_dict


print(f"Время удаления рандомного ключа dict: {timeit('get_key_dict()', globals=globals(), number=1000000)}")

print(
    f"Время удаления рандомного ключа OrderedDict: {timeit('get_key_ord_dict()', globals=globals(), number=1000000)}")

"""
Время заполнения OrderedDict немного медленнее чем dict
Время удаления и получения значений примерно одинаково +/-.
Ранее OrderedDict имел преимущество в виде своей упорядоченности перед обынчый словарем, однако начиная с версии 
Python 3.6 dict тоже упорядочен. Этого преимущества более нет, может есть еще какие-то, я пока не знаю) 

"""
