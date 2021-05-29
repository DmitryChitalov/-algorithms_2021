"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import random

def check_1(lst_obj):
    lst_to_set = set(lst_obj)
    return lst_to_set

def compare(lst):
    mins = lst[0]
    for i in lst:
        if i < mins:
            mins = i
    return mins

def compare_1(lst_obj):
    lst_copy = list(lst_obj)
    lst_copy.sort()
    return lst_copy[0]

def compare_2(lst):
    for i in range(0, len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] >= lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst[i + 1]

def compare_3(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                [j + 1], lst[j]
    return lst[j - 1]

def compare_4(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(0, j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst[j - 1]



for j in (0, 20):
    lst = random.sample(range(0, 1000), j)

print(check_1(lst))
print(compare(lst))
print(compare_1(lst))
print(compare_2(lst))
print(compare_3(lst))
print(compare_4(lst))


