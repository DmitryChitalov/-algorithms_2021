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
import random


def check_time(func):
    def wrap(*args):
        time_start = time.time()
        ret = func(*args)
        time_end = time.time()
        print(func.__name__, time_end - time_start)
        return ret

    return wrap


ex_list = []
ex_dict = {}


#Сложность O(n)
@check_time
def fill_list():
    for i in range(10):                                 # O(n)
        ex_list.append(i+1)                             # O(1)


#Сложность O(n)
@check_time
def fill_dict():
    for i in range(10):                                 # O(n)
        ex_dict.setdefault(i+1, chr(97+i))   # O(1)


fill_list()
fill_dict()


print(ex_list)
print(ex_dict)

n = random.randint(1,9)

@check_time
def input_list():
    ex_list[n] = n+n            # O(1)


@check_time
def input_dict():
    ex_dict[n] = n+n            # O(1)

input_list()
input_dict()

print(ex_list)
print(ex_dict)

@check_time
def pop_list():
    ex_list.pop(n)              # O(n)

@check_time
def pop_dict():
    ex_dict.pop(n)              # O(1)



pop_list()
pop_dict()

print(ex_list)
print(ex_dict)

@check_time
def clear_list():
    ex_list.clear()         # O(1)

@check_time
def clear_dict():
    ex_dict.clear()         # O(1)

clear_list()
clear_dict()

print(ex_list)
print(ex_dict)


