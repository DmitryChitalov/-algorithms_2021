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


my_list = []
my_dict = {}
num_oper = 100000


def time_decorator(func):
    def timer(*arg, **kwargs):
        start = time()
        res = func(*arg, **kwargs)
        end = time()
        print(f'Время выполнения функции: {func.__name__} - {end - start}')
        return res
    return timer


@time_decorator
def fucn_list_append(my_list, num_oper):
    for i in range(num_oper):
        my_list.append(i)
    return my_list

@time_decorator
def fucn_list_insert(my_list, num_oper):
    for i in range(num_oper):
        my_list.insert(0, i)

@time_decorator
def func_dict(my_dict, num_oper):
    for i in range(num_oper):
        my_dict[i] = i
    return my_dict

# ----------------------------------------------------------------------------------------------------------------------

@time_decorator
def change_list(my_list):
    for i in range(10001):
        my_list[i] += 1
    for i in range(1001):
        my_list.pop(i)

@time_decorator
def change_dict(my_dict, num_oper):
    for i in range(num_oper):
        my_dict[i] = i + 1
    for i in range(num_oper): # ЧТО ВАЖНО у my_list удаляли 1001 элемент, а тут все 100000
        my_dict.pop(i)
    return my_dict


# работа с list
fucn_list_append(my_list, num_oper)
print('+' * 100)
fucn_list_insert(my_list, num_oper)
print('+' * 100)
change_list(my_list)
print('+' * 100)

# работа с dict
func_dict(my_dict, num_oper)
print('+' * 100)
change_dict(my_dict, num_oper)


"""
RESULT:

Время выполнения функции: fucn_list_append - 0.008036375045776367
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Время выполнения функции: fucn_list_insert - 7.445335865020752
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Время выполнения функции: change_list - 0.03124237060546875
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Время выполнения функции: func_dict - 0.015622377395629883
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Время выполнения функции: change_dict - 0.015622138977050781


ВЫВОД: Добавление элементов что в list, что в dict по времени почти одинаково, но вот изменение list и dict сильно
        отличается по времени, а именно, например для list отобрал только 1001 элемент, в то время как для dict 
        отобрал все 100000 элементов и всё равно редактирование dict отработало быстрее.
        Поэтому по общим показателям с dict работать быстрее.
"""
