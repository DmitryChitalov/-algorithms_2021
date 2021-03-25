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
from time import time

def time_dec(func):
    def time_dec_in(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        return f"Затраченное время {t2 - t1}"
    return time_dec_in

list1 =[]
dict1 = {}
@time_dec
def fill_dict(dict1):
    for i, k in zip(range(10000000), range(10000000)):
        dict1[i] = k
    return dict1

@time_dec
def fill_list(list1 = []):
    for i in range(10000000):
        list1.append(i)
    return list1

@time_dec
def del_dict(dict1):
    for i in range(1000):
        dict1.pop(i)


@time_dec
def del_list(list1):
    for i in range(1000):
        list1.pop(i)


print(fill_dict(dict1))#1.6 ~ сильно не отличается от наполнения списка
print(fill_list(list1))#1.1 ~
print(del_dict(dict1))# 0.0 ~ удаление у словаря гораздо быстрее, так как поиск элемента идет по хэшу
print(del_list(list1))# 11. ~ гораздо медленее, так как идет проход по списку




