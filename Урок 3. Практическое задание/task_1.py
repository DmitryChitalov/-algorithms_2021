"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start_val = time.time()
        value = func(*args, **kwargs)
        print(f' *** Время выполнения {func} - {time.time() - start_val} сек.')
        return value
    return wrapper


@benchmark
def get_list(n):
    return [x * 2 for x in range(n)]


@benchmark
def get_dict(n):
    return {x: x * 2 for x in range(n)}


@benchmark
def get_rand_list_values(_list, n):
    """
    Функция получает список, извлекает из него n произвольных элементов и возвращает их в виде нового списка
    """
    import random
    temp_list = []
    for _ in range(n):
        temp_list.append(_list[random.randint(0, len(_list))])
    return temp_list


@benchmark
def get_rand_dict_values(_dict, n):
    """ Функция получает словарь, извлекает из него n произвольных элементов и возвращает их в виде списка """
    import random
    temp_list = []
    for _ in range(n):
        temp_list.append(_dict.get(random.randint(0, len(_dict))))
    return temp_list


@benchmark
def join_lists(first_list, second_list):
    """ Функция объединяет два словаря """
    return first_list.copy().extend(second_list)


@benchmark
def join_dicts(first_dict, second_dict):
    """ Функция объединяет два словаря """
    return first_dict.copy().update(second_dict)


my_list_1 = get_list(10000000)
my_dict_1 = get_dict(10000000)

temp_list = get_rand_list_values(my_list_1, 1000)
temp_list = get_rand_dict_values(my_dict_1, 1000)

my_list_2 = get_list(200000)
my_dict_2 = get_dict(200000)

my_list_3 = join_lists(my_list_1, my_list_2)
my_dict_3 = join_dicts(my_dict_1, my_dict_2)


# print('my_list_2', my_list_2)
# print('my_list_3', my_list_3)
