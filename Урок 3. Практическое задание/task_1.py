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


def time_decorator(func):
    """ Функция декоратор времени выполнения программы"""
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print (f'Время выполнения функции {func.__name__}'
               f' составило {end - start} ')
        return result
    return timer


@time_decorator
def fill_list_append(lst, num):
    """ Заполнение списка """
    for i in range(num):
        lst.append(i)


@time_decorator
def fill_list_insert(lst, num):
    """ Заполнение списка insert-ом """
    for i in range(num):
        lst.insert(0, i) # Сложность операции O(n)


@time_decorator
def fill_dict(dct, num):
    """ Функция заполнения словаря"""
    for i in range(num):
        dct[i] = i


@time_decorator
def pop_list(lst, num):
    """ Удаление элементов списка """
    for i in range(num // 2):
        lst.pop(i)


@time_decorator
def change_list(lst, num):
    """ Изменение списка """
    for i in range(num // 3):
        lst[i] = lst[i+1]


@time_decorator
def pop_dict(dct, num):
    """ Удаление элементов словаря """
    for i in range(num // 2):
        dct.pop(i)

@time_decorator
def change_dict(dct, num):
    """ Изменение элементов словаря """
    for i in range(num // 3):
        dct[i] = 'test'


if __name__ == '__main__':
    some_list = []
    some_dict = {}
    N_CONST = 10 ** 5
    fill_list_append (some_list, N_CONST)  # Сложность операции O(1)
    print ('_' * 100)
    fill_list_insert (some_list, N_CONST)  # Сложность операции O(n)
    print ('_' * 100)
    fill_dict (some_dict, N_CONST)  # Сложность операции O(1)
    print ('_' * 100)
    print ('_' * 100)
    pop_list(some_list, N_CONST)  # Сложность операции O(n)
    print ('_' * 100)
    change_list(some_list, N_CONST)  # Сложность операции O(1)
    print ('_' * 100)
    pop_dict(some_dict, N_CONST)
    print ('_' * 100)
    change_dict(some_dict, N_CONST)
    print ('_' * 100)


'''
Время выполнения функции fill_list_append составило 0.007978439331054688 
____________________________________________________________________________________________________
Время выполнения функции fill_list_insert составило 5.14766263961792 
____________________________________________________________________________________________________
Время выполнения функции fill_dict составило 0.0069539546966552734 
____________________________________________________________________________________________________
____________________________________________________________________________________________________
Время выполнения функции pop_list составило 1.4222187995910645 
____________________________________________________________________________________________________
Время выполнения функции change_list составило 0.000997304916381836 
____________________________________________________________________________________________________
Время выполнения функции pop_dict составило 0.003988981246948242 
____________________________________________________________________________________________________
Время выполнения функции change_dict составило 0.000997781753540039 
____________________________________________________________________________________________________
'''

'''
import random
import time


def decoration(func):
    def decocarate(var_number_in, number_operation, var_list):
        start = time.time ()
        obj_func = func (var_number_in, number_operation, var_list)
        stop = time.time ()
        result = (stop - start) * 1000
        print (f'Дельта по времени *1000 составляет для кол-ва элементов {var_number_in} для '
               f'{func}: {result}')
        return obj_func

    return decocarate


@decoration
def work_list(var_number_bg=0, number_operation=0, var_list=None):
    if var_list is None:
        var_list = []
    if number_operation == 0:
        var_list = [number for number in range (var_number_bg)]
        return var_list
    elif number_operation == 1:
        if var_number_bg < 0:
            return var_list
        var_list.append (var_number_bg)
        var_number_bg -=10
        return work_list (var_number_bg - 10, 1, var_list)


@decoration
def work_dict(var_number_dct=0, number_operation=0, var_dict=None):
    if var_dict is None:
        var_dict = {}
    if number_operation == 0:
        var_dict = {number: number ** 2 + 1 for number in range (var_number_dct)}
        return var_dict
    elif number_operation == 1:
        if var_number_dct < 0:
            return var_dict
        var_dict.update(var_number_dct = var_number_dct ** 2 + 1)
        var_number_dct -=10
        return work_dict (var_number_dct - 10, 1, var_dict)


if __name__ == '__main__':
    var_number = random.randint (0, 100000)
    my_list = work_list (var_number, 0, None)
    my_dict = work_dict (var_number, 0, None)
    my_list = work_list (1000, 1, my_list)
    my_dict = work_dict (1000, 1, my_dict)
    '''
"""
Заполнение списка занимает примерно в 10 раз меньше времени
но при добавлении элементов время примерно одинаково если
делать рекурсией, правда я не облегчал рекурсию мемозиацией,
функция была универсальной
"""
