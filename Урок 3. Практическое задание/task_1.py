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
    def wrapped():
        global times_lst
        start_time = time.time()
        function()
        times_lst.append(time.time() - start_time)
    return wrapped


@time_of_function
def list_generator():
    global lst
    lst = [a for a in range(1, 1000000)]


@time_of_function
def dict_generator():
    global dct
    dct = {a: a for a in range(1, 1000000)}
    return dct


@time_of_function
def list_actions():     #O(n)
    min(lst)
    max(lst)
    lst.reverse()
    lst.sort()
    len(lst)
    for _ in lst:
        pass


@time_of_function
def dict_actions():     #O(n)
    dct[123] = 321
    len(dct)
    dct.keys()
    for _ in dct.values():
        pass
    dct.popitem()
    dct.clear()


lst = []
dct = {}
times_lst = []
for _ in range(0, 10):
    list_generator()
    list_actions()
    dict_generator()
    dict_actions()

for i in range(0, 40):
    print(f'{times_lst[i]:.6f}', end='\t')
    if (i + 1) % 4 == 0:
        print()

# Заполнение словаря происходит медленне заполнения списка