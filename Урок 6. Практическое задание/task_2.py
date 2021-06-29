"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""

import _pickle as pickle
import json
from pympler import asizeof


"""
Pickle (англ. консервировать, мариновать) — модуль сериализации и десериализации объектов в Питоне для последующей
их передачи.
Что умеет запаковывать?
- None, True, False
- Строки (обычные или Юникод)
- Стандартные числовые типы данных
- Словари, списки, кортежи
- Функции
- Классы
"""


my_dict = {x: x for x in range(100000)}
print(asizeof.asizeof(my_dict))  # 8442960
pickle_dict = pickle.dumps(my_dict)
json_dict = json.dumps(my_dict)
print(asizeof.asizeof(pickle_dict))  # 737696
print(asizeof.asizeof(json_dict))  # 1577832

"""
по сравнению с json занимает меньше места
"""



