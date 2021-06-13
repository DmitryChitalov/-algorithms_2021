"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
import collections

dict_1 = {}
dict_2 = collections.OrderedDict()


def fill_dict(my_dict):
    my_dict = {i: i for i in range(1000)}
    return my_dict


print("Заполнение словарей (1000 элементов, 10^4 повторов):")
print("Обычный словарь	-	", timeit("fill_dict(dict_1)", globals=globals(), number=10000))
print("OrderedDict  	-	", timeit("fill_dict(dict_2)", globals=globals(), number=10000))

print("\nПолучение элементов словарей (10^7 повторов):")
print("Обычный словарь	-	", timeit("a = dict_1.get(10)", globals=globals(), number=10000000))
print("OrderedDict  	-	", timeit("a = dict_2.get(10)", globals=globals(), number=10000000))

"""
Заполнение словарей (1000 элементов, 10^4 повторов):
Обычный словарь	-	 0.922228272
OrderedDict  	-	 0.862044895

Получение элементов словарей (10^7 повторов):
Обычный словарь	-	 0.7890700429999999
OrderedDict  	-	 0.7521764289999999

Операции заполнения и получения элементов выполняются для словарей OrderedDict немного быстрее, чем для обычных.
Соответственно, в Python 3.6 и более поздних версиях имеет смысл использовать OrderedDict при большом объеме операций 
со словарями, который критичен ко времени выполнения.

"""