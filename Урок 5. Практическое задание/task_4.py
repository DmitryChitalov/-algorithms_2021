"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
import timeit

list1 = [i for i in range(1000)]
list2 = [i for i in range(1000)]
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]

orddict = OrderedDict()
for i in range(len(list1)):
    orddict[list1[i]] = list2[i]

def filling_dict(first, second):
    dict1 = {}
    for i in range(len(list1)):
        dict1[first[i]] = second[i]


def filling_orddict(first, second):
    orddict = OrderedDict()
    for i in range(len(list1)):
        orddict[first[i]] = second[i]


def pop_dict(dict):
    for i in range(100):
        dict.popitem()

def pop_orddict(orddict):
    for i in range(100):
        orddict.popitem()

def get_dict(dict):
    for i in range(1000):
        dict.get(i)

def get_orddict(orddict):
    for i in range(1000):
        orddict.get(i)

def update_dict(dict):
    for i in range(1000):
        dict.update({i : i})

def update_orddict(orddict):
    for i in range(1000):
        orddict.update({i : i})

num = 10000

print("Measurments for the filling in:")
print("Dict: ", timeit.timeit('filling_dict(list1, list2)', globals = globals(), number = num))
print("Ordered Dict: ", timeit.timeit('filling_orddict(list1, list2)', globals = globals(), number = num))

# print("Measurments for the pop command:")
# print("Dict: ", timeit.timeit('pop_dict(dict1)', globals = globals(), number = num))
# print("Ordered Dict: ", timeit.timeit('pop_orddict(orddict)', globals = globals(), number = num))

print("Measurments for the get command:")
print("Dict: ", timeit.timeit('get_dict(dict1)', globals = globals(), number = num))
print("Ordered Dict: ", timeit.timeit('get_orddict(orddict)', globals = globals(), number = num))

print("Measurments for the update command:")
print("Dict: ", timeit.timeit('update_dict(dict1)', globals = globals(), number = num))
print("Ordered Dict: ", timeit.timeit('update_orddict(orddict)', globals = globals(), number = num))

'''
обычный словарь работает быстрее в большинстве случаях, нужды в OrderedDict нет

Measurments for the filling in:
Dict:  0.9047878
Ordered Dict:  1.4181706000000003
Measurments for the get command:
Dict:  0.6709242999999998
Ordered Dict:  0.6797484999999996
Measurments for the update command:
Dict:  1.8504205999999996
Ordered Dict:  3.1762929
'''
