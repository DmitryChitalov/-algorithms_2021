"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


dict_obj = {}
dict_obj = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66, 7: 77}
odict_obj = OrderedDict(dict_obj)

dict_obj[8] = 88
odict_obj[8] = 88

dict_obj.values()
odict_obj.values()

dict_obj.popitem()
odict_obj.popitem()
dict_obj.keys()

print(dict_obj.pop(1))
print(dict_obj)
print(odict_obj.pop(1))
print(odict_obj)


print(f"Добавление эл-та в dict {timeit('dict_obj[5] = 55', globals=globals(), number=100000)}")
print(f"Добавление эл-та d OrderedDict {timeit('odict_obj[5] = 55', globals=globals(), number=100000)}")

print(f"Удаление эл-та из dict {timeit('dict_obj.popitem()', globals=globals(), number=3)}")
print(f"Удаление эл-та из OrderedDict {timeit('odict_obj.popitem()', globals=globals(), number=3)}")

print(f"Вывод всез значений dict {timeit('dict_obj.values() ', globals=globals(), number=100000)}")
print(f"Вывод всез значений OrderedDict = {timeit('odict_obj.values()', globals=globals(), number=100000)}")

print(f"Вывод всех ключей dict {timeit('dict_obj.keys() ', globals=globals(), number=100000)}")
print(f"Вывод всех ключей dict {timeit('odict_obj.keys() ', globals=globals(), number=100000)}")

"""
При большинстве тестов OrderedDict оказывается медленее, но и иногда эти цифры равны
Учитывая что расхождение идет на уровне 1 тысячной, то можно сделать скидку на влияние ОС
и сказать что скорости равны
Но учитывая что единственным преимуществом OrderedDict ранее было сохранение порядка, то сейчас 
смысл в использовании его отпадает, так как обычный dict так же сейчас сохраняет порядок эл-ов
"""