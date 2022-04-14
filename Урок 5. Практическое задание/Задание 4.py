
"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

# OrderedDict - Словарь, «запоминающий» порядок добавления элементов.
# Необходим был в версиях до 3.6, т. к.  были словари неупорядоченными.

# О ЭФФЕКТИВНОСТИ обычного словаря и OrderedDict.
# Заполнение, получение элемента и делаем замеры.


# Заполняем обычный словарь и делаем замеры.
from collections import OrderedDict
from timeit import timeit

dic = {}
def dic_filling():
    for val in range(100):
        key = val + 1
        dic[key] = val
    return(dic)
print('Полученный словарь: ', dic_filling())
print('Полученный словарь: ', type(dic_filling()))
print(f'Заполнение обычного словаря:', timeit("dic_filling()", globals=globals(), number=100000))


# OrderedDict (заполнение) и делаем замеры.
def Orderdic_filling():
    new_dic = OrderedDict()
    for val in range(100):
        key = val + 1
        new_dic[key] = val
    return(new_dic)
#print('Полученный словарь: ', Orderdic_filling())
print(f'Заполнение OrderedDict:', timeit("Orderdic_filling()", globals=globals(), number=100000))
print('Заполнение обычного словаря происходит быстрее примерно в 2 раза')
print('_____________________________________________________')


# Получение эл-та в обычном словаре
d = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}

def extract_el_dic():
    list = [item for item in d.items()]
    return list[0]
print(extract_el_dic())
print(f'Получение элемента обычного словаря:', timeit("extract_el_dic()", globals=globals(), number=100000))

# Получение эл-та в Orderdic().
d_Ord = OrderedDict([('apple', 5600.00), ('orange', 3500.00), ('banana', 5000.00)])
print(type(d_Ord))
def extract_el_Orderdic():
    list = [item for item in d_Ord.items()]
    return list[0]
print(extract_el_Orderdic())
print(f'Получение элемента OrderedDict:', timeit("extract_el_Orderdic()", globals=globals(), number=100000))
print('Извлечение, у обычного словаря, происходит быстрее примерно 20-30%')

"""
ВЫВОД: В применении OrderedDict особого смысла, в современных версиях Python, нет. 
Стоит его применять только используя его спец-ные ф-ии: move_to_end(), popitem().
"""