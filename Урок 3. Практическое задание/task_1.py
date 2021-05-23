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
from time import time
from random import randint


def timer(function):
    def wrap(*args):
        start = time()
        result = function(*args)
        print(f'Время потраченое на выполнение функции: {time() - start}')
        return result
    return wrap


@timer
def list_random(n):
    lst = [randint(0, 10) for el in range(n)]
    return lst


@timer
def dict_random(n):
    dct = {el: randint(0, 10) for el in range(n)}
    return dct


n = randint(1000000, 2000000)
lst = list_random(n)
print(f'Длина списка = {len(lst)}')
dct = dict_random(n)
print(f'Длина словаря = {len(dct)}')

# Время заполнения списка меньше чем заполнение словаря, так как нет расчета хеш значений для элементов словаря
# а также у словаря больше элементов


@timer
def get_list_random(lst):
    return lst.pop(randint(0, n))


@timer
def get_dct_random(dct):
    return dct.pop(randint(0, n))


print(f'Находим элемент в списке и удаляем его: {get_list_random(lst)}')
print(f'Находим элемент в словаре и удаляем его: {get_dct_random(dct)}')

# Поиск в словаре происходит быстрее из за хеширования значений


@timer
def clear_list_random(lst):
    return lst.clear()


@timer
def clear_dct_random(dct):
    return dct.clear()


print(f'Очищаем список: {clear_list_random(lst)}')
print(f'Очищаем словарь: {clear_dct_random(dct)}')

# Очистка списка идет быстрее, так как меньше элементов надо удалять

