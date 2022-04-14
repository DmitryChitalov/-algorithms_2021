"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import cProfile
from collections import OrderedDict


def dict_input(number):
    my_dict = {}
    for i in number:
        my_dict[i] = i


def ordrdict_input(number):
    my_dict = OrderedDict(number)


def dict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def ordrdict_output(dictt):
    for i in dictt.items():
        a = i[0]
        b = i[1]


def main():
    my_dict = {}
    nums = [i for i in range(50000)]
    for i in nums:
        my_dict[i] = i
    dict_input(nums)
    ordrdict_input(my_dict)
    dict_output(my_dict)
    ordrdict_output(my_dict)

cProfile.run('main()')

# Результаты замеров указывают на то, что разница в работе словаря и OrderedDict примерно одинакова.
# На мой взягляд, использование OrderedDict не имеет особого смысла в новых версиях питона