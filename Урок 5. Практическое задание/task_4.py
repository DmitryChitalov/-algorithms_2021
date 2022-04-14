"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from random import randint
from timeit import timeit, default_timer


def time_dict(func):
    def wrapper(*args):
        t1 = default_timer()
        res = func(*args)
        print(f'Время выполенения {func.__name__}: {default_timer() - t1}. ')
        return res
    return wrapper


def full_dict(j_dict):
    for el in range(10000):
        j_dict[el] = el * 3


def change_el_dict(j_dict):
    for _ in range(2000):
        j_dict[randint(0, 9999)] /= 3


def items_dict(j_dict):
    for key_dict, item_dict in j_dict.items():
        if item_dict % 2 == 0:
            j_dict[key_dict] += 1

@time_dict
def pop_el_dict(j_dict):
    for num in range(1000):
        j_dict.pop(num)


just_dict = {}
order_dict = OrderedDict()
full_dict(just_dict)
full_dict(order_dict)
change_el_dict(just_dict)
change_el_dict(order_dict)
items_dict(just_dict)
items_dict(order_dict)

print(f'Время заполнения простого словаря: {timeit("full_dict(just_dict)", globals=globals(), number=1000)}')
print(f'Время заполнения упорядоченного словаря: {timeit("full_dict(order_dict)", globals=globals(), number=1000)}')
print(f'Время изменения простого словаря: {timeit("change_el_dict(just_dict)", globals=globals(), number=1000)}')
print(f'Время изменения упорядоченного словаря: {timeit("change_el_dict(order_dict)", globals=globals(), number=1000)}')
print(f'Время изменения (еще раз) простого словаря: {timeit("items_dict(just_dict)", globals=globals(), number=1000)}')
print(f'Время изменения (еще раз) упорядоченного словаря: '
      f'{timeit("items_dict(order_dict)", globals=globals(), number=1000)}')
pop_el_dict(just_dict)
pop_el_dict(order_dict)

'''
Время заполнения простого словаря: 1.3896083
Время заполнения упорядоченного словаря: 1.6636456
Время изменения простого словаря: 3.0398193
Время изменения упорядоченного словаря: 3.0861357
Время изменения (еще раз) простого словаря: 1.3198959000000006
Время изменения (еще раз) упорядоченного словаря: 1.6988912000000003
Время выполенения pop_el_dict: 0.00018949999999939848. 
Время выполенения pop_el_dict: 0.0002870999999995405.
(Для удаления элемента был использован декоратор)

Обычный словарь заполняется быстрее заполняется, быстрее получает нужный элемент и быстрее удаляет элемент,
чем OrderedDict.
Так что смысла нет использовать OrderDict вместо обычного словаря. Тем более, что в Python 3.9 обычный словарь тоже
фиксирует порядок добавления элементов.'''
