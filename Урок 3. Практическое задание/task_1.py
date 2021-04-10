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

Выводы.
1. Списки быстрее создаются и оперции выполняемые с известными индексами выполняются быстрее чем в словарях,
   операции требующие поиск значения в вловаре выполняются медленно
2. Словари медленне создаются, операция получения значения по ключу медленне чем в словаре по индексу,
   операции поиска выполняются несравнимо быстрееы
"""

import time


def do_test_list(n):
    test_list = []
    result_list = []
    start_val = time.time()
    for a in range(n):
        test_list.append(a)
    end_val = time.time()
    result_list.append(end_val - start_val)

    start_val = time.time()
    for a in range(n):
        test_val = test_list[a]
    end_val = time.time()
    result_list.append(end_val - start_val)

    test_val = -1
    start_val = time.time()
    if test_val in test_list:
        pass
    end_val = time.time()
    result_list.append(end_val - start_val)

    start_val = time.time()
    for a in range(n):
        test_list.pop()
    end_val = time.time()
    result_list.append(end_val - start_val)

    for a in range(n):
        test_list.append(a)
    start_val = time.time()
    for a in range(n):
        test_list.remove(a)
    end_val = time.time()
    result_list.append(end_val - start_val)

    return test_list, result_list


def do_test_dict(n):
    test_dict = {}
    result_list = []
    start_val = time.time()
    for a in range(n):
        test_dict[a] = a
    end_val = time.time()
    result_list.append(end_val - start_val)

    start_val = time.time()
    for a in range(n):
        test_val = test_dict[a]
    end_val = time.time()
    result_list.append(end_val - start_val)

    test_val = -1
    start_val = time.time()
    test_dict.get(test_val)
    end_val = time.time()
    result_list.append(end_val - start_val)

    start_val = time.time()
    for a in range(n):
        test_dict.pop(a)
    end_val = time.time()
    result_list.append(end_val - start_val)

    return test_dict, result_list


x = 100000
print('Операции с списками')
print('Операции:   создание, чтение, поиск, удаление по индексу, удаление по значению соответственно заняли')
for i in range(5):
    print(f'Операции заняли {do_test_list(x)[1:]} сек')

print('Операции с словорями')
print('Операции: создание, чтение, поиск, удаление по значению соответственно заняли')
for i in range(5):
    print(f'Операция заняла {do_test_dict(x)[1:]} сек')
