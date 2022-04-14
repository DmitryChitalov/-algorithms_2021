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
from random import randint


# Первый вариант (O(n^2))


def min_in_list(lst):
    for i in lst:                # O(n)
        is_min = True            # O(1)
        for j in lst:            # O(n)
            if i > j:            # O(1)
                is_min = False   # O(1)
        if is_min:               # O(1)
            return i             # O(1)


# Второй вариант (O(n))


def my_min(n):
    min_num = n[0]               # О(1)
    for i in range(len(n)):      # O(n)
        if min_num > n[i]:       # O(1)
            min_num = n[i]       # O(1)
    return min_num               # O(1)


lst = [randint(0, 100) for i in range(50)]
print(min_in_list(lst))
print(my_min(lst))
