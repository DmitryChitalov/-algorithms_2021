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


"""В этом задании проработал код который обьясняли на уроке
 и разобрался с декораторами"""


from time import time

my_list = []
my_dict = {}
count = 1000000


def check_time_decorator(func):
    def check_time(*args, **kwargs):
        start_val = time()
        out_func = func(*args, **kwargs)
        end_val = time()
        print(f'Время выполнения: {end_val - start_val}')
        return out_func
    return check_time


@check_time_decorator
def fill_list_append(data, count):
    for i in range(count):
        data.append(i)


print('Вставляем в конец списка, сложность О(1)')
fill_list_append(my_list, count)


@check_time_decorator
def fill_list_insert(data, cnt):
    for i in range(cnt):
        data.insert(0, i)


print('Встаяляем в начало списка сложность О(n)')
fill_list_insert(my_list, count)


@check_time_decorator
def fill_dict(data, cnt):
    for i in range(cnt):
        data[i] = i


print('Заполняем словарь, т.к. ключи хешируются, операция быстрая O(1)')
fill_dict(my_dict, count)


@check_time_decorator
def change_list(data):
    for i in range(1000):
        data.pop(i)
    for j in range(1000):
        data[j] = data[j + 1]


print('Удаление (у нас из начала списка O(n), получение элементов по O(1)')
change_list(my_list)


@check_time_decorator
def change_dict(data):
    for i in range(1000):
        data.pop(i)
    for j in range(1001, 2002):
        data[j] = '01010101'


print('Операции в словарях все константной сложности.')
change_dict(my_dict)
