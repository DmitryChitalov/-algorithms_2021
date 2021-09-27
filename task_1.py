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
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time, '\n')
        return res
    return wrapped


@time_of_function
def filling_list():
    #Сложность: O(1).
    result = []
    for num in range(10000):
        result.append(num)
    return result


@time_of_function
def filling_dict():
    #Сложность: O(1).
    result = {}
    for num in range(10000):
        result[num] = num
    return result


@time_of_function
def change_list(some_list):
    #Сложность O(1)
    for el in range(9999, 9000, -1):
        some_list.pop(el)
    for el in range(9000):
        some_list[el] = some_list[el + 1]


@time_of_function
def change_dict(some_dict):
    #Сложность O(1).
    for key in range(9999, 9000, -1):
        some_dict.pop(key)
    for key in range(9001):
        some_dict[key] = 'update'


#Изменив алгоритмы и увеличив количество элементов получил результат:
#1) Списки заполняются быстрее словарей;
#2) Операции изменения быстрее реализованы в словарях.


if __name__ == '__main__':
    change_list(filling_list())
    change_dict(filling_dict())
