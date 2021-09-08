from collections import OrderedDict
from timeit import timeit


def fill_in_dict():
    result = {}
    for el in range(1, 1000):
        result[f"{el}"] = el
    return result


print(fill_in_dict())


def fill_in_orderdict():
    result = OrderedDict()
    for el in range(1, 1000):
        result[f"{el}"] = el
    return result


# pprint(fill_in_dict())

dict_default = fill_in_dict()
dict_ordered = fill_in_orderdict()


def get_elem_dict(key: str):
    return dict_default[key]


def get_elem_orderdict(key: str):
    return dict_ordered[key]


key_to_get_value = '100'

print("Выполнение функции fill_in_dict занимает: ", timeit("fill_in_dict()",
                                                           globals=globals(), number=1000), " сек.")
print("Выполнение функции fill_in_orderdict занимает: ", timeit("fill_in_orderdict()",
                                                                globals=globals(), number=1000), " сек.")
print("Выполнение функции get_elem_dict занимает: ", timeit("get_elem_dict(key_to_get_value)",
                                                            globals=globals(), number=100_000), " сек.")
print("Выполнение функции get_elem_orderdict занимает: ", timeit("get_elem_orderdict(key_to_get_value)",
                                                                 globals=globals(), number=100_000), " сек.")

"""
Выполнение функции fill_in_dict занимает:  0.1311539  сек.
Выполнение функции fill_in_orderdict занимает:  0.1780527  сек.
Выполнение функции get_elem_dict занимает:  0.008093500000000031  сек.
Выполнение функции get_elem_orderdict занимает:  0.008090199999999992  сек.

Добавление в словарь новых элементов в простом словаре происходит незначительно, но быстрее.
А порядок элементов сохраняется в обоих случаях.

Получение же элементов из обоих словарей происходит практически с одинаковой скоростью.

По моему мнению упорядоченный словарь нужен только для обратной совместимости со старыми приложениями. 
"""
