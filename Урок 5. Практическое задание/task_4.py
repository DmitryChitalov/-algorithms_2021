"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def create_dict():
    std_dict = {}
    for i in range(1000):
        std_dict[i] = 'a'
    return std_dict


def create_od_dict():
    od_dict = OrderedDict()
    for i in range(1000):
        od_dict[i] = 'a'
    return od_dict


def get_values(obj):
    return obj[0]


def get_values_od(obj):
    return obj[0]


def del_key_dict(obj):
    for i in range(10):
        obj.pop(i)


def del_key_od(obj):
    for i in range(10):
        obj.pop(i)


new_dict = create_dict()
new_od_dict = create_od_dict()
print(f"Создание словаря через dict: "
      f"{timeit('create_dict()', number=10000, globals=globals())}")
print(f"Создание словаря через OrderDict: "
      f"{timeit('create_od_dict()', number=10000, globals=globals())}")
print(f"Получение элемента из словаря через dict: "
      f"{timeit('get_values(new_dict)', number=10000000, globals=globals())}")
print(f"Получение элемента из словаря через OrderDict: "
      f"{timeit('get_values_od(new_od_dict)', number=10000000, globals=globals())}")
print(f"Удаление элемента из словаря через dict: "
      f"{timeit('del_key_dict(new_dict)', number=1, globals=globals())}")
print(f"Удаление элемента из словаря через OrderDict: "
      f"{timeit('del_key_od(new_od_dict)', number=1, globals=globals())}")


"""
По всем замерам OrderDict уступает стандартному словарю. 
Считаю что использовать его нужно только где это реально необходимо. 
"""
