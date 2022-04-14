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
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import time
import random


def work_time(func):
    def time_count(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        work = end_time - start_time
        print(f'Время выполнения функции {func.__name__}: {work} сек')
    return time_count


@work_time
def fill_list(lst):
    for i in range(1, 10000):
        lst.append(i)


@work_time
def find_in_list(lst):
    for i in range(1, 100):
        n = random.randint(1, 10000)
        if n in lst:
            continue


@work_time
def fill_dict(dct):
    for i in range(1, 10000):
        dct[i] = i


@work_time
def find_in_dict_values(dct):
    for i in range(1, 100):
        n = random.randint(1, 10000)
        for key in dct.keys():
            if dct[key] == n:
                continue


empty_list = []
empty_dict = {}
fill_list(empty_list)
fill_dict(empty_dict)
find_in_list(empty_list)
find_in_dict_values(empty_dict)

"""
И список и словарь заполняются за 0.0 сек, но логично предположить, что список заполняется быстрее, так как в списке
заполняется только значение, в то время как в словаре заполняются и ключи, и значения, что занимает больше времени.

Операции со списком, опять же, выполняются быстрее. Например, поиск значения в спике занял 0.01561427116394043 сек,
а в словаре - 0.0312502384185791 сек. Иногда поиск в списке проходит за 0.0 сек, что подтверждает гипотезу о том, что 
операции со словарями выполняются доольше. Происходит это потому, что словарь имеет более сложную структруру - 
ключ и значение, в то время, как у списка есть только значение
"""
