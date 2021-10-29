"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict
from random import randint


# Работаем со dict()

def dict_add_val():
    simple_dict[next(key_range)] = next(val_range)


def dict_show_items():  # сделаем простой проход по всем ключам и получим значения в переменную
    for key, val in simple_dict.items():
        res = [key, val]


def dict_find():  # находим по значению ключа
    val = simple_dict.get(randint(1, n))


def dict_pop():
    simple_dict.pop(next(pop_range))


# Работаем со OrderedDict()


def od_add_val():
    order_dict[next(key_range)] = next(val_range)


def od_show_items():  # сделаем простой проход по всем ключам и получим значения в переменную
    for key, val in order_dict.items():
        res = [key, val]


def od_find():  # получаем значени по ключу
    val = order_dict.get(randint(1, n))


def od_pop():
    order_dict.pop(next(pop_range))


# -- Общие параметры модели:
n = 1000
simple_dict = {}
order_dict = OrderedDict()

# 1. --- Делаем замеры для dict()
# Генераторы для добавления данных в словарь
key_range = (i for i in range(n))
pop_range = (i for i in range(n))
val_range = ((randint(1, 100), randint(1, 100)) for i in range(n))

func = ['dict_add_val', 'dict_show_items', 'dict_find', 'dict_pop']
res_dict_time = []
for func_name in func:
    res_dict_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))


# 2. --- Делаем замеры для OrderedDict
# Генераторы для добавления данных в словарь (восстанавливаем после истощения)
key_range = (i for i in range(n))
pop_range = (i for i in range(n))
val_range = ((randint(1, 100), randint(1, 100)) for i in range(n))


func = ['od_add_val', 'od_show_items', 'od_find', 'od_pop']
res_od_time = []
for func_name in func:
    res_od_time.append(timeit(f'{func_name}()', setup=f'from __main__ import {func_name}', number=n))


# --- Выводим результаты:
operations = ['add_val', 'show_items', 'find_val', 'pop']
all_result = []
all_result = list(zip(operations, res_dict_time, res_od_time))
print(f'Количество повторов: ', n)
print('Операция                 Dict       ODict      Win   D/Od % ')
for i in all_result:
    print(f'{i[0]:15.15}\t{round(i[1], 6):15.15}\t{round(i[2], 6):10.10}\t'
          f'\t{"D" if i[1] < i[2] else "OD" }\t{round((i[1]/i[2]-1)*100, 3)}')

""" 
Выводы:
Если предполагается, что в проекте используется версия Python до 3.6,
то следует обратить внимание на необходимость сохранения порядка добаления элементов.
Результаты замеров показали, что обычный словарь в данном случае не имеет каких-либо существенных отличий по
 скорости основных операций по сравнению с OrderedDict.
OrderedDict имеет дополнительные методы, которых нет в обычном словаре:
    . move_to_end()- это новый метод, добавленный в Python 3.2, который позволяет 
    переместить существующий элемент в конец или в начало словаря.
    . popitem()представляет собой расширенный вариант своего dict.popitem()аналога, 
    который позволяет вам удалять и возвращать элемент либо из конца, либо из начала базового упорядоченного словаря.


Результаты замеров следюущие:


Количество повторов:  1000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	         0.0033	  0.002927		OD	12.747
show_items     	       0.096972	  0.128937		D	-24.791
find_val       	       0.001618	  0.001416		OD	14.312
pop            	       0.000387	  0.000624		D	-37.933


Количество повторов:  5000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	       0.014794	  0.014874		D	-0.538
show_items     	       2.478371	  3.354214		D	-26.112
find_val       	        0.00811	  0.007183		OD	12.909
pop            	       0.001939	  0.002775		D	-30.146


Количество повторов:  10000
Операция                 Dict       ODict      Win   D/Od % 
add_val        	       0.028794	  0.031006		D	-7.135
show_items     	      10.052472	 14.573369		D	-31.022
find_val       	       0.016228	  0.014654		OD	10.741
pop            	       0.004157	  0.005843		D	-28.855
"""
