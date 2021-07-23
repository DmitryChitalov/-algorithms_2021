"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit


def filling_dict(list_len):
    """
    Заполненеие словаря.
    Сложность: O(N)
    :param list_len:
    :return:
    """
    test_dict = {i + 1: i for i in range(0, list_len)}  # O(N)
    return test_dict


def filling_ordered_dict(list_len):
    """
    Заполненеие словаря.
    Сложность: O(N)
    :param list_len:
    :return:
    """
    test_dict = OrderedDict({i + 1: i for i in range(0, list_len)})  # O(N)
    return test_dict


# region operation
def dict_clear(test_dict):
    """
    Removes all the elements from the dictionary.
    Сложность: O(1).
    """
    return test_dict.clear()


def dict_copy(test_dict):
    """
    Returns a copy of the dictionary.
    Сложность: O(N).
    """
    test_dict_copy = test_dict.copy()
    return test_dict_copy


def dict_fromkeys(keys, values):
    """
    Returns a dictionary with the specified keys and value.
    Сложность: O(N).
    """
    return dict.fromkeys(keys, values)


def dict_get(test_dict, key):
    """
    Returns the value of the specified key.
    Сложность: O(1).
    """
    return test_dict.get(key)


def dict_items(test_dict):
    """
    Returns a list containing a tuple for each key value pair.
    Сложность: O(N).
    """
    return test_dict.items()


def dict_keys(test_dict):
    """
    Returns a list containing the dictionary's keys.
    Сложность: O(N).
    """
    return test_dict.keys()


def dict_pop(test_dict, key):
    """
    Removes the element with the specified key.
    Сложность: O(1).
    """
    return test_dict.pop(key)


def dict_popitem(test_dict):
    """
    Removes the last inserted key-value pair.
    Сложность: O(1).
    """
    return test_dict.popitem()


def dict_setdefault(test_dict, key, value):
    """
    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
    Сложность: O(1).
    """
    return test_dict.setdefault(key, value)


def dict_update(test_dict, key, value):
    """
    Updates the dictionary with the specified key-value pairs.
    Сложность: O(1).
    """
    return test_dict.update({key: value})


def dict_values(test_dict):
    """
    Returns a list of all the values in the dictionary.
    Сложность: O(N).
    """
    return test_dict.values()


def dict_sort(test_dict):
    """
    Sort dict by keys.
    Сложность O(N log N)
    """
    return dict(sorted(test_dict.items()))


# endregion


def get_new_dict(elements_count):
    return {i + 1: i for i in range(0, elements_count)}


def get_new_ordered_dict(elements_count):
    return OrderedDict({i + 1: i for i in range(0, elements_count)})


el_count = 1000000
number_repetitions = 10

# Dict.
print("Dict: ")

print("filling_dict: ", timeit(stmt="filling_dict(el_count)", globals=globals(), number=number_repetitions))

print("dict_clear: ", timeit(stmt="dict_clear(get_new_dict(el_count))", globals=globals(), number=number_repetitions))

print("dict_copy: ", timeit(stmt="dict_copy(get_new_dict(el_count))", globals=globals(), number=number_repetitions))

print("dict_fromkeys: ", timeit(stmt="dict_fromkeys(get_new_dict(el_count).keys(), get_new_dict(el_count).values())",
                                globals=globals(), number=number_repetitions))

print("dict_get: ", timeit(stmt="dict_get(get_new_dict(el_count), 10000)", globals=globals(),
                           number=number_repetitions))

print("dict_items: ", timeit(stmt="dict_items(get_new_dict(el_count))", globals=globals(), number=number_repetitions))

print("dict_keys: ", timeit(stmt="dict_keys(get_new_dict(el_count))", globals=globals(), number=number_repetitions))

print("dict_pop: ", timeit(stmt="dict_pop(get_new_dict(el_count), 14568)", globals=globals(),
                           number=number_repetitions))

print("dict_popitem: ", timeit(stmt="dict_popitem(get_new_dict(el_count))", globals=globals(),
                               number=number_repetitions))

print("dict_setdefault: ", timeit(stmt="dict_setdefault(get_new_dict(el_count), 1001, 'test')", globals=globals(),
                                  number=number_repetitions))

print("dict_update: ", timeit(stmt="dict_update(get_new_dict(el_count), 10000, 'value_212121')", globals=globals(),
                              number=number_repetitions))

print("dict_values: ", timeit(stmt="dict_values(get_new_dict(el_count))", globals=globals(),
                              number=number_repetitions))

print("dict_sort: ", timeit(stmt="dict_sort(get_new_dict(el_count))", globals=globals(),
                            number=number_repetitions))

print("OrderedDict: ")

# OrderedDict.
print("filling_ordered_dict: ", timeit(stmt="filling_ordered_dict(el_count)", globals=globals(),
                                       number=number_repetitions))

print("ordered_dict_clear: ",
      timeit(stmt="dict_clear(get_new_ordered_dict(el_count))", globals=globals(), number=number_repetitions))

print("ordered_dict_copy: ",
      timeit(stmt="dict_copy(get_new_ordered_dict(el_count))", globals=globals(), number=number_repetitions))

print("ordered_dict_fromkeys: ",
      timeit(stmt="dict_fromkeys(get_new_ordered_dict(el_count).keys(), get_new_ordered_dict(el_count).values())",
             globals=globals(), number=number_repetitions))

print("ordered_dict_get: ", timeit(stmt="dict_get(get_new_ordered_dict(el_count), 10000)", globals=globals(),
                                   number=number_repetitions))

print("ordered_dict_items: ",
      timeit(stmt="dict_items(get_new_ordered_dict(el_count))", globals=globals(), number=number_repetitions))

print("ordered_dict_keys: ",
      timeit(stmt="dict_keys(get_new_ordered_dict(el_count))", globals=globals(), number=number_repetitions))

print("ordered_dict_pop: ", timeit(stmt="dict_pop(get_new_ordered_dict(el_count), 14568)", globals=globals(),
                                   number=number_repetitions))

print("ordered_dict_popitem: ", timeit(stmt="dict_popitem(get_new_ordered_dict(el_count))", globals=globals(),
                                       number=number_repetitions))

print("ordered_dict_setdefault: ",
      timeit(stmt="dict_setdefault(get_new_ordered_dict(el_count), 1001, 'test')", globals=globals(),
             number=number_repetitions))

print("ordered_dict_update: ",
      timeit(stmt="dict_update(get_new_ordered_dict(el_count), 10000, 'value_212121')", globals=globals(),
             number=number_repetitions))

print("ordered_dict_values: ", timeit(stmt="dict_values(get_new_ordered_dict(el_count))", globals=globals(),
                                      number=number_repetitions))

print("ordered_dict_sort: ", timeit(stmt="dict_sort(get_new_ordered_dict(el_count))", globals=globals(),
                                    number=number_repetitions))

"""
Тест операций проводился на миллионе записей с 10 повторениями.
Заполнение:
Dict: 
filling_dict:  1.2120224
OrderedDict: 
filling_ordered_dict:  2.907774

Операции:
Dict: 
dict_clear:  1.2374169000000002
dict_copy:  1.4184589000000005
dict_fromkeys:  2.8444802000000005
dict_get:  1.2423960999999997
dict_items:  1.2229804000000009
dict_keys:  1.2244620000000008
dict_pop:  1.1976560999999997
dict_popitem:  1.2335881000000004
dict_setdefault:  1.2126830000000002
dict_update:  1.203773
dict_values:  1.2174768999999994
dict_sort:  2.241135100000001
OrderedDict: 
ordered_dict_clear:  2.9254694999999984
ordered_dict_copy:  3.9045196000000004
ordered_dict_fromkeys:  6.453468800000003
ordered_dict_get:  2.9455979000000028
ordered_dict_items:  2.9118099999999956
ordered_dict_keys:  2.9490301000000017
ordered_dict_pop:  2.9087169000000017
ordered_dict_popitem:  2.9487888999999967
ordered_dict_setdefault:  2.945205999999999
ordered_dict_update:  2.948351300000006
ordered_dict_values:  2.953710600000001
ordered_dict_sort:  4.2696586

Из теста видно, что OrderedDict проигрывает Dict как по заполнению, так и по операциям. А начиная с версии Python 3.6 
словари «помнят» порядок добавления элементов.
В Python 3.6 и более поздних версиях использование OrderedDict скорее вредно.
"""
