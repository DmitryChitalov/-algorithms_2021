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
from time import time

num_it = 10**7


def time_func(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        print(time() - start_time)
        return res
    return wrapper_timer


@time_func
def gen_list(n):
    print('Заполнение списка:')
    res = [i for i in range(n)]
    return res


gen_l = gen_list(num_it)


@time_func
def gen_dict(n):
    print('Заполнение словаря:')
    result = {i: i for i in range(n)}
    return result


gen_d = gen_dict(num_it)


# список будет заполнен быстрее, т.к. при генерации словаря еще создаются хеши


@time_func
def find_list(n):
    print('Поиск в листе:')
    n.index(num_it//2)


find_list(gen_l)


@time_func
def find_dict(n):
    print('Поиск в словаре:')
    n.get(num_it//2)


find_dict(gen_d)

# поиск по ключу словаря практически мгновенный, т.к. словарь - хеш-таблица. Поиск в списке - O(n)


@time_func
def clear_list_list(n):
    print('Очищение списка:')
    n.clear()


clear_list_list(gen_l)


@time_func
def clear_list_dict(n):
    print('Очищение словаря:')
    n.clear()


clear_list_dict(gen_d)

# список меньше словаря, поэтому очищение быстрее
