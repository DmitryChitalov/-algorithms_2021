import collections
from timeit import timeit

NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
USUAL_DICT = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# вывод списка ключей
def ordered_d_key_list():
    return NEW_DICT.keys()


def usual_d_key_list():
    return USUAL_DICT.keys()


print('ВЫВОД СПИСКА КЛЮЧЕЙ')
print(f'Time for ordered_d_key_list() is {timeit("ordered_d_key_list()", globals=globals())} seconds')
print(f'Time for usual_d_key_list() is {timeit("usual_d_key_list()", globals=globals())} seconds')
print('#########################################################################')


# добавление элемента в словарь
def ordered_d_add():
    NEW_DICT['data'] = True
    return NEW_DICT


def usual_d_add():
    USUAL_DICT['data'] = True
    return USUAL_DICT


print('ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СЛОВАРЬ')
print(f'Time for ordered_d_add() is {timeit("ordered_d_add()", globals=globals())} seconds')
print(f'Time for usual_d_add() is {timeit("usual_d_add()", globals=globals())} seconds')
print('#########################################################################')

# вывод знчения ключа
def ordered_d_get_key():
    return NEW_DICT.get('b')


def usual_d_get_key():
    return USUAL_DICT.get('b')


print('ВЫВОД ЗНАЧЕНИЯ КЛЮЧА')
print(f'Time for ordered_d_get_key() is {timeit("ordered_d_get_key()", globals=globals())} seconds')
print(f'Time for usual_d_get_key() is {timeit("usual_d_get_key()", globals=globals())} seconds')

'''
ВЫВОД СПИСКА КЛЮЧЕЙ
Time for ordered_d_key_list() is 0.2042402 seconds
Time for usual_d_key_list() is 0.24126060000000002 seconds
#########################################################################
ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СЛОВАРЬ
Time for ordered_d_add() is 0.20853860000000002 seconds
Time for usual_d_add() is 0.1759887 seconds
#########################################################################
ВЫВОД ЗНАЧЕНИЯ КЛЮЧА
Time for ordered_d_get_key() is 0.2232516 seconds
Time for usual_d_get_key() is 0.19778549999999995 seconds
ВЫВОД: OrderedDict не дает никаких преимуществ перед обычным словарем. 
Т.о., использование OrderedDict оправданно только если нужны специфические
функции, которые не поддерживаются обычным словарем, или в ситуациях, когда
приходится работать с ранними версиями Python.  
'''
