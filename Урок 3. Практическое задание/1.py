import time

variable_to_function = 2 ** 21
storage_dct = {}
storage_lst = []


def my_decorator(function_to_decorate):
    def time_calculation(*args, **kwargs):
        start_time = time.time()
        result = function_to_decorate(*args, **kwargs)
        end_time = time.time()
        print(f'* Время выполнения функции {function_to_decorate.__name__} составляет: '
              f'{end_time - start_time} секунд.' + " ")
        return result

    return time_calculation


@my_decorator
def dct_func_1(variable, dct):
    for values in range(variable):
        lst_key = 'may_' + '' + str(values + 1)
        dct[lst_key] = values
        # сложность этой функции будет O(n)


dct_func_1(variable_to_function, storage_dct)


@my_decorator
def lst_func_1(variable, lst):
    for lst_values in range(variable):
        lst_key = 'may_' + '' + str(lst_values + 1)
        lst.append(lst_key)
        # сложность этой функции будет O(n)


lst_func_1(variable_to_function, storage_lst)
print('---' * 80)
# * Время выполнения функции dct_func_1 составляет: 1.2494471073150635 секунд.
# * Время выполнения функции lst_func_1 составляет: 0.7525467872619629 секунд.


execution_speed_dct_1 = 1.2494471073150635
execution_speed_lst_1 = 0.7525467872619629

if execution_speed_dct_1 > execution_speed_lst_1:
    res = execution_speed_dct_1 - execution_speed_lst_1
    print(f'Выполнение функции lst_func_1 происходит быстрее чем выполнение функции dct_func_1 на {res} секунд')
else:
    res = execution_speed_lst_1 - execution_speed_dct_1
    print(f'Выполнение функции dct_func_1 происходит быстрее чем выполнение функции lst_func_1 на {res} секунд')
print('---' * 80)
"""
Вывод:
    Выполнение функции lst_func_1 происходит быстрее чем выполнение функции dct_func_1 на 0.4969003200531006 секунд,
    т.к. в моем случае функция выполняет каждое ключ значение через цикл в хеш-таблице
"""


@my_decorator
def lst_func_2(data_counting):
    data_counting.count(100000)
    for sfg in range(len(data_counting)):
        do_not_use = data_counting[sfg]
        # сложность этой функции будет O(n)


lst_func_2(storage_lst)


@my_decorator
def dct_func_2(using_dict):
    for key_bulkhead in using_dict:
        do_not_use_1 = key_bulkhead
    for values_bulkhead in using_dict:
        do_not_use_2 = using_dict[values_bulkhead]
    for xs in using_dict.values():
        do_not_use_3 = xs
    for key, values in using_dict.items():
        do_not_use_4 = f'{key}:{values}'
        # сложность этой функции будет O(n)


dct_func_2(storage_dct)
print('---' * 80)
# * Время выполнения функции lst_func_2 составляет: 0.10756087303161621 секунд.
# * Время выполнения функции dct_func_2 составляет: 0.815767765045166 секунд.

execution_speed_dct_2 = 0.815767765045166
execution_speed_lst_2 = 0.10756087303161621

if execution_speed_dct_2 > execution_speed_lst_2:
    res_2 = execution_speed_dct_2 - execution_speed_lst_2
    print(f'Выполнение функции lst_func_2 происходит быстрее чем выполнение функции dct_func_2 на {res_2} секунд')
else:
    res_2 = execution_speed_lst_2 - execution_speed_dct_2
    print(f'Выполнение функции dct_func_2 происходит быстрее чем выполнение функции lst_func_2 на {res_2} секунд')
"""
Вывод:
    Выполнение функции lst_func_2 происходит быстрее чем выполнение функции dct_func_2 на 0.7082068920135498 секунд,
    и здесь функия со списком будет быстрее, так как для вывода информации списка требуется немного меньше времени
    чем ключ-значения из словаря
"""
