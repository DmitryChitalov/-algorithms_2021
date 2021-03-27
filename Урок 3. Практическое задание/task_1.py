"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def benchmark(func):
    def wrapper(n):
        start_val = time.time()
        return_value = func(n)
        end_val = time.time()
        print(f'время выполнения: {end_val - start_val} секунд.')
        return return_value
    return wrapper


def benchmark2(func):
    def wrapper(obj, n):
        start_val = time.time()
        return_value = func(obj, n)
        end_val = time.time()
        print(f'время выполнения: {end_val - start_val} секунд.')
        return return_value
    return wrapper


@benchmark
def gen_lst(n):
    """
    Генерирует список
    :param n: размер списка
    :return: список
    """
    lst_obj = [i for i in range(n)]
    return lst_obj


@benchmark
def gen_dic(n):
    """
    Генерирует словать
    :param n: размер словаря
    :return: словарь
    """
    dict_obj = {i: i * 2 for i in range(n)}
    return dict_obj


@benchmark2
def list_append(list_obj, n):
    """
    Добавляем в список n-элементов
    :param list_obj:
    :param n:
    :return:
    """
    for i in range(n):
        list_obj.append(i)
    return list_obj


@benchmark2
def dict_upd(dic_obj, n):
    """
    Добавляем в словарь n - пар ключ:значение
    :param dic_obj:
    :param n:
    :return:
    """
    i = len(dic_obj)  # Чтобы ключи не совпадали
    for i in range(n+i):
        dic_obj[i] = i
    return dic_obj


print('Генерация списка:', end=' ')
my_list = gen_lst(1000000)  # Генерация списка: время выполнения: 0.09029912948608398 секунд.
print('Генерация словаря:', end=' ')
my_dict = gen_dic(1000000)  # Генерация словаря: время выполнения: 0.2204599380493164 секунд.
"""
Генерация словаря занимет, примерно, в 3 раза больше времени
чем генерация списка
"""

print('Добавление элементов списка:', end=' ')
list_append(my_list, 1000000)  # Добавление элементов списка: время выполнения: 0.12303876876831055 секунд.
print('Добавление элементов словаря:', end=' ')
dict_upd(my_dict, 1000000)  # Добавление элементов словаря: время выполнения: 0.2886805534362793 секунд.
"""
Добавление элементов в словарь занимает, примерно,  в 2 раза больше времени
чем добавление в список.
"""

"""
За счет создании и изменнения хеш-таблицы операции со словарем занимают больше времени
"""