"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from time import time
from collections import OrderedDict

dict_list = dict()
or_dict = OrderedDict()
### start insert ###
start = time()
for i in range(10000):
    dict_list[str(i)]=i
end = time()
print(end - start)
### end insert ###

### start pop ###
start = time()
for i in range(10000):
    dict_list.pop(str(i))
end = time()
print(end - start)
### end pop ###


### start update ###
start = time()
for i in range(10000):
    or_dict.update({str(i):i})
end = time()
print(end - start)
### end update ###

### start pop ###
start = time()
for i in range(10000):
    or_dict.pop(str(i))
end = time()
print(end - start)
### end pop ###

#OrderedDict с базовыми операциями работает хуже
