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

# очищение списка происходит быстрее словаря, так как меньше его

from time import time

num = 10**7


def time_function(function):

    def wrapper_timer(*args, **kwargs):

        start_time = time()

        result = function(*args, **kwargs)

        print(time() - start_time)

        return result

    return wrapper_timer


@time_function
def main_list(n):

    print('Заполнение списка:')

    result = [i for i in range(n)]

    return result


main_list_list = main_list(num)


@time_function
def main_dict(n):

    print('Заполнение словаря:')

    result = {i: i for i in range(n)}

    return result


main_dict_dict = main_dict(num)


# список будет заполнен быстрее, т.к. при генерации словаря еще создаются хеши


@time_function
def list_find(n):

    print('Поиск в листе:')

    n.index(num//2)


list_find(main_list_list)


@time_function
def dict_find(n):

    print('Поиск в словаре:')

    n.get(num//2)


dict_find(main_dict_dict)

# поиск по ключу словаря практически мгновенный, т.к. словарь - хеш-таблица. Поиск в списке - O(n)


@time_function
def clear_list(n):

    print('Очищение списка:')

    n.clear()


clear_list(main_list_list)


@time_function
def clear_dict(n):

    print('Очищение словаря:')

    n.clear()


clear_dict(main_dict_dict)
