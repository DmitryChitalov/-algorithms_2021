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

    Сложность: О(n).
    """
    lst_to_set = set(lst_obj)  # О(n)
    return lst_to_set          # О(1)


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: О(n**2).
    """
    for j in range(len(lst_obj)):          # О(n)
        if lst_obj[j] in lst_obj[j+1:]:    # О(n)
            return False                   # О(1)
    return True                            # О(1)


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: О(n log n)
    """
    lst_copy = list(lst_obj)                 # О(n)
    lst_copy.sort()                          # О(n log n)
    for i in range(len(lst_obj) - 1):        # О(n)
        if lst_copy[i] == lst_copy[i+1]:     # О(1)
            return False                     # О(1)
    return True                              # О(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
