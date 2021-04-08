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


def count_time(func):
    def inner(data_of_func):
        start_time = time.perf_counter()
        result = func(data_of_func)
        print(f'Время: {time.perf_counter() - start_time:0.6f} секунд')
        return result
    return inner


# Наполнение(вставка)
# Список заполняется быстрее, так как не нужно делать хеш в отличии от словаря.
@count_time
def list_1(digit):
    items = []
    for i in range(digit):
        items.append(i)
    return items


@count_time
def list_2(digit):
    return [i for i in range(digit)]


@count_time
def dict_1(digit):
    return {i: i for i in range(digit)}


@count_time
def dict_2(digit):
    result = {}
    for i in range(digit):
        result[i] = i
    return result


# Удаление
# В словаре удаление быстрее, так есть хеш, список идет по алгоритму O(n)
@count_time
def list_3(digit):
    for i in range(1, 5000):
        digit.pop(i)


@count_time
def dict_3(digit):
    for i in range(1, 5000):
        digit.pop(i)


# Поиск
# Аналогично примерам выше поиск быстрее в Словаре за счет хеша
@count_time
def list_4(digit):
    digit.index(5000)


@count_time
def dict_4(digit):
    digit.get(5000)


# Данные для вставки
data_list = [i for i in range(50000)]
data_dict = {i: i for i in range(50000)}


print("*" * 40)
print(f'Наполнение(вставка) Список_1')
list_1(500000)
print("*" * 40)
print(f'Наполнение(вставка) Список_2')
list_2(500000)
print("*" * 40)
print(f'Наполнение(вставка) Словарь_1')
dict_1(500000)
print("*" * 40)
print(f'Наполнение(вставка) Словарь_2')
dict_2(500000)
print("*" * 40)
print(f'Удаление Список')
list_3(data_list)
print("*" * 40)
print(f'Удаление Словарь')
dict_3(data_dict)
print("*" * 40)
print(f'Поиск в Списке')
list_4(data_list)
print("*" * 40)
print(f'Поиск в Словаре')
dict_4(data_dict)
print("*" * 40)
