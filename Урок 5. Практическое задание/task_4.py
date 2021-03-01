"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import collections
import timeit

my_dict = {1: 111, 2: 222, 3: 333}
ord_dict = collections.OrderedDict([(1, 111), (2, 222), (3, 333)])


def fill(dct):
    start = list(dct.keys())[-1]
    for i in range(start + 1, 11005):
        dct.update({i: int(str(f'{i}{i}{i}'))})


print(timeit.timeit("my_dict.keys()", globals=globals(), number=1000000))
print(timeit.timeit("my_dict.update({4:444})", globals=globals(), number=1000000))
print(timeit.timeit("my_dict.get(4)", globals=globals(), number=1000000))
fill(my_dict)
print(timeit.timeit("my_dict.popitem()", globals=globals(), number=10000))
print()
print(timeit.timeit("ord_dict.keys()", globals=globals(), number=1000000))
print(timeit.timeit("ord_dict.update({4:444})", globals=globals(), number=1000000))
print(timeit.timeit("ord_dict.get(4)", globals=globals(), number=1000000))
fill(ord_dict)
print(timeit.timeit("ord_dict.popitem(last=True)", globals=globals(), number=10000))

'''
Результаты замеров на моём пк:
0.06542928999988362
0.13076091899893072
0.045632885998202255
0.0006581819998245919

0.054205677999561885
0.21997439699953247
0.048066485000163084
0.0013319619993126253

Я сильно загрузил словарь и OrderedDict так как на 10000 результат был одинаков.
На 10000000 повторений мы уже видим небольшую разницу, а именно в добавление пары
ключ значение немного медленнее в OrderedDict. А вот достать пару ключ значение с
конца в словаре существенно быстрее чем в OrderedDict.
В python3 до версии 3.6 словари были неупорядоченными. А OrderedDict упорядочивает словарь. 
Поэтому в этом модуле было больше смысла чем в современых версиях python3. Правда если 
вам потребуется достать пару ключ значение с начала, то в OrderedDict есть такая возможность
popitem(last=False). У словаря нет аналогичной функции и нужно будет либо знать название
либо пройтись по парам ключ значение в цикле и нагромаждать код. Общий вывод такой что
в современном Python3 нужды в OrderedDict практически нет.
'''
