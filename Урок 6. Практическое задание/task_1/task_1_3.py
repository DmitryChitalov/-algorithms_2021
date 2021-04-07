"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

'''
Третий скрипт:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
'''

import memory_profiler
import time
from pympler import asizeof
from numpy import array  # !!!
from recordclass import recordclass

import csv
import json
from random import randint


#############################################################################################
def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, t2-t1
    return wrapper

#############################################################################################
def fill_company_in_json_file(file_name = 'company.json'):  # запишем в JSON-файл словарь компаний с прибылями
    with open('company.csv') as f:
        reader = csv.reader(f)
        my_set = set([row[0] for row in reader])               # Заполним список наименований организаций
        for i in range(5):                                     # Увеличим это количество в ... раз
            # print([el+'_'+str(i) for el in my_set])
            my_set = my_set.union([el+'_'+str(i) for el in my_set])
        # print(my_set)

    my_dict = {x: randint(1, 100000000) for x in my_set}
    # print(my_dict)
    with open(file_name, 'w', encoding='utf-8') as f_json:
        json.dump(my_dict, f_json, ensure_ascii=True, indent=4)     #!!!! добавить для криллицы ensure_ascii=True

def get_from_file(file_name = 'company.json'):                      # возвращает DICT/RecordClass, из JSON-файла
    with open(file_name, encoding='utf-8') as f_json:
        dict = json.load(f_json)
        # dumped_dict = json.dumps(dict, ensure_ascii=True, indent=4)
        dumped_dict = json.dumps(dict, ensure_ascii=False, indent=4)
        a = recordclass('cls', ('company', 'profit'))
        list_rec_cls = [a(el,dict[el]) for el in dict]
        array_name = array([el for el in dict])
        array_profit = array([el for el in dict.values()])
        print(f'Расчет размера памяти, требуемой для хранения информации по {len(dict)} компаниям с их прибылями:')
        print('Размер Dict: ', asizeof.asizeof(dict))
        print('Размер json: ', asizeof.asizeof(dumped_dict))
        print('Размер list recordclass: ', asizeof.asizeof(list_rec_cls))
        print('Размер array из numPy: ', asizeof.asizeof(array_name) + asizeof.asizeof(array_profit))
    return dict, list_rec_cls

#############################################################################################
@decor
def get_company_with_max_profit_1(dict, amount):
    my_list = sorted(dict.items(),  key=lambda x: x[1], reverse=1)  # !!! O(n LOG n)
    return my_list[0:amount]                                        # !!! O(n)

#############################################################################################
@decor
def get_company_with_max_profit_2(dict, amount):
    my_list = []                        # !!! O(1)
    for key, value in dict.items():     # !!! O(n)
        my_list.append((value, key))    # !!! O(1)
    my_list.sort(reverse=1)             # !!! O(n LOG n)
    return my_list[0:amount]            # !!! O(n)

#############################################################################################
@decor
def get_company_with_max_profit_3(dict, amount):
    my_list = []                            # !!! O(1)
    for i in range(amount):                 # !!! O(1)
        max_company = ''                    # !!! O(1)
        max_value = 0                       # !!! O(1)
        for key, value in dict.items():     # !!! O(n)
            if max_value < value:           # !!! O(1)
                max_value = value           # !!! O(1)
                max_company = key           # !!! O(1)
        my_list.append((max_company, max_value))    # !!! O(1)
        dict[max_company] = 0               # !!! O(1)
    return my_list                          # !!! O(1)

#############################################################################################
@decor
def get_company_with_max_profit_3_3(obj, amount):
    my_list = []                            # !!! O(1)
    for i in range(amount):                 # !!! O(1)
        max_company = ''                    # !!! O(1)
        max_value = 0                       # !!! O(1)
        i = 0                               # !!! O(1)
        for el in obj:                      # !!! O(n)
            if max_value < el.profit:       # !!! O(1)
                max_value = el.profit       # !!! O(1)
                max_company = el.company    # !!! O(1)
                pos = i
            i += 1
        my_list.append((max_company, max_value))    # !!! O(1)
        obj.pop(pos)
    return my_list                          # !!! O(1)

#############################################################################################

file_name = 'company.json'
amount_find_company = 3

# fill_company_in_json_file(file_name)
dict, list_rec_cls = get_from_file(file_name)

# res, mem_diff, time_diff = get_company_with_max_profit_1(dict, 3)
# print(f"Результат поиска {amount_find_company} компаний с максимальной прибылью:\n{res}\n")
# print(f"Выполнение первого варианта заняло {mem_diff} Mib, {time_diff} времени.")
# res, mem_diff, time_diff = get_company_with_max_profit_2(dict, 3)
# print(f"Выполнение второго варианта заняло {mem_diff} Mib, {time_diff} времени.")
# res, mem_diff, time_diff = get_company_with_max_profit_3(dict, 3)
# print(f"Выполнение третьего варианта заняло {mem_diff} Mib, {time_diff} времени.")
res, mem_diff, time_diff = get_company_with_max_profit_3_3(list_rec_cls, 3)
print(f"Выполнение третьего (модифицированного) варианта заняло {mem_diff} Mib, {time_diff} времени.")


'''
Для оптимизацции памяти, действительно неплохо выглядит вариант с JSON-сериализации (4 793 496) против DICT (11 654 208).
Но, recordClass (3 375 888) - менее затратный. 
В принципе, можно было "подумать", как оптимизировать array от numPy для более компактного размещения 
или воспользоваться Cython для оптимизации по памяти и скорости обработки...
Чтобы показания занимаемой памяти были "верными", пришлось запускать каждый алгоритм "отдельно первым".
Третий алгоритм модифицировал на обработку RecordClass. Немного проиграл по времени, но память осталась на прежнем уровне.
Стоит учесть, что алгоритмы не "учитывают" различия в памяти на обрабатываемые последовательности.
Для более точных замеров, желательно их произвести в изолированных экземплярах, предварительно удалив из каждого 
"ненужные" остатки от др. вариантов (del dict,...)
Но, учитывая достаточно существенные различия в системах хранения обрабатываемых объектов, этого не требуется.

Аналитика:
Расчет размера памяти, требуемой для хранения информации по 70304 компаниям с их прибылями:
Размер Dict:  11654208
Размер json:  4793496
Размер list recordclass:  3375888
Размер array из numPy:  23622368
Выполнение первого варианта заняло 3.9765625 Mib, 0.0680532455444336 времени.
Выполнение второго варианта заняло 4.38671875 Mib, 0.13308501243591309 времени.
Выполнение третьего варианта заняло 0.00390625 Mib, 0.016954660415649414 времени.
Выполнение третьего (модифицированного) варианта заняло 0.00390625 Mib, 0.028960704803466797 времени.
'''