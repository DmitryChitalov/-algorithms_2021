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

# a) заполнение списка и словаря программно,
#    сделайте замеры и сделайте выводы, что выполняется быстрее и почему
import time


def with_measure_time(fn):
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        performed_time = end_time - start_time
        print(f'{fn.__name__} performed in {performed_time}')
        return result
    return wrapped


@with_measure_time
def generate_array(size):
    array = []
    for i in range(size):
        array.append(i)
    return array


@with_measure_time
def generate_dictionary(size):
    dictionary = {}
    for i in range(size):
        dictionary[i] = i
    return dictionary

# generate_array performed in 0.11853909492492676
array = generate_array(pow(10, 6))

# generate_dictionary performed in 0.15125679969787598
dictionary = generate_dictionary(pow(10, 6))

# заполненеие словаря происходит быстрее, потому что при его создание нужно генерировать хэши ключей, при заполнение же массива данные р


# b) выполните набор операций и со списком, и со словарем,
#    сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

import random

@with_measure_time
def array_find_operation_speed_test(array, number):
    array_len = len(array)
    for i in range(number):
        find_el = random.randint(0, array_len - 1)
        array.index(find_el)


@with_measure_time
def dictionary_find_operation_speed_test(dictionary, number):
    dictionary_len = len(dictionary)
    for i in range(number):
        find_el = random.randint(0, dictionary_len - 1)
        dictionary[find_el]


# array_find_operation_speed_test performed in 0.13517403602600098
array_find_operation_speed_test(array, pow(10, 1))

# dictionary_find_operation_speed_test performed in 2.8848648071289062e-05
dictionary_find_operation_speed_test(dictionary, pow(10, 1))

# поиск элемента в словаре в разы быстрее, потому что сложность такого поиска O(1) по сравнению со списком O(n)
# из-за того, чтобы взять элемент из словаря нужно сделать хэш и по нему обратиться за элементом
# в случае списка же нужно перебирать каждый элемент, пока не найдем нужный
