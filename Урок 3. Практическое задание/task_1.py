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
# Заполнения словаря будет быстрее всего, т.к. она представляет из себя хеш таблицу и у операций будет сложность O(1)

def times(function):
    import time

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f'Время выполнения функции {function.__name__}: '
              f'{end - start}')

    return wrapper


dict = {}
lst = []


@times
def fill_dict(): # O(1)
    for el in range(10000):
        dict[el + 1] = el

fill_dict()


@times
def dict_pop(): # O(1)
    for el in range(len(dict)):
        dict.pop(el + 1)


dict_pop()


@times
def fill_list_append(): # O(1)
    for el in range(10000):
        lst.append(el)


fill_list_append()


@times
def list_remove(): # O(n)
    for el in range(len(lst)):
        lst.remove(el)


list_remove()


@times
def fill_list_insert(): # O(n)
    for el in range(10000):
        lst.insert(0, el)


fill_list_insert()