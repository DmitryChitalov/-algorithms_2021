"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

print('Заполнение словаря',
      timeit('my_dict = {i: i for i in range(100)}', globals=globals(),
             number=100000))
print('Заполнение OrderedDict',
      timeit('my_odict = OrderedDict({i: i for i in range(100)})',
             globals=globals(), number=100000))

my_dict = {i: i for i in range(10000)}  # Заполнение для дальнейших измерений
my_odict = OrderedDict({i: i for i in range(10000)})
print('Удаление из словаря',
      timeit('''for inx in range(10000):
                    my_dict.pop(inx)
                    inx += 1''', globals=globals(), number=1))
print('Удаление из OrderedDict',
      timeit('''for inx in range(10000):
                    my_odict.pop(inx)
                    inx += 1''', globals=globals(), number=1))
print('Возвращение значения из словаря',
      timeit('''for inx in range(10000):
                    my_dict.setdefault(inx)
                    inx += 1''', globals=globals(), number=1))
print('Возвращение значения из OrderedDict',
      timeit('''for inx in range(10000):
                    my_odict.setdefault(inx)
                    inx += 1''', globals=globals(), number=1))
'''
1. Заполнение обычного словаря с использование DC происходит в 4 раза быстрее? 
2. Удаление с помощью pop(inx):
обычный словарь в 2 раза быстрее.
3. Возвращение значения ключа:
значения равны.
Вывод: смысла использовать OrderedDict в Python 3.6 и более поздних версиях нет, 
ввиду его медлительности по сравнению с обычным словарем и при упорядоченности 
ключей в последнем. В более ранних версиях Python это было целесообразно.
'''
