"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time

list_fill = []
dict_fill = {}
n = 10 ** 5


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__} составило {end - start}')
        return result

    return timer


@time_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)  # O(1)


fill_list_append(list_fill, n)


@time_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)  # O(n)


fill_list_insert(list_fill, n)


@time_decorator
def fill_dict(dct, num):
    for i in range(num):  # Добавление нового элемента имеет сложность O(1)
        dct[i] = i


fill_dict(dict_fill, n)


@time_decorator
def change_list(lst):
    for i in range(1000):
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]


change_list(list_fill)

#  для change_list(lst) сложность O(n), так как указан i? Обращение по индексу для изменения - сложность O(1)


@time_decorator
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for j in range (1001, 2002):
        dct[j] = 'fill'


change_dict(dict_fill)
# все операции по изменению словаря проходят по сложности O(1)
