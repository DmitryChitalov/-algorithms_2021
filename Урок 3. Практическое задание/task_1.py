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
from random import randint


def time_taken(function):
    global start_time

    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        print(f"Выполнение функции заняло {time() - start_time}")
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
        lst.append(i)
    return lst


@time_taken
def add_elem_to_dict(dict, elems_to_add):
    print(f"Добавляем {len(elems_to_add)} элементов в словарь")
    for elem in elems_to_add:
        dict.update({elem: elem})


@time_taken
def add_elem_to_list(lst, elems_to_add):
    print(f"Добавляем {len(elems_to_add)} элементов в список")
    for elem in elems_to_add:
        lst.append(elem)


@time_taken
def remove_elements_from_dict(dict, lst_of_keys):
    print(f"Удаляем {len(lst_of_keys)} элементов из словаря")
    for key_ in lst_of_keys:
        dict.pop(key_)


@time_taken
def remove_elements_from_lst(lst, list_of_elems):
    print(f"Удаляем {len(list_of_elems)} элементов из списка")
    for elem in list_of_elems:
        lst.pop(elem)


@time_taken
def insert_elements_into_lst(lst, lst_to_insert):
    print(f"Вставляем {len(lst_to_insert)} элементов в список")
    for elem in lst_to_insert:
        lst.insert(1000, elem)


@time_taken
def remove_elements_from_end_of_list(lst):
    print("Удаление 10000 элементов из конца списка")
    for i in range(10000):
        lst.pop()


@time_taken
def remove_elements_from_lst_by_index(lst):
    print("Удаление 10000 элементов из середины списка по индексу")
    for i in range(30000, 40000):
        lst.remove(i)


n = 1000000
lst_of_elements_to_add = [i for i in range(n, n + 100000)]
lst_of_elements_to_remove = [j for j in range(10000, 20000)]

my_dict = fulfill_dict(n)
my_list = fulfill_list(n)
print("*" * 50)

add_elem_to_dict(my_dict, lst_of_elements_to_add)
add_elem_to_list(my_list, lst_of_elements_to_add)
print("*" * 50)

remove_elements_from_dict(my_dict, lst_of_elements_to_remove)
remove_elements_from_lst(my_list, lst_of_elements_to_remove)
remove_elements_from_end_of_list(my_list)
remove_elements_from_lst_by_index(my_list)
print("*" * 50)

insert_elements_into_lst(my_list, lst_of_elements_to_remove)
print("*" * 50)
"""
Вывод:
1.Добавление элементов в словарь работает медленнее, чем добавление элементов в КОНЕЦ списка,
примерно в 3 раза на 1 миллионе элементов однотипных данных.
2.Удаление определенных элементов из словаря выполняется на порядки бысстрее,
чем удаление элементов из списка.
3.Вставка элементов в середину списка, так же занимет очень много времени. Вставка(добавление) в словарь занимает
одиинаковое время,т.к. список - структура данных неупорядоченая. поиск необходимых элементов осуществляется
за константное время, как и их удаление.

4.Запись элементов в конец списка и удаление элементов из конца списка - операции чамые быстрые, быстре чем добавление
и удаление элементов из словаря. Значит если необходимо записывать и считывать данные из хвоста списка, нужно
использовать список. Если необходимо часто осуществлять поиск элемента, то использовать словарь.
5. Список в питоне - это связный список, т.к. удаление элементов по значению, происходит примерно за то же время, что и
удаление элементов списка по индексу.
"""
