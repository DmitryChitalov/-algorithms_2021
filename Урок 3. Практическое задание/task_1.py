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

from random import randint
import time


def counting_time(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        result_time = end_time - start_time
        return result_time
    return wrapper


@counting_time
def add_lst(lst):  # O(N)
    for i in range(1000000):  # O(N)
        lst.append(randint(-10, 10))  # O(1)
    return lst  # O(1)


@counting_time
def pop_lst(lst):  # O(N)
    for i in range(999999):  # O(N)
        lst.pop()  # O(1)
    return lst  # O(1)


@counting_time
def add_dictionary(dic):  # O(N)
    for i in range(1000000):  # O(N)
        dic[str(i)] = randint(-10, 10)
    return dic  # O(1)


@counting_time
def pop_dictionary(dic):  # O(N)
    for i in range(999999):  # O(N)
        dic.pop(str(i))  # O(1)
    return dic  # O(1)


my_lst = []
my_dictionary = {}

print(f'add_lst time: {add_lst(my_lst)}')
print(f'add_dictionary time: {add_dictionary(my_dictionary)}')
print(f'pop_lst time: {pop_lst(my_lst)}')
print(f'pop_dictionary time: {pop_dictionary(my_dictionary)}')

'''
Выполнение практически одинаковых операций в списках занимает ощутимо меньше времени, чем в словарях.
Это происходит из-за того, что при добавлении ключей в словарь вычисляется их хеш.
'''

# ##########################  ADD  ##########################
#
# start_time = time.time()
#
# add_lst(my_lst)
#
# end_time = time.time()
# result_time = end_time - start_time
#
# print(f'add_lst time: {result_time}')
#
# start_time = time.time()
#
# add_dictionary(my_dictionary)
#
# end_time = time.time()
# result_time = end_time - start_time
#
# print(f'add_dictionary time: {result_time}')
#
# #######################  POP  #######################
#
# start_time = time.time()
#
# pop_lst(my_lst)
#
# end_time = time.time()
# result_time = end_time - start_time
#
# print(f'pop_lst time: {result_time}')
#
# start_time = time.time()
#
# pop_dictionary(my_dictionary)
#
# end_time = time.time()
# result_time = end_time - start_time
#
# print(f'pop_dictionary time: {result_time}')
