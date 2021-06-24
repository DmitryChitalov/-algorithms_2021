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

N = 100000


def get_runtime(func):

    def timer(*arg, **kwargs):
        start = time.time()
        function = func(*arg, **kwargs)
        end = time.time()
        print(f'Время выполнения функции: {func.__name__} - {end - start}')
        return function

    return timer


@get_runtime
def list_append(my_lst):
    for i in range(N):
        my_lst.append(i)
    return my_lst


@get_runtime
def list_append_tuple(my_lst):
    for i in range(N):
        my_lst.append((i, i + 1))
    return my_lst


@get_runtime
def dict_add(my_dct):
    for i in range(N):
        my_dct[i] = i + 1           # O(1)
    return my_dct


@get_runtime
def list_insert(my_lst):
    for i in range(N):
        my_list.insert(0, i)        # O(n)
    return my_lst


@get_runtime
def list_update(my_lst):
    for i in range(len(my_lst)):
        my_lst[i] = i + 10
    return my_lst


@get_runtime
def dict_update(my_dct):
    for i in range(N):
        my_dct[i] = i + 1
    return my_dct


@get_runtime
def list_pop(my_lst):
    for i in range(50000):
        my_lst.pop(i)
    return my_lst


@get_runtime
def dict_pop(my_dct):
    for i in range(N):
        my_dct.pop(i)
    return my_dct


my_list = []
my_dict = {}
list_append(my_list)
my_list.clear()
list_append_tuple(my_list)
my_list.clear()
list_insert(my_list)
dict_add(my_dict)
list_update(my_list)
dict_update(my_dict)
list_pop(my_list)
dict_pop(my_dict)
"""
Вывод:
Словарь заполняется медленее, чем список с методом append, поскольку и в том и в другом случае, мы имеем сложность
O(1) - константа, однако в список мы добавляем лишь 1 элемент, а в словарь пару - ключ:значение
Однако, если мы попробуем добавлять в список элементы в его начало, используя insert, то такой алгоритм будет 
работать гораздо медленнее, чем словарь, а также если мы будем добавлять в список не по одному элементу, а парой, 
как в словарь,то список также будет заполняться медленее.
Обновление данных в списке работает также быстрее, чем в словаре, однако стоит учитывать, что словарь содержит пару
ключ-значение, а список лишь одиночные элементы.
Удаление же элементов из словаря работает гораздо быстрее, чем удаление элементов из списка. В моем примере, времени
на удаление элементов лишь половины списка потребовалось в разы больше, чем удаление элементов всего словаря. 
"""
