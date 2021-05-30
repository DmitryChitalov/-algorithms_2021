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
from time import time_ns


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time_ns()
        result = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__}: {time_ns() - start}')
        return result

    return wrapper


@timeit
def dict_fill(test_dict: dict, n: int) -> dict:
    for i in range(1, n + 1):
        test_dict[i] = i
    return test_dict


@timeit
def list_fill(test_list: list, n: int) -> list:
    for i in range(1, n + 1):
        test_list.append(i)
    return test_list


@timeit
def dict_search(test_dict: dict, st: str) -> int:
    return test_dict.get(st, 0)


@timeit
def list_search(test_list: list, st: str) -> int:
    return test_list.index(st)


a = []
b = {}
test_ls = [str(i) for i in range(1000000)]
test_dict = {str(i): i for i in range(1000000)}

dict_fill({}, 100000)
list_fill([], 100000)
dict_search(test_dict, '999999')
list_search(test_ls, '999999')

"""
Время выполнения dict_fill: 16835100 - медленнее, чем у списка при одинаковой сложности O(n)
Время выполнения list_fill: 15720400
Время выполнения dict_search: 0 - моментально, сложность О(1)
Время выполнения list_search: 21959400 - сложность О(n)
"""
