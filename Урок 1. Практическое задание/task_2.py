"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random

# O(n^2)


def find_min_el_1(lst):
    for i in lst:
        status_min = True
        for j in lst:
            if i > j:
                status_min = False
        if status_min:
            return i


# O(n)


def find_min_el_2(lst):
    return min(lst)


lst_obj = random.sample(range(-100000, 100000), 10)
print(lst_obj)
print()
print(find_min_el_1(lst_obj))
print()
print(find_min_el_2(lst_obj))
