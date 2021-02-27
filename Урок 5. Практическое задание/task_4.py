"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from timeit import timeit
from collections import OrderedDict

my_dict = {i: i**2 for i in range(6000)}
my_order = OrderedDict(my_dict)

# Посмотрим на обычные операции:
print('order values:')
print(timeit('my_order.values', globals=globals(), number=1000))
print('dict values')
print(timeit('my_dict.values', globals=globals(), number=1000))

print('order keys:')
print(timeit('my_order.keys', globals=globals(), number=1000))
print('dict keys:')
print(timeit('my_dict.keys', globals=globals(), number=1000))

print('order pop:')
print(timeit('my_order.popitem()', globals=globals(), number=1000))
print('dict pop:')
print(timeit('my_dict.popitem()', globals=globals(), number=1000))


# Теперь посмотрим непосредственно на перебор, раз смысл orderdict в упорядоченности:
def values_to_list(check_dict):
    return [i for i in check_dict]


print('order elems:')
print(timeit('values_to_list(my_order)', globals=globals(), number=1000))
print('dict elems:')
print(timeit('values_to_list(my_dict)', globals=globals(), number=1000))


'''
В общем, судя по полученным данным, операции по выборке ключей и их значений происходят одинаково. 
При этом pop у обычного словаря работает быстрее, и более того, у него же быстрее работает 
перебор элементов, хотя, по сути, OrderDict необходим в контексте этого самого перебора элементов,
раз значения в нем упорядочены по порядку внесения в список.
Вероятно, у OrderDict могут быть какие-либо операции, в которых он себя проявляет лучше, но, думаю,
обычный словарь не будет сильно ему уступать, а, если учитывать написанное выше, то нет никакого смысла
испоьзовать OrderDict в нынешних реалиях.
'''
