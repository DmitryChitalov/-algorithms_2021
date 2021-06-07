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


from random import randint
from time import time

my_list = []
my_dict = {}


def my_timer(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer


@my_timer
def list_append(lst, n):
    for i in range(n):
        lst.append(i)


list_append(my_list, 1000000)
print()


@my_timer
def dict_append(dct, n):
    for i in range(n):
        dct[i] = i


dict_append(my_dict, 1000000)
print()


# Операции удаления, получения по индексу и ключу
@my_timer
def change_list(lst):
    for i in range(10000):
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]


change_list(my_list)
print()


@my_timer
def change_dict(dct):
    for i in range(10000):
        dct.pop(i)
    for j in range(1001, 2002):
        dct[j] = 'fill'


change_dict(my_dict)
print()

# Заполнение словаря происходит быстрее, чем списка, т.к. он представляет собой хеш-таблицу и операция имеет константную сложность.
# Заполнение списка имеет линейную сложность
# Аналогично обрабатываются операции по изменению списка и словаря - у словаря намного быстрее при константной сложности.
