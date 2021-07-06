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
random_list = []
random_dict = {}


def end_list_append(lst, n):
    for i in range(n):
        lst.append(i)  # O(1)


start_time = time.time()
end_list_append(random_list, 1000)
print(time.time() - start_time)


def start_list_append(lst, n):
    for i in range(n):
        lst.insert(0, i)  # O(n)


start_time = time.time()
start_list_append(random_list, 1000)
print(time.time() - start_time)


def dict_append(dct, n):
    for i in range(n):
        dct[i] = i  # O(1)


start_time = time.time()
dict_append(random_dict, 1000)
print(time.time() - start_time)


def change_list_pop(lst, n):
    for i in range(n):
        lst.pop()  # O(n)


start_time = time.time()
change_list_pop(random_list, 1000)
print(time.time() - start_time)


def change_list(lst, n):
    for i in range(n):
        lst[i] = lst[i+1]  # O(1)


start_time = time.time()
change_list_pop(random_list, 1000)
print(time.time() - start_time)


def change_dict_pop(dct, n):
    for i in range(n):
        dct.pop(i)  # O(n)


start_time = time.time()
change_dict_pop(random_dict, 1000)
print(time.time() - start_time)


def change_dict(dct, n):
    for i in range(n):
        dct[i] = 'ok'  # O(1)


start_time = time.time()
change_dict(random_dict, 1000)
print(time.time() - start_time)
