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

def know_time(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@know_time
def fullfill_ls(n = 10000000):
    array_py = []
    for i in range(n):
        array_py.append(i)
    return array_py

@know_time
def fullfill_dict(n = 10000000):
    dictionary = {}
    for i in range(n):
        dictionary.setdefault(i)
    return dictionary


print("ls",fullfill_ls())

fullfill_dict()
