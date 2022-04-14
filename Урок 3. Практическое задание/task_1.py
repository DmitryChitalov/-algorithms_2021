"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и
   отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time

my_list = []
my_dict = {}
num_of_repetitions = 10 ** 5


def time_spend(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"время выполнения функции {func.__name__} составило {end - start}")
        return result

    return timer


@time_spend
def append_in_list(lst, n):  # сложность всей функции О(N)
    for i in range(n):  # сложность О(N)
        lst.append(i)  # сложность О(1)


append_in_list(my_list, num_of_repetitions)


@time_spend
def insert_in_list(lst, n):  # сложность всей функции О(N^2)
    for i in range(n):  # сложность О(N)
        lst.insert(0, i)  # сложность О(N)


insert_in_list(my_list, num_of_repetitions)


@time_spend
def insert_in_dict(dct, n):  # сложность всей функции О(N)
    for i in range(n):  # сложность О(N)
        dct[i] = i  # сложность О(1)


insert_in_dict(my_dict, num_of_repetitions)

"""
время выполнения функции append_in_list составило 0.006003379821777344
время выполнения функции insert_in_list составило 6.464010715484619
время выполнения функции insert_in_dict составило 0.009992599487304688
Заполнение списка и словаря линейными функциями сопоставимо по времени.
Подстановка в список через инсерт медленнее, так как там имеем квадратичную функцию и при каждой вставке все имеющиеся 
элементы сдвигаются внутри списка.
"""


@time_spend
def change_list(lst, n):  # сложность О(N)
    for i in range(n):  # сложность О(N)
        lst[i] += 100  # сложность О(1)


@time_spend
def clear_list(lst, n):  # сложность О(N^2)
    for i in range(n):  # сложность О(N)
        lst.pop(i)  # сложность О(N)


change_list(my_list, 10000)
clear_list(my_list, 10000)

"""
время выполнения функции change_list составило 0.001123189926147461
время выполнения функции clear_list составило 0.6600251197814941
В первой функции сложность ниже и время на выполнение значительно меньше
"""


@time_spend
def change_dict_value(dct, n):
    for i in range(n):
        dct[i] = "new value"


@time_spend
def del_dict_key(dct, n):
    for i in range(n):
        dct.pop(i)


change_dict_value(my_dict, 10000)
del_dict_key(my_dict, 10000)

"""
время выполнения функции change_dict_value составило 0.001001596450805664
время выполнения функции del_dict_key составило 0.0009987354278564453
Все функции со словарем имеют сложность O(N), при этом основные действия (удаление ключа и изменение значения у ключа)
имеют линейную сложность. В целом на операции по изменению словаря уходит меньше времени, что особенно заметно по 
функции del_dict_key.
"""