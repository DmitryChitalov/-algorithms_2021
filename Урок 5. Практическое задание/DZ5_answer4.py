"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import collections, timeit

key = range(100)

ordinary_dict = {}
ordered_dict = collections.OrderedDict([])

print(f"{timeit.timeit('for i in key: ordinary_dict[i] = 1', globals=globals())} сек.")
print(f"{timeit.timeit('for i in key: ordered_dict[i] = 1', globals=globals())} сек.")

print(f"{timeit.timeit('ordinary_dict[10]', globals=globals(), number=100000)} сек.")
print(f"{timeit.timeit('ordered_dict[10]', globals=globals(), number=100000)} сек.")

'''
Операция заполнения словаря проходит быстрее со встроенным словарем 3.2925228 сек. против 6.9076717 сек.
Операция вызова элемента проходит примерно одинаково для боих словарей 0.00323799999999963 сек. / 0.003635000000000943 сек.
OrderedDict не имеет приемущества по быстродействию в Python 3.9, поэтому нет смысла его использовать
'''
