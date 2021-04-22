"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
#время заполнения dict  4.8625123500823975
#время заполнения order_dict  4.79100775718689
#----------------------------------------------------------
#время перебор эелментов dict  0.0009844303131103516
#время перебор эелментов order_dict 0.0010139942169189453
#----------------------------------------------------------
#время удаления эелмента dict  0.0
#время удаления эелмента order_dict 0.0
#----------------------------------------------------------
#время получения эелмента dict  0.0
#время получения эелмента order_dict 0.0
#----------------------------------------------------------
#по нескольким замерам можно увидеть что order_dict срабатывает быстрее чем обычный словарь
# целособразности использования OrderedDict не вижу т.к. разница слишком мала и нужны лишние манипуляции для подключения



import time
from collections import OrderedDict


start_time = time.time()
my_dict = {x: y for x in range(10000) for y in range(10000)}
end_time = time.time()
print('время заполнения dict ', end_time - start_time)

start_time = time.time()
# order_dict = {x: y for x in range(10000) for y in range(10000)}
order_dict = OrderedDict({x: y for x in range(10000) for y in range(10000)})
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
my_dict.pop(1000)
end_time = time.time()
print('время удаления эелмента dict ', end_time - start_time)

start_time = time.time()
order_dict.pop(1000)
end_time = time.time()
print('время удаления эелмента order_dict', end_time - start_time)

print('----------------------------------------------------------')

start_time = time.time()
my_dict.get(999)
end_time = time.time()
print('время получения эелмента dict ', end_time - start_time)

start_time = time.time()
order_dict.get(999)
end_time = time.time()
print('время получения эелмента order_dict', end_time - start_time)

print('----------------------------------------------------------')