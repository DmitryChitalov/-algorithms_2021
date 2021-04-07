"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import collections
import timeit


def create_dict(num):
    my_dict = dict()
    for i in range(num):
        my_dict[str(i)] = i


def create_odict(num):
    odict = collections.OrderedDict()
    for i in range(num):
        odict[str(i)] = i


def pop_dict(my_regular_dict):
    for i in range(len(my_regular_dict)):
        my_regular_dict.popitem()


def pop_odict(my_ordery_dict):
    for i in range(len(my_ordery_dict)):
        my_ordery_dict.popitem()


def update_dict(dict_one, dict_two):
    dict_one.update(dict_two)


def update_odict(dict_one, dict_two):
    dict_one.update(dict_two)


def get_dict(dict):
    for i in range(len(dict)):
        dict.get(i)


def get_odict(odict):
    for i in range(len(odict)):
        odict.get(i)


def key_value_dict(dict):
    for key, value in dict.items():
        k = key
        v = value


def key_value_odict(odict):
    for key, value in odict.items():
        k = key
        v = value

my_regular_dict = {}
my_regular_dict2 = {}
my_ordery_dict = collections.OrderedDict
num = 10000
for i in range(num):
    my_regular_dict[i] = i
    my_regular_dict2[i] = i+1000

my_ordery_dict = collections.OrderedDict(my_regular_dict)

create_dict(num)
create_odict(num)
pop_dict(my_regular_dict)
pop_odict(my_ordery_dict)
update_dict(my_regular_dict, my_regular_dict2)
update_odict(my_ordery_dict, my_regular_dict2)
get_dict(my_regular_dict)
get_odict(my_ordery_dict)
key_value_dict(my_regular_dict)
key_value_odict(my_ordery_dict)
print("create_dict:", timeit.timeit("create_dict(num)", globals=globals(), number=10000))
print("create_odict:", timeit.timeit("create_odict(num)", globals=globals(), number=10000))
print('--------------------------------------------------------------------------------------------------------')
print("pop_dict:", timeit.timeit("pop_dict(my_regular_dict)", globals=globals(), number=10000))
print("pop_odict:", timeit.timeit("pop_odict(my_ordery_dict)", globals=globals(), number=10000))
print('--------------------------------------------------------------------------------------------------------')
print("update_dict:", timeit.timeit("update_dict(my_regular_dict, my_regular_dict2)", globals=globals(), number=10000))
print("update_odict:", timeit.timeit("update_odict(my_ordery_dict, my_regular_dict2)", globals=globals(), number=10000))
print('--------------------------------------------------------------------------------------------------------')
print("get_dict:", timeit.timeit("get_dict(my_regular_dict)", globals=globals(), number=10000))
print("get_odict:", timeit.timeit("get_odict(my_ordery_dict)", globals=globals(), number=10000))
print('--------------------------------------------------------------------------------------------------------')
print("key_value_dict:", timeit.timeit("key_value_dict(my_regular_dict)", globals=globals(), number=10000))
print("key_value_odict:", timeit.timeit("key_value_odict(my_ordery_dict)", globals=globals(), number=10000))

"""
результат выполнения на моей машине.
create_dict: 19.0129102
create_odict: 23.166326700000003
--------------------------------------------------------------------------------------------------------
pop_dict: 0.0018542000000039138
pop_odict: 0.002248399999999151
--------------------------------------------------------------------------------------------------------
update_dict: 0.8752005999999994
update_odict: 7.058721800000001
--------------------------------------------------------------------------------------------------------
get_dict: 4.356152999999999
get_odict: 4.704274199999993
--------------------------------------------------------------------------------------------------------
key_value_dict: 2.2689300999999986
key_value_odict: 4.147819599999998

в каждом из представленных случаев OrderedDict показал меньшую эффективность 
по сравнению с регулярным Dict(Python3.9). 
Отсюда делаем вывод о неактуальности OrderedDict в текущей версии для решения стандартных задач
"""
