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


def time_measuring(func):
    def wrapper(*args, **kwargs):
        t = time()
        res = func(*args, **kwargs)
        print(f'Время выполнения функции: {(time() - t)}')
        return res
    return wrapper


@time_measuring
def list_filling(size):
    user_list = [i for i in range(size)]
    return user_list


@time_measuring
def list_filling_2(size):
    user_list = []
    for el in range(size):
        user_list.append(el)
    return user_list


@time_measuring
def list_call(list, element):
    return list[element]

@time_measuring
def list_pop_element(list, element):
    list.pop(element)

@time_measuring
def list_remove_element(list, value):
    list.remove(value)

@time_measuring
def list_insert_element(list, el_1, el_2):
    list.insert(el_1, el_2)


@time_measuring
def dict_filling(size):
    user_dict = {i: i for i in range(size)}
    return user_dict

@time_measuring
def dict_filling_2(size):
    user_dict = {}
    for el in range(size):
        user_dict.update({el: el})
    return user_dict

@time_measuring
def dict_call(dict, element):
    return dict[element]

@time_measuring
def dict_pop(dict, key):
    dict.pop(key)

@time_measuring
def dict_get(dict, key):
    dict.get(key)


number_elements = int(input('input number elements'))

print('Generate list comprehension')
list_1 = list_filling(number_elements)

print('\nGenerate list with for + .append')
list_2 = list_filling_2(number_elements)

print('\nCall element from list')
print(list_call(list_1, randint(0, number_elements)))
print('Pop element from list')
list_pop_element(list_1, randint(0, number_elements))
print('Remove element with value')
list_remove_element(list_1, randint(0, number_elements))
print('Insert element in list')
list_insert_element(list_1, randint(0, number_elements), randint(0, number_elements))

print('\nGenerate dict with dict comprehension')
dict_1 = dict_filling(number_elements)
print('\nGenerate dict with for + dict update')
dict_2 = dict_filling_2(number_elements)

print('\nDict call element')
print(dict_call(dict_1, randint(0, number_elements)))
print('Dict pop element by key')
dict_pop(dict_1, randint(0, number_elements))
print('Dict get')
dict_get(dict_1, randint(0, number_elements))


'''
input number elements100000000
Generate list comprehension
Время выполнения функции: 4.241968631744385

Generate list with for + .append
Время выполнения функции: 7.334787368774414

Call element from list
Время выполнения функции: 0.0
14094696
Pop element from list
Время выполнения функции: 0.10209274291992188
Remove element with value
Время выполнения функции: 0.9183611869812012
Insert element in list
Время выполнения функции: 0.10709905624389648

Generate dict with dict comprehension
Время выполнения функции: 19.583229780197144

Generate dict with for + dict update
Время выполнения функции: 26.46024775505066

Dict call element
Время выполнения функции: 0.0
87860155
Dict pop element by key
Время выполнения функции: 0.0
Dict get
Время выполнения функции: 0.0010006427764892578

Генерация как списка так и словаря на порядок быстрее происходит при использовании comprehension
Вызов элемента из списка по индексу эелемента происходит моментально.
Удаление элемента из списка по индексу методом pop происходит гораздо быстрее чем метод remove,
хотя это совсем разные методы и сравнивать их некорректно.

Получение элементов из словаря методами get и просто обращение по ключу почти одинаково.
Удаление элемента по ключу в словаре вообще не занимает никакого времени.
'''


