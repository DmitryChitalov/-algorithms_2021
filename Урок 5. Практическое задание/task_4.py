"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def add_elem_dict(dict_, elem):
    dict_.update(elem)


def add_elem_ord_dict(dict_, elem):
    dict_.update(elem)


def pop_elem_dict(dict_, elem):
    dict_.pop(elem)


def pop_elem_ord_dict(dict_, elem):
    dict_.pop(elem)


def pop_item_dict(dict_):
    dict_.popitem()


def pop_item_ord_dict(dict_):
    dict_.popitem()


def get_dict_element(dict_):
    dict_.get('500')


def get_ordered_dict_element(dict_):
    dict_.get('500')


my_dict = {str(i): i for i in range(10000)}
my_o_dict = OrderedDict([(str(i), i) for i in range(10001)])

elem_ = {'15': 15}

print('Поиск элемента: ')
print(f"обычный словарь: {timeit('get_dict_element(my_dict)', globals=globals(), number=100000)}")
print(f"упорядоченный словарь: {timeit('get_ordered_dict_element(my_o_dict)', globals=globals(), number=100000)}")

print('Добавление элемента')
print(f"обычный словарь: {timeit('add_elem_dict(my_dict, elem_)', globals=globals(), number=100000)}")
print(f"упорядоченный словарь: {timeit('add_elem_ord_dict(my_o_dict, elem_)', globals=globals(), number=100000)}")
print("удаление элемента с хвоста")
print(f"обычный словарь: {timeit('pop_item_dict(my_dict)', globals=globals(), number=10000)}")
print(f"упорядоченный словарь: {timeit('pop_item_ord_dict(my_o_dict)', globals=globals(), number=10000)}")

my_dict = {str(i): i for i in range(10000)}
my_o_dict = OrderedDict([(str(i), i) for i in range(10001)])
print("Поиск и удаление элемента по ключу")
print(f"обычный словарь: {timeit('pop_elem_dict(my_dict, list(my_dict.keys())[0])', globals=globals(), number=10000)}")
print(
    f"упорядоченный словарь: "
    f"{timeit('pop_elem_ord_dict(my_o_dict, list(my_o_dict.keys())[0])', globals=globals(), number=10000)}")

"""
Вывод. Структура данных OrderedDict значительно уступает по скорости обычному словарю в python. 
Нет смысла использовать эту структуру.
"""
