"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from collections import OrderedDict
from timeit import timeit


ord_dict = OrderedDict({i: i ** 2 for i in range(1000)})
just_dict = {i: i ** 2 for i in range(1000)}

print(ord_dict[100])
print(timeit('ord_dict', globals=globals()))             # 0.021139900000000003
print(timeit('just_dict', globals=globals()))            # 0.0214006
print(timeit('ord_dict[50]', globals=globals()))         # 0.0410944
print(timeit('just_dict[50]', globals=globals()))        # 0.040245600000000006
print(timeit('ord_dict[10] = 100', globals=globals()))   # 0.06266730000000001
print(timeit('just_dict[10] = 100', globals=globals()))  # 0.0697914

"""
Судя по данным замера разницы в заполнении и обработке данных особо и нет.
вывод напрашивается только один зачем он (OrderedDict) нужен в версии Python 3.6 и более поздних версиях?
Но не все так однозначно если в программе нужно чтобы словарь сохранял свой порядок, то она не будет корректно
работать на старых версиях интерпритатора. 
"""
