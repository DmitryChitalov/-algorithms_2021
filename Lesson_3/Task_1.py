import time
import random


def time_decor(func):
    def wrapped(*args):
        time_1 = time.time()
        result = func(*args)
        time_2 = time.time()
        return result, time_2 - time_1
    return wrapped


@time_decor
def rand_dict(elems: int):
    origin_dict = {}
    for i in range(elems):
        origin_dict[i] = random.randint(0, 10000)
    return origin_dict


@time_decor
def rand_list(elems: int):
    origin_list = [random.randint(0, 10000) for i in range(elems)]
    return origin_list


quantity_el = int(input('Введите количество элементов: '))
print('---------------------------------------------------------------------------')
my_dict_1 = rand_dict(quantity_el)
my_list = rand_list(quantity_el)
print(f'Заполнение словаря длилось {my_dict_1[1]} сек. Длина словаря: {quantity_el}')
print(f'Заполнение списка длилось {my_list[1]} сек. Длина списка: {quantity_el}')
print('---------------------------------------------------------------------------')


@time_decor
def dict_keys_del(user_dict: dict):
    keys = list(user_dict.keys())
    for key in keys[:(len(user_dict)) // 2]:
        user_dict.pop(key)


@time_decor
def list_el_del(user_list: list):
    for i in range(len(user_list) // 2):
        user_list.pop(i)


new_dict_1 = dict_keys_del(my_dict_1[0])
print('Удалим половину значений из словаря')
print(f'Удаление из словаря длилось {new_dict_1[1]} сек.')
print('---------------------------------------------------------------------------')
new_list_1 = list_el_del(my_list[0])
print('Удалим половину значений из списка')
print(f'Удаление из списка длилось {new_list_1[1]} сек.')
print('---------------------------------------------------------------------------')

@time_decor
def dict_update(user_dict: dict, new_dict: dict):
    user_dict.update(new_dict)


@time_decor
def list_update(user_list: list, new_list: list):
    user_list.extend(new_list)


added_dict = {i: random.random() for i in range(5000, 15000)}
added_list = [elem for elem in range(10000)]

dict_after_update = dict_update(my_dict_1[0], added_dict)
print('Добавим 10000 новых значений в словарь')
print(f'Добавление новых значений в словарь заняло {dict_after_update[1]} сек.')
print('---------------------------------------------------------------------------')
list_after_update = list_update(my_list[0], added_list)
print('Добавим 10000 новых значений в список')
print(f'Добавление новых значений в список заняло {list_after_update[1]} сек.')


# Выводы:
# 1: Словарь заполняется дольше, чем список, из-за хэширования ключей и значений в словаре.
# 2: Удаление в словаре происходит намного быстрее из-за поиска в словаре по ключам.
# 3: Добавление в словаре происходит медленнее, насколько я понимаю из-за повторного хеширования ключей.
