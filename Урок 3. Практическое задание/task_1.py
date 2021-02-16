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


def time_taken(function):
    global start_time

    def wrapper(*args):
        start_time = time()
        result = function(*args)
        print(f"Выполнение функции заняло {round(time() - start_time, 4)} == {time() == start_time}")
        return result

    return wrapper


@time_taken
def fulfill_dict(n):
    dict = {}
    print(f"Наполняем словарь {n} элементами")
    for i in range(0, n):
        dict.update({i: 'j'})
    return dict


@time_taken
def fulfill_list(n):
    lst = []
    print(f"Наполняем список {n} элементами")
    for i in range(0, n):
        lst.append('j')
    return lst


@time_taken
def add_elem_to_dict(dict):
    print("Добавляем элемент в словарь")
    dict.update({'qwe': 'qwe'})


@time_taken
def add_elem_to_list(lst):
    print("Добавляем элемент в список")
    lst.append('qwe')


n = 1000000
my_dict = fulfill_dict(n)
my_list = fulfill_list(n)
print("*" * 50)
add_elem_to_dict(my_dict)
add_elem_to_list(my_list)
print("*" * 50)
