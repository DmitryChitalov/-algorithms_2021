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


import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time, '\n')
        return res
    return wrapped


@time_of_function
def filling_list(n=100):
    #Сложность: O(n).
    name = [x for x in range(n)]
    print('Filling list: ', end='')
    return name


@time_of_function
def filling_dict(n=100):
    #Сложность: O(n).
    name = {x:x for x in range(n)}
    print('Filling dict: ', end='')
    return name


@time_of_function
def read_list(some_list):
    #Сложность: O(n^2).
    [some_list.index(el) for el in some_list]
    print('List read: ', end='')


@time_of_function
def read_dict(some_dict):
    # Сложность: O(n).
    [some_dict.get(el) for el in some_dict]
    print('Dict read: ', end='')


@time_of_function
def delete_list(some_list):
    # Сложность O(n).
    for idx in range(len(some_list), -1):
        some_list.pop(idx)
    print('List delete: ', end='')


@time_of_function
def delete_dict(some_dict):
    # Сложность: O(n).
    for key in range(len(some_dict), -1):
        some_dict.pop(key)
    print('Dict delete: ', end='')


# При заполнении словарь немного или много быстрее.
# При чтении словарь гораздо быстрее, из-за того, что разная сложность функций.
# При удалении примерно равны.
# PS: Эти значения скорости постоянно скачат, что сбивает с толку.


if __name__ == '__main__':
    some_list = filling_list()
    some_dict = filling_dict()
    read_list(some_list)
    read_dict(some_dict)
    delete_list(some_list)
    delete_dict(some_dict)
