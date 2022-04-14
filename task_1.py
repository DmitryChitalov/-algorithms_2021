"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time
import random


def time_check(function):
    """
    Функция-декоратор для измерения времени функции.
    Фиксируем отсечки времени до и после выполнения основной логики
    :param function: передаём в декоратор исполняемую функцию
    :return: кортеж из результата ф-ции и затраченного времени
    """
    def wrapped(*args):
        start_val = time.time()
        result = function(*args)
        end_val = time.time()
        return result, end_val - start_val
    return wrapped


@time_check
def dict_fill(quantity: int):
    origin_dict = {}
    for i in range(quantity):
        origin_dict[i] = random.randint(0, 5000)
    return origin_dict


@time_check
def list_fill(quantity: int):
    origin_list = [random.randint(0, 5000) for i in range(quantity)]
    return origin_list


@time_check
def dict_elem_remove(user_dict: dict):
    """
    удаляем элементы из словаря:
    сначала получаем список ключей, а потом удаляю половину из них
    """
    keys = list(user_dict.keys())
    print('Удалим половину словаря')
    for key in keys[:(len(user_dict)) // 2]:
        user_dict.pop(key)


@time_check
def list_elem_remove(user_list: list):
    print('Удалим половину списка')
    for i in range(len(user_list) // 2):
        user_list.pop(i)


@time_check
def dict_update(user_dict: dict, new_dict: dict):
    print('Обновим словарь, добавив в него 5000 новых записей')
    user_dict.update(new_dict)


@time_check
def list_update(user_list: list, new_list: list):
    print('Обновим список, добавив в него 5000 новых записей')
    user_list.extend(new_list)


@time_check
def find_values_list(user_list, quantity: int, start_val: int):
    result = []
    for i in range(start_val, start_val + quantity):
        for el in user_list:
            if el == i:
                result.append(i)
    return result


@time_check
def find_values_dict(dict1, quantity: int, start_val: int):
    result = {}
    for i in range(start_val, start_val + quantity):
        for key, el in dict1.items():
            if el == i:
                result[key] = el
    return result


elem_quantity = int(input('Ждём от вас количество элементов: '))
print('Начинаем работу...')
my_dict_1 = dict_fill(elem_quantity)
my_list = list_fill(elem_quantity)
print(f'Операция заполнения словаря заняла {my_dict_1[1]} сек. Количество занесённых элементов: {elem_quantity}')
print(f'Операция заполнения списка заняла {my_list[1]} сек. Количество занесённых элементов: {elem_quantity}')
print(len(my_dict_1[0]), len(my_list[0]))
# Вывод №1: Словарь заполняется дольше, чем список, так как в словарь записываются ключи, которые хэшируются,
# и их значения.

# 2. Удаление элементов
dict_after_remove = dict_elem_remove(my_dict_1[0])
print(f'Операция удаления элементов из словаря заняла {dict_after_remove[1]} сек.')
list_after_remove = list_elem_remove(my_list[0])
print(f'Операция удаления элементов из списка заняла {list_after_remove[1]} сек.')
print(len(my_dict_1[0]), len(my_list[0]))
# Вывод №2: Удаление в словаре происходит намного быстрее за счет того, что поиск
# по ключу в словаре работает гораздо быстрее, чем поиск по индексу в списке.


# 3. Обновление
# Подготовим новые словарь и список для добавления
added_dict = {i: random.random() for i in range(5000, 10000)}
added_list = [elem for elem in range(5000)]

dict_after_update = dict_update(my_dict_1[0], added_dict)
print(f'Операция добавления элементов в словарь заняла {dict_after_update[1]} сек.')
list_after_update = list_update(my_list[0], added_list)
print(f'Операция добавления элементов в список заняла {list_after_update[1]} сек.')
print(len(my_dict_1[0]), len(my_list[0]))
# Вывод №3: Добавление в словаре происходит медленнее, т.к. опять нужно хешировать ключи


# 4. Поиск по значению
# для поиска по значениям подготовим список с нужными ключами
my_find_dict = find_values_dict(my_dict_1[0], 100, 1500)
print(f'Поиск по значению в словаре занял {my_find_dict[1]}')
my_find_list = find_values_list(my_list[0], 100, 1500)
print(f'Поиск по значению в списке занял {my_find_list[1]}')
# Вывод №4: Поиск по значению в словаре осуществляется дольше, чем в списке
