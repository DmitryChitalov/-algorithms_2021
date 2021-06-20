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


array_length = 1000000
my_list = []
my_dict = {}


def timer_func(func):
    def a(quantity, array):
        start = time.time()
        func(quantity, array)
        end = time.time()
        return end - start
    return a


@timer_func
def list_fill(quantity, some_list):
    for i in range(quantity):
        some_list.append(i)



@timer_func
def dict_fill(quantity, some_dict):
    for i in range(quantity):
        some_dict[i] = i


print(list_fill(array_length, my_list))   # 0.25000905990600586
print(dict_fill(array_length, my_dict))   # 0.3281373977661133
# Словарь заполняется медленнее так как программе приходиться формировать и значение и ключ


@timer_func
def list_del_elem(quantity, some_list):
    for i in range(quantity):
        del some_list[i]


@timer_func
def dict_del_elem(quantity, some_dict):
    for i in range(quantity):
        del some_dict[i]


print(list_del_elem(int(array_length/1000), my_list))  # 6.922288179397583
print(dict_del_elem(int(array_length/100), my_dict))   # 0.01561737060546875
# Поэлементное удаление работает намного быстрее в словарях, потому что сложность
# операции со списками - O(n), а со словарями - O(1)
