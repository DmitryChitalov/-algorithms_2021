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

    Сложность: O(len(...))+O(1) = O(n) - линейная
    """
    lst_to_set = set(lst_obj)  # O(len(...)) - линейная
    return lst_to_set          # O(1) - константная


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: O(n)*O(n)+O(1)+O(1) = O(n^2).
    """
    for j in range(len(lst_obj)):          # O(n) - линейная
        if lst_obj[j] in lst_obj[j+1:]:    # O(n) - линейная
            return False                   # O(1) - константная
    return True                            # O(1) - константная


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: O(n)+O(n log n)+O(n)+O(n)*O(1)+O(1) =
               O(n + n log n + n + O(n*1) + 1) = O(3n + n log n + 1) = O(n log n)  - линейно-логарифмическая
    """
    lst_copy = list(lst_obj)                 # O(n) - линейная
    lst_copy.sort()                          # O(n log n) - линейно-логарифмическая
    for i in range(len(lst_obj) - 1):        # O(n) - линейная
        if lst_copy[i] == lst_copy[i+1]:     # O(n) - линейная
            return False                     # O(1) - константная
    return True                              # O(1) - константная

#############################################################################################


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
