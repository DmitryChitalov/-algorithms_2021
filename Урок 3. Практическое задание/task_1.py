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
from time import time
from sys import getsizeof


def timer(func):
    def wrapped(*args):
        start = time()
        response = func(*args)
        print(f'Время выполнения функции {func.__name__}: {time() - start:.6}')  #
        return response
    return wrapped


@timer
def fill_list():  # заполнение списка
    l = []
    for i in range(1000000):
        l.append(f'element{i}')
    return l

@timer
def fill_dict():  # заполнение словаря
    d = {}
    for i in range(1000000):
        d[i] = f'element{i}'
    return d

@timer
def operate_list_On(l):  # функция операций со списком с линейной сложностью O(n)
    for i in range(len(l)):
        l[i] = l[i].replace('me', 'pha')
    return l


@timer
def operate_list_On2(l):  # функция операций со списком с квадратичной сложностью O(n^2)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in 'elph':
                l[i] = l[i].replace(l[i][j], '-')
    return l


@timer
def operate_dict_On(d):  # функция операций со словарем с линейной сложностью O(n)
    for i in d:
        d[i] = d[i].replace('me', 'pha')
    return d


@timer
def operate_dict_On2(d):  # функция операций со словарем с квадратичной сложностью O(n^2)
    for i in d:
        for j in range(len(d[i])):
            if d[i][j] in 'elph':
                d[i] = d[i].replace(d[i][j], '-')
    return d


# заполнение массивов
lst = fill_list()
dct = fill_dict()
# замеры памяти для созданных массивов
print(f'Количество памяти для lst: {getsizeof(lst)} b')
print(f'Количество памяти для dct: {getsizeof(dct)} b')
# выполнение операций над массивами и замеры
lst = operate_list_On(lst)
lst = operate_list_On2(lst)
dct = operate_dict_On(dct)
dct = operate_dict_On2(dct)

# функции с квадратичной сложностью выполняются примерно
# в десять раз дольше линейных функций с похожим функционалом
# словарь занимает в пять раз больше памяти, из-за хеширования ключей и коллизии
