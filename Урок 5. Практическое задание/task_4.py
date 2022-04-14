"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit

number_call = 10000

my_dict = {k: str(k) for k in range(100)}
my_ord_dict = OrderedDict({k: str(k) for k in range(100)})

create_time_dict = timeit('my_dict = {k: str(k) for k in range(100)}', number=number_call, globals=globals())
create_time_odict = timeit('my_ord_dict = OrderedDict({k: str(k) for k in range(100)})', number=number_call,
                           globals=globals())

get_time_dict = timeit('my_dict[50]', globals=globals())
get_time_odict = timeit('my_ord_dict[50]', globals=globals())


pop_dict = 'for i in range(50):\
    my_dict.popitem()'
pop_time_dict = timeit('pop_dict', globals=globals())

pop_odict = 'for i in range(50):\
    my_ord_dict.popitem()'
pop_time_odict = timeit('pop_odict', globals=globals())


print(f'Создание и наполнение словаря: {create_time_dict}\n'
      f'Создание и наполнения OrderedDict: {create_time_odict}\n'
      f'**********************************************\n'
      f'Получение элемента словаря: {get_time_dict}\n'
      f'Получение элемента OrderedDict: {get_time_odict}\n'
      f'**********************************************\n'
      f'Удаление элементов словаря: {pop_time_dict}\n'
      f'Удаление элементов OrderedDict: {pop_time_odict}\n')

'''
Операция наполнения словаря dict происходит быстрее почти в 2 раза, а вот другие операции получения элмента, удаления
практически не отличаются по времени с OrderedDict. В версиях Python 3.7+ dict стал гарантированно запоминать порядок
вставки, чего не было в прежних версиях, До Python 3.8 в обычных словарях dict отсутствовал метод __reversed__(),
который возвращает обратный итератор по ключам словаря dict. В новых версиях начиная с Python 3.7 использовать объект
OrderedDict не имеет смысла, так, как главная особенность (упорядоченность) этого объекта теперь есть во встроенном 
классе dict.

Создание и наполнение словаря: 0.1900204
Создание и наполнения OrderedDict: 0.34058910000000003
**********************************************
Получение элемента словаря: 0.034895699999999974
Получение элемента OrderedDict: 0.032596599999999976
**********************************************
Удаление элементов словаря: 0.018542599999999965
Удаление элементов OrderedDict: 0.01729320000000001
'''