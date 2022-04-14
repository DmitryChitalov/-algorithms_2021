"""
Задание 1.

Для каждой из трех функций выполнить следующее:

1) для каждого выражения вместо !!! укажите сложность этого выражения.
2) определите сложность каждой функции в целом.

Сложность нужно определять только там, где указаны символы !!!

Примечание:
Прошу вас внимательно читать ТЗ и не выполнять все пункты.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: O(1)
    """
    lst_to_set = set(lst_obj)  # O(1)
    return lst_to_set  # O(1)


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: O(N^2).
    """
    for j in range(len(lst_obj)):          # O(N)
        if lst_obj[j] in lst_obj[j+1:]:    # T(N) = 2*(1+2+...+(N-1)) = 2*1/2*N = O(N)
            return False                   # O(1)
    return True                            # O(1)


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: N*logN
    """
    lst_copy = list(lst_obj)                 # O(N)
    lst_copy.sort()                          # O(N*logN)
    for i in range(len(lst_obj) - 1):        # O(N)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

#Не совсем поняла вопрос: в О-нотации сложность алгоритма не зависит от входных данных (это же оценка сверху, худший случай). Или нет?
#Или здесь сложность не в О-нотации нужно оценивать?
#Я просто переписала свои ответы сверху.
print(check_1(lst)) #O(1)
print(check_2(lst)) #O(N^2)
print(check_3(lst)) #O(N*logN)
