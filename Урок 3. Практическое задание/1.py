import time

storage_dct = {}
storage_lst = []
variable_to_function = 2 ** 21


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
# сложность этой функции будет O(1)
def dct_func_1(variable, dct):
    for value in range(variable):
        dct[value] = value


@my_decorator
# сложность этой функции будет O(n)
def lst_func_1(variable, lst):
    for lst_values in range(variable):
        lst.append(lst_values)


dct_func_1(variable_to_function, storage_dct)
lst_func_1(variable_to_function, storage_lst)
print('---' * 500)

# * Время выполнения функции dct_func_1 составляет: 0.310821533203125 секунд.
# * Время выполнения функции lst_func_1 составляет: 0.19988441467285156 секунд.


"""
Вывод:
    Функция со списком будет быстрее, т.к. у словаре время затрачивается еще на хеш вычисления.
"""


@my_decorator
def lst_func_2(data_counting):
    # сложность этой функции будет O(n)
    for i in range(1000):
        data_counting.pop(i)
    for l in range(1000):
        data_counting[l] = data_counting[l + 1]


@my_decorator
def dct_func_2(using_dict):
    # сложность этой функции будет O(1)
    for i in range(1000):
        using_dict.pop(i)
    for l in range(1000):
        using_dict[l] = l + 1


lst_func_2(storage_lst)
dct_func_2(storage_dct)

# * Время выполнения функции lst_func_2 составляет: 3.8467884063720703 секунд.
# * Время выполнения функции dct_func_2 составляет: 0.07495641708374023 секунд.

"""
Вывод:
     функции по удаления и иизменению:
        Лучший результат по выполнению будет у словаря, т.к. изменение и удаление имеют временную сложность O(1)
        константную, поэтому она самая быстрая по выполнению.
"""