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
import time

my_list = list()
my_dict = dict()


def benchmark(func):
    def wrapper(*args, **kwargs):
        start_val = time.time()
        res = func(*args, **kwargs)
        print(f'Время выполнения {time.time() - start_val}')
        return res

    return wrapper


"""ЗАДАНИЕ 1 ВЫВОД. Заполнение словаря происходит значительно дольше чем заполнение списка.
Список быстрее из за того что он не является хеш-таблицей:
Время выполнения 0.05385565757751465
Добавление элементов в словарь
Время выполнения 0.009973526000976562
Добавление элементов в список"""


@benchmark
def dict_add(key, value):
    while key < 100000:
        my_dict[f'key_{key}'] = f'value_{value}'
        key += 1
        value += 1
    return f'Добавление элементов в словарь'


print(dict_add(1, 1))


@benchmark
def list_add(n):
    while n < 100000:
        my_list.append(n)
        n += 1
    return f'Добавление элементов в список'


print(list_add(0))

"""ЗАДАНИЕ 2 ВЫВОД.  Я сделал 2 общие операции clear и copy для обоих,
результат показал что и в операциях словари уступают спискам.
Время выполнения 0.0039904117584228516
Копирование словаря
Время выполнения 0.003987789154052734
Отчистка словаря
Время выполнения 0.0009980201721191406
Копирование списка
Время выполнения 0.000997304916381836
Отчистка списка"""


@benchmark
def dict_search():
    for el in my_dict.keys():
        if el == 'key_30000':
            return f"Поиск в словаре по ключу"


print(dict_search())


@benchmark
def dict_values():
    for el in my_dict.values():
        if el == 'value_30000':
            return f"Поиск в словаре по значению"


print(dict_values())


@benchmark
def list_search():
    for el in range(len(my_list)):
        if my_list[el] == 30000:
            print(el)
    return "Поиск по списку"


print(list_search())


@benchmark
def dict_copy():
    my_dict.copy()
    return f'Копирование словаря'


print(dict_copy())


@benchmark
def dict_clear():
    my_dict.clear()
    return f'Отчистка словаря'


print(dict_clear())


@benchmark
def list_copy():
    my_list.copy()
    return f'Копирование списка'


print(list_copy())


@benchmark
def list_clear():
    my_list.clear()
    return f'Отчистка списка'


print(list_clear())
