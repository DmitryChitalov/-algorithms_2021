"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

my_dict = {}
my_dict['bb'] = 22
my_dict['aa'] = 11
my_dict['dd'] = 44
my_dict['cc'] = 33

order_dict = OrderedDict()
order_dict['bb'] = 22
order_dict['aa'] = 11
order_dict['dd'] = 44
order_dict['cc'] = 33

# добавление пары ключ
print("#" * 100)
print("добавление пары ключ")
print(timeit("my_dict['qq'] = 33", number=1000000, globals=globals()))
print(timeit("order_dict['qq'] = 33", number=1000000, globals=globals()))

# изменние ключа
print("#" * 100)
print("изменние ключа")
print(timeit("my_dict['bb'] = 1", number=1000000, globals=globals()))
print(timeit("order_dict['bb'] = 1", number=1000000, globals=globals()))

# полусение значения по ключу
print("#" * 100)
print("полусение значения по ключу get()")
print(timeit("my_dict.get('cc')", number=10000000, globals=globals()))
print(timeit("order_dict.get('cc')", number=10000000, globals=globals()))

# возвращает пары
print("#" * 100)
print("возвращает пары items()")
print(timeit("my_dict.items()", number=10000000, globals=globals()))
print(timeit("order_dict.items()", number=10000000, globals=globals()))

# возвращает ключи в словаре
print("#" * 100)
print("возвращает ключи в словаре keys()")
print(timeit("my_dict.keys()", number=10000000, globals=globals()))
print(timeit("order_dict.keys()", number=10000000, globals=globals()))

# обновление словаря
print("#" * 100)
print("обновление словаря update()")
print(timeit("my_dict.update()", number=10000000, globals=globals()))
print(timeit("order_dict.update()", number=10000000, globals=globals()))

# удаляем пару ключ
print("#" * 100)
print("удаляем пару ключ")
print(timeit("my_dict.popitem()", number=4, globals=globals()))
print(timeit("order_dict.popitem()", number=4, globals=globals()))

"""
Изменение ключа и добавление нового элемента работает быстрее в dict
 
 добавление
dict - 0.048672499999999994
order_dict - 0.0647393
 изменнение
dict - 0.04049169999999999
order_dict - 0.05671040000000001

При получение элемента по ключу get()и получение пары items() скорость примно одинаковая
    get()
dict - 0.5840289000000001
order_dict - 0.6303169
    items()
dict - 0.7163272999999999
order_dict - 0.7164932999999998

возвращает ключи в словаре keys()  скорость примно одинаковая
dict - 0.6743933000000002
order_dict - 0.6765570000000003

обновление словаря update() быстрее работает OrderedDict
dict - 0.5491039999999998
order_dict - 0.5011443

удаление пары ключ popitem быстрее dict
dict - 2.3000000002326715e-06
order_dict - 9.499999999995623e-06


dict быстрее работает при добавлении, удалении и изменении элементов, в случае обновления dict и OrderedDict быстрее работает OrderedDict,
в других случаях значения почти одинаковые, но все же быстрее работает dict.
Вывод: операции в обычном словаре выполняются быстрее, чем в OrderedDict, кроме update()
"""
