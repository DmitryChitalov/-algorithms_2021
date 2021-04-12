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
import time

def fun_list(n):
    start_val = time.time()
    res = []
    for i in range(n):
        res.append(i)
    end_val = time.time()
    return res, end_val - start_val


def fun_dict(n):
    start_val = time.time()
    res = {}
    for i in range(n):
        res[i] = f'number {i}'
    end_val = time.time()
    return  res, end_val - start_val

print(fun_list(1000))
print(fun_dict(1000))
"""
заполнение словаря происходит дольше

"""

def fun_list_1(n):
    res = []
    for i in range(n):
        res.append(i)
    return res

def fun_dict_1(n):
    res = {}
    for i in range(n):
        res[i] = f'number {i}'
    return  res


a = fun_dict_1(1000)
b = fun_list_1(1000)


def list_index(b):
    start_val = time.time()
    for i in range(len(b)):
        if i ==5:
            print(b[i])
    end_val = time.time()
    return b[i], end_val - start_val

def dict_key(a):
    start_val = time.time()
    for i in range(len(b)):
        if i ==5:
            print(b[i])
    print(a[5])
    end_val = time.time()
    return  end_val - start_val



print(list_index(b))
print(dict_key(a))

"""
Поиск по индексу показал одинаковое время
"""