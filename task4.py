"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


import time
from collections import OrderedDict


start_time = time.time()
my_dict = {x: y for x in range(1000) for y in range(1000)}
end_time = time.time()
print('время заполнения dict ', end_time - start_time)

start_time = time.time()
order_dict = OrderedDict({x: y for x in range(1000) for y in range(1000)})
end_time = time.time()
print('время заполнения order_dict ', end_time - start_time)


print('----------------------------------------------------------')
start_time = time.time()
for el in my_dict:
        get_el = my_dict[el]
end_time = time.time()
print('время перебор эелментов dict ', end_time - start_time)

start_time = time.time()
for el in order_dict:
        get_el_order = order_dict[el]
end_time = time.time()
print('время перебор эелментов order_dict', end_time - start_time)


print('----------------------------------------------------------')

start_time = time.time()
my_dict.get(999)
end_time = time.time()
print('время получения эелмента dict ', end_time - start_time)

start_time = time.time()
order_dict.get(999)
end_time = time.time()
print('время получения эелмента order_dict', end_time - start_time)

#время заполнения dict  0.09376072883605957
#время заполнения order_dict  0.06249737739562988
#----------------------------------------------------------
#время перебор эелментов dict  0.0
#время перебор эелментов order_dict 0.0
#----------------------------------------------------------
#время получения эелмента dict  0.0
#время получения эелмента order_dict 0.0

#Есть небольшая разница в заполеии по времени, order_dicr немного быстрее.
#Смысла подключать нет, так как нет ощутимой разницы во времени.