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

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time

count_elms = 200000
lst = []
dct = {}

lst_1 = []
dct_1 = {}


def exec_time_checker(func):
    def checker(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        exec_time = end - start
        print(f'Время выполнения функции {func.__name__} равно {exec_time}')
        return result

    return checker


@exec_time_checker
def list_fill_app(some_lst):     # O(n)

    for i in range(count_elms):  # O(n)
        some_lst.append(i)       # O(1)


@exec_time_checker
def list_fill_ins(some_lst):     # O(n^2)

    for i in range(count_elms):  # O(n)
        some_lst.insert(0, i)    # O(n)


@exec_time_checker
def dict_fill(some_dct):         # O(n)

    for i in range(count_elms):  # O(n)
        some_dct[i] = i          # O(1)


@exec_time_checker
def list_del(some_lst):          # O(n^2)

    for i in range(100000):      # O(n)
        some_lst.pop(i)          # O(n)


@exec_time_checker
def dict_del(some_dct):          # O(n)

    for i in range(100000):      # O(n)
        some_dct.pop(i)          # O(1)


@exec_time_checker
def list_modif(some_lst):        # O(n)

    for i in range(100000):      # O(n)
        some_lst[i] = i + 1      # O(1)


@exec_time_checker
def dict_modif(some_dct):        # O(n)

    for i in range(100000):      # O(n)
        some_dct[i] = i - 1      # O(1)


@exec_time_checker
def list_extend(from_lst, to_lst):   # O(n)

    to_lst.extend(from_lst)


@exec_time_checker
def dict_update(from_dct, to_dct):   # O(n) - не нашла информации о сложности операции update,
    to_dct.update(from_dct)          # но пердопложила, что она линейная.


# start = time()
list_fill_app(lst)
# end = time()
# result = end - start
# print(f'Время выполнения функции заполнения списка через append: {result}')

# start = time()
list_fill_ins(lst)
# end = time()
# result = end - start
# print(f'Время выполнения функции заполнения списка через insert: {result}')

# start = time()
dict_fill(dct)
# end = time()
# result = end - start
# print(f'Время выполнения функции заполнения словаря: {result}')

# start = time()
list_del(lst)
# end = time()
# result = end - start
# print(f'Время выполнения функции удаления элемента из списка: {result}')

# start = time()
dict_del(dct)
# end = time()
# result = end - start
# print(f'Время выполнения функции удаления элемента из словаря: {result}')

# start = time()
list_modif(lst)
# end = time()
# result = end - start
# print(f'Время выполнения функции изменения элементов списка: {result}')

# start = time()
dict_modif(lst)
# end = time()
# result = end - start
# print(f'Время выполнения функции изменения элементов словаря: {result}')

# start = time()
list_extend(lst, lst_1)
# end = time()
# result = end - start
# print(f'Время выполнения функции расширения списка: {result}')

# start = time()
dict_update(dct, dct_1)
# end = time()
# result = end - start
# print(f'Время выполнения функции расширения словаря: {result}')

"""
Выводы:

- По функциям вставки элементов:
Между функциями вставки элементов в список через append и вставки элементов в словарь сильной разницы в скорости 
выполнения нет, алгоритмическая сложность одинаковая.
Функция вставки элементов в список через insert сильно отличается в худшую сторону, тк при каждой вствке элемента 
в начало, индексы последующих элементов пересчитываются. Алгоритмическая сложность O(n^2).

- По функциям удаления элементов:
Скорость удаления элементов из списка значительно ниже, скорости удаления такого же количества элементов из словаря, 
т.к алгоритмическая сложность удаления элемента из списка O(n), а при удалении некольких элементов через цикл 
получается O(n^2)одинаковая. Связано также с пересчетом индексов последующих элементов 
как и в случае с insert. При этом сложность удаления нескольких элементов из словаря - O(n).

- По функциям изменения значений элементов:
Скорость изменения значений одинакового количества элементов списка и словаря примерно одинакова. Алгоритмическая 
сложность функции изменения нескольких элементов через цикл в обоих случаях O(n). Скорость выскоая т.к. 
алгоритмы обращаются к элементам по индексам и ключам.

- По функциям расширения списка и словаря:
Скорость обоих алгоритмов очень высокая, т.к в обоих случаях новые элементы записываются в конец массива. 
Функция расширения словаря чуть медленнее.
"""

