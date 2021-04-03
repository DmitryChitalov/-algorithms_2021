"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
# from timeit import timeit
from random import randint
from cProfile import run

def fill_set(amount_el=1000):       # функция заполнения множества для последующей перегрузки в список и словарь
    my_set = set()
    while len(my_set) < amount_el:
#        my_set.add(random.randint(0, amount_el*100))
        my_set.add(str(randint(0, amount_el * 100)) + 'word')  # для чистоты эксперимента, значения будут строковыми
    return my_set

def fill_dict(obj):         # Функция заполнения dict и OrderedDict значениями из множества
    obj.clear()             # очистим словарь
    for el in my_set:
        obj[el] = 'simple_word'
    return obj

def fill_ordered_dict(obj): # Функция заполнения dict и OrderedDict значениями из множества
    obj.clear()             # очистим словарь
    for el in my_set:
        obj[el] = 'simple_word'
    return obj

def find_in_dict(obj):      # Процедура взятия элемента по ключу
    for el in my_set:
        get_el = obj[el]

def find_in_ordered_dict(obj):      # Процедура взятия элемента по ключу
    for el in my_set:
        get_el = obj[el]

def del_el_in_dict(obj):        # Процедура удаления в словаре элементов передаваемого множества
    for el in my_set:
        obj.pop(el)

def del_el_in_ordered_dict(obj):        # Процедура удаления в словаре элементов передаваемого множества
    for el in my_set:
        obj.pop(el)

def main(count_iteration):
    for i in range(count_iteration):
        fill_dict(my_dict)
        fill_ordered_dict(my_odict)
        find_in_dict(my_dict)
        find_in_ordered_dict(my_odict)
        del_el_in_dict(my_dict)
        del_el_in_ordered_dict(my_odict)


len_dict = 1000
count_iteration = 10000
my_dict = {}
my_odict = OrderedDict()
my_set = fill_set(len_dict)

run('main(count_iteration)')

'''
Результаты замеров:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    1.452    0.000    1.486    0.000 task_4.py:22(fill_dict)
    10000    2.429    0.000    2.459    0.000 task_4.py:28(fill_ordered_dict)
    10000    0.940    0.000    0.940    0.000 task_4.py:34(find_in_dict)
    10000    0.910    0.000    0.910    0.000 task_4.py:38(find_in_ordered_dict)
    10000    2.905    0.000    4.824    0.000 task_4.py:42(del_el_in_dict)
    10000    3.004    0.000    6.852    0.001 task_4.py:46(del_el_in_ordered_dict)
    10000    0.030    0.000    0.030    0.000 {method 'clear' of 'collections.OrderedDict' objects}
    10000    0.034    0.000    0.034    0.000 {method 'clear' of 'dict' objects}
 10000000    3.848    0.000    3.848    0.000 {method 'pop' of 'collections.OrderedDict' objects}
 10000000    1.919    0.000    1.919    0.000 {method 'pop' of 'dict' objects}

Вывод:
    Учитывая то, что с версии 3.6 словари поддерживают сортировку, потребности в использовании OrderedDict нет.
    Тем более, что по скорости он в большинстве случаев проигрывает стандартному Dict.
    Особенно это заметно на операциях pop.
    Естественно, этот вывод не распространяется на случаи, когда требуется работать с более ранними версиями Python. 


'''
