"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import time


# Декоратор измерения времени работы функции
def time_check_decor(func):
    def time_check(a):
        start_val = time.time()
        func(a)
        end_val = time.time()
        return print(func(a), end_val - start_val)

    return time_check


# Заполнение списка
@time_check_decor
def check_list(a):
    my_list = [i for i in range(1, a)]
    return f'Генерация списка из {a} элементов -'


check_list(10000000)


# Заполнение словаря
@time_check_decor
def check_dict(a):
    my_dict = {x: x for x in range(a)}
    return f'Генерация словаря из {a} элементов -'


check_dict(10000000)

# извлечение из списка элементов
my_list = [i for i in range(1, 100000)]


@time_check_decor
def out_list(a):
    while a:
        a.pop(0)
    return f'Удаление элементов списка -'


out_list(my_list)

# извлечение из словаря элементов
my_dict = {x: x for x in range(100000)}


@time_check_decor
def out_dict(a):
    while a:
        a.popitem()
    return f'Удаление элементов списка -'


out_dict(my_dict)
