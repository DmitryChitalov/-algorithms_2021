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
from random import randrange

def gen_list(num_el):
    return [c * 3 for c in range(num_el)]


def gen_dict(num_el):
    return {c: c * 3 for c in range(num_el)}

def dict_key(dict):
    for i in range(len(dict)):
        if i == 5678:
            k = dict[i]
    return 0

def list_ind(lst):
    for i in range(len(lst)):
        if i == 5678:
            k = lst[i]
    return 0

def dict_value(dict):
    for i in dict.values():
        if i == 17034:
            k = i
    return 0

def list_value(lst):
    for i in lst:
        if i == 17034:
            k = i
    return 0



num_el = 100000
t1 = time()
#print(gen_list(num_el))
test_list = gen_list(num_el)
t2 = time()
#print(gen_dict(num_el))
test_dict = gen_dict(num_el)
t3 = time()
print("Время генерации списка", t2 - t1)
print("Время генерации словаря", t3 - t2)
print("Разница", (t3 - t2) - (t2 - t1))
print("Словарь заполняется медленнее, т.к. для ключей требуется посчитать хэш")
print("-----------------------------------------------------------------------")

t1 = time()
list_ind(test_list)
t2 = time()
dict_key(test_dict)
t3 = time()

print("Время поиска элементов списка", t2 - t1)
print("Время поиска элементов словаря", t3 - t2)
print("Разница", (t3 - t2) - (t2 - t1))
print("На моём примере однозначно не понятно что быстрее поиск по ключу в словаре или поиск в списке по индексу, "
      "т.к. иногда разница получается положительной, иногда отрицательной. Чаще отрицательной.")
print("-----------------------------------------------------------------------")

t1 = time()
list_value(test_list)
t2 = time()
dict_value(test_dict)
t3 = time()

print("Время поиска значений элементов списка", t2 - t1)
print("Время поиска значений элементов словаря", t3 - t2)
print("Разница", (t3 - t2) - (t2 - t1))
print("Поиск значению в словаре происходит дольше")



