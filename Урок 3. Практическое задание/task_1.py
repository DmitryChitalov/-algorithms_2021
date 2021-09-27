"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from random import randrange
from pprint import pprint
from time import time
from numpy import average, mean


def func_timer(n: int = 1):
    """
    Декоратор, измеряющий время выполнения функции. При выполнении больше одного замера функции, выполняющей операции
    над итерируемым объектом, операция будет выполнена то же количество раз, что количество замеров.
    TODO: Подумать, можно ли как-то не влиять количеством замеров на результат работы функции
    :param n: количество замеров, по умолчанию 1
    :return: None
    """
    def func_decorator(func):

        def wrapper(*args, **kwargs):
            durations = []
            result = None
            try:
                start = time()
                for i in range(n):
                    # start = time()
                    result = func(*args, **kwargs)
                    # stop = time()
                    # durations.append(stop - start)
                stop = time()
                print(f"Duration of {n} operations for {func} function: {stop - start} sec")
            except IndexError as ex:
                print("Looks like you tried to make too many measures for an iterable, which has no enough elements")
                pprint(ex.args)

            # print(f"Weighted average execution time of the {func} function is {average(durations)}")
            # print(f"Arithmetic mean execution time of the {func} function is {mean(durations)}")
            return result
        return wrapper
    return func_decorator


@func_timer(1000)
def fill_list(size: int) -> list:
    return [i * 10 for i in range(size)]        # O(n)


@func_timer(1000)
def fill_dict(size: int) -> dict:
    return {i: i * 10 for i in range(size)}     # O(n)


@func_timer(100000)
def list_append(lst: list):
    element = len(lst)                      # O(1)
    lst.append(element * 10)                # O(1)
    lst.append((element + 1) * 10)          # O(1)


@func_timer(10000)
def list_popi(lst: list):
    # i = randrange(len(lst))    # O(1)
    res = lst.pop()  # O(1)
    return res


@func_timer(100000)
def list_get(lst: list):
    # i = randrange(len(lst))   # O(1)
    return lst[1000]     # O(1)


@func_timer(100000)
def dict_append(dct: dict):
    element = len(dct)                     # O(1)
    dct[element] = element * 10            # O(1)
    dct[element + 1] = (element + 1) * 10  # O(1)


@func_timer(10000)
def dict_popi(dct: dict):
    # Проблема с расхождением теории с практикой в этой строке.
    # Проблема в том, что я создаю список для выбора случайного ключа
    # key = list(dct.keys())[randrange(len(dct.keys()))]  # O(n)
    return dct.popitem()                                # O(1)


@func_timer(100000)
def dict_get(dct: dict):
    # Проблема с расхождением теории с практикой в этой строке.
    # Проблема в том, что я создаю список для выбора случайного ключа
    # key = list(dct.keys())[randrange(len(dct.keys()))]    # O(n)
    # key = randrange(iter(dct))
    return dct.get(1000)                                   # O(1)


if __name__ == '__main__':
    lst = fill_list(100000)
    # Weighted average execution time of the<function fill_list at 0x000002B1040854C0> function is 4.669475555419922e-05
    # Arithmetic mean execution time of the <function fill_list at 0x000002B1040854C0> function is 4.669475555419922e-05

    dct = fill_dict(100000)
    # Weighted average execution time of the<function fill_dict at 0x000002B11449F310> function is 0.0001225006580352783
    # Arithmetic mean execution time of the <function fill_dict at 0x000002B11449F310> function is 0.0001225006580352783

    # ##############
    # Список заполняется быстрее почти в 2 раза при достаточно большом количестве элементов, хотя сложность алгоритма
    # одинакова в обоих случаях. Думаю, это связано с тем, что в словаре каждый раз при добавлении элемента вычисляется
    # хеш для ключа.
    # ##############

    list_append(lst)
    # Weighted average execution time of the <function list_append at 0x000001B33DF8DA60> function is 0.0
    # Arithmetic mean execution time of the <function list_append at 0x000001B33DF8DA60> function is 0.0

    dict_append(dct)
    # Weighted average exec-n time of the<function dict_append at 0x000001DFCB55BE50> function is 1.5640974044799803e-05
    # Arithmetic mean exec-n time of the <function dict_append at 0x000001DFCB55BE50> function is 1.5640974044799803e-05

    # ###############
    # Вопреки ожиданиям и здесь список оказывается быстрее.
    # ###############

    list_popi(lst)
    # Weighted average execution time of the <function list_popi at 0x000001DFCB55BC10> function is 0.0
    # Arithmetic mean execution time of the <function list_popi at 0x000001DFCB55BC10> function is 0.0

    dict_popi(dct)
    # Weighted average execution time of the<function dict_popi at 0x000001DFCB55BF70> function is 3.748607635498047e-05
    # Arithmetic mean execution time of the <function dict_popi at 0x000001DFCB55BF70> function is 3.748607635498047e-05

    # ###############
    # Снова список оказывается быстрее.
    # ###############

    list_get(lst)
    # Weighted average execution time of the <function list_get at 0x000001DFCB55BD30> function is 0.0
    # Arithmetic mean execution time of the <function list_get at 0x000001DFCB55BD30> function is 0.0

    dict_get(dct)
    # Weighted average execution time of the <function dict_get at 0x000001DFCB5620D0> function is 3.125e-05
    # Arithmetic mean execution time of the <function dict_get at 0x000001DFCB5620D0> function is 3.125e-05

    # ###############
    # И даже получить элемент списка получилось быстрее.
    # ###############

    """
    Общий вывод: согласно полученным данным, получается, что список, пусть незначительно, но всё же быстрее словаря 
    во всех операциях. Хотя изначально это не кажется очевидным, но ожидаемым при создании структур. Можно предположить,
    что по каким-то причинам именно на списке замер не работает, но это как-то натянуто. Тот же результат получен и при 
    измерении времени n выполнений каждой функции. Теория ошибается? Вряд ли. Вот только объяснить результат не могу ((
    
    Duration of 1000 operations for <function fill_list at 0x000001E378E99820> function: 0.06077766418457031 sec
    Duration of 1000 operations for <function fill_dict at 0x000001E378E99940> function: 0.10306930541992188 sec
    Duration of 1000 operations for <function list_append at 0x000001E378E99A60> function: 0.0 sec
    Duration of 1000 operations for <function dict_append at 0x000001E378E99DC0> function: 0.0 sec
    Duration of 1000 operations for <function list_popi at 0x000001E378E99B80> function: 0.010024309158325195 sec
    Duration of 1000 operations for <function dict_popi at 0x000001E378E99EE0> function: 0.0156705379486084 sec
    Duration of 1000 operations for <function list_get at 0x000001E378E99CA0> function: 0.0 sec
    Duration of 1000 operations for <function dict_get at 0x000001E378E9F040> function: 0.031230449676513672 sec   
    
    
    ===== Данные после исправления кода ======
    Duration of 1000 operations for <function fill_list at 0x0000021804A99820> function: 3.904294729232788 sec
    Duration of 1000 operations for <function fill_dict at 0x0000021804A99940> function: 10.729747772216797 sec
    Duration of 100000 operations for <function list_append at 0x0000021804A99A60> function: 0.030739307403564453 sec
    Duration of 100000 operations for <function dict_append at 0x0000021804A99DC0> function: 0.028804302215576172 sec
    Duration of 10000 operations for <function list_popi at 0x0000021804A99B80> function: 0.0023076534271240234 sec
    Duration of 10000 operations for <function dict_popi at 0x0000021804A99EE0> function: 0.0 sec
    Duration of 100000 operations for <function list_get at 0x0000021804A99CA0> function: 0.010366201400756836 sec
    Duration of 100000 operations for <function dict_get at 0x0000021804A9F040> function: 0.010378599166870117 sec
    
    Здесь мы уже видим, что словарь либо сопоставим со списком по скорости выполнения операций (кроме создания), 
    либо немного или даже заметно быстрее списка, как, например, при добавлении элемента или в операции pop, где список
    выполнил операцию так быстро, что нам не хватило разрешения используемого таймера на выбранном количестве повторений
    """
