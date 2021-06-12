
"""
Задание 1.
Для каждой из трех задач выполнить следующее:
1) для каждого выражения вместо !!! укажите сложность этого выражения.
2) определите сложность задачи в целом.
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 3:
    Создать множество из списка
    Сложность: n + 1.  (O(n)) - сложность операции
    """
    lst_to_set = set(lst_obj)  #  len(len(lst_obj)) = n
    return lst_to_set  # 1


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: n*1 + n**2 + 1 + 1  =  2n + 2.  (O(n))
    """
    for j in range(len(lst_obj)):          # n*1
        if lst_obj[j] in lst_obj[j+1:]:    # n**2
            return False                   # 1
    return True                            # 1


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: len(lst_obj) + n*log(n) + n*1 + n + 1 + 1  =  n*log(n) + 2n + 2 + len(lst_obj).  (O(n*log(n)))
    """
    lst_copy = list(lst_obj)                 # len(lst_obj) = n
    lst_copy.sort()                          # n*log(n)
    for i in range(len(lst_obj) - 1):        # n*1
        if lst_copy[i] == lst_copy[i+1]:     # 1
            return False                     # 1
    return True                              # 1

#############################################################################################
