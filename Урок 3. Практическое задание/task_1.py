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

import time


def performance_measurement(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        return run_time
    return wrapper


@performance_measurement
def list_fill(n):
    test_fill_list = list()
    for i in range(n):
        test_fill_list.append(i)


@performance_measurement
def dict_fill(n):
    test_fill_dict = dict()
    for i in range(n):
        test_fill_dict[i] = i


@performance_measurement
def list_read(t_list):
    for i in range(len(t_list)-1):
        i


@performance_measurement
def dict_read(t_dict):
    for i in range(len(t_dict)-1):
        t_dict[i]


l_time = list_fill(1000000)
d_time = dict_fill(1000000)

if l_time > d_time:
    print('Быстрее заполняется список')
elif l_time < d_time:
    print('Быстрее заполняется словарь')
else:
    print('Нет никакой разницы.')

# На записе миллиона значений у меня получается то список быстрее то словарь :-)

test_list = [i for i in range(1000000)]
test_dict = dict()
for i in range(1000000):
    test_dict[i] = i

print(list_read(test_list))
print(dict_read(test_dict))

# Получается что прочитать весь список быстрее чем весь словарь

