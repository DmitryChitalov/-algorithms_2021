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

import random
import time

def fill_set(amount_el=1000):       # функция заполнения множества для последующей перегрузки в список и словарь
    my_set = set()
    while len(my_set) < amount_el:
#        my_set.add(random.randint(0, amount_el*100))
        my_set.add(str(random.randint(0, amount_el * 100)) + 'word')  # для чистоты эксперимента, значения будут строковыми
    return my_set

def timer_for_func(func):           # Декоратор для замера времени выполнения функции
   def timer(*args, **kwargs):
       start_val = time.time()
       result = func(*args, **kwargs)
       end_val = time.time()
       return result, end_val-start_val
   return timer

def timer_for_proc(func):           # Декоратор для замера выполнения процедуры
   def timer(*args, **kwargs):
       start_val = time.time()
       func(*args, **kwargs)
       end_val = time.time()
       return end_val-start_val
   return timer

@timer_for_func
def fill_list_or_dict(type_object, my_set):   # Функция заполнения списка и словаря значениями из множества
    if type_object == 'list':       # если передан список
        obj = []
        for el in my_set:
            obj.append(el)
    elif type_object == 'dict':     # если передан словарь
        obj = {}
        for el in my_set:
            obj[el] = 'simple_word'
    else:
        return None
    return obj

@timer_for_proc
def find_el_in_list_or_dict(obj, my_set):       # Процедура поиска в списке/словаре элементов передаваемого множества
    if str(type(obj)).find('list') != - 1:      # если передан список
        for el in my_set:
            get_el = obj.count(el)
    elif str(type(obj)).find('dict') != -1:     # если передан словарь
        for el in my_set:
            get_el = obj[el]

@timer_for_proc
def del_el_in_list_or_dict(obj, my_set):        # Процедура удаления в списке/словаре элементов передаваемого множества
    if str(type(obj)).find('list') != - 1:      # если передан список
        for el in my_set:
            obj.remove(el)
    elif str(type(obj)).find('dict') != -1:     # если передан словарь
        for el in my_set:
            obj.pop(el)


len_obj = 10000                # размерность списка и словаря
my_set = fill_set(len_obj)      # заполним эталонное множество

my_list, time_list = fill_list_or_dict('list', my_set)
my_dict, time_dict = fill_list_or_dict('dict', my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
# Заполнение 10000 элементов заняло для списка: 0.002002, для словаря: 0.004003 (199%)
print('Заполнение {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                            time_dict,
                                                                                            percent_dict_in_list))

time_list = find_el_in_list_or_dict(my_list, my_set)
time_dict = find_el_in_list_or_dict(my_dict, my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
# Поиск/чтение 10000 элементов заняло для списка: 4.880468, для словаря: 0.001001 (0%)
print('Поиск/чтение {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                              time_dict,
                                                                                              percent_dict_in_list))

time_list = del_el_in_list_or_dict(my_list, my_set)
time_dict = del_el_in_list_or_dict(my_dict, my_set)
percent_dict_in_list = int(time_dict / time_list * 100)
# Удаление 10000 элементов заняло для списка: 0.025022, для словаря: 0.002999 (11%)
print('Удаление {} элементов заняло для списка: {:.6f}, для словаря: {:.6f} ({}%)'.format(len_obj, time_list,
                                                                                              time_dict,
                                                                                              percent_dict_in_list))
'''
Общий вывод:
            При заполнении словаря и списка идентичными значениями (ключ словаря == значение списка),
            как правило, наблоюдается выигрыш по времени у списка.
            Это обусловлено отсутствием необходимости строить ключи.
            При последующей работе со словарем и списком (поиск/удаление элемента),
            список явно "проигрывает" словарю, даже с использованием встроенных функций.
            Естественно, это подтверждает гипотезу о "полезности" ключей. 
'''
