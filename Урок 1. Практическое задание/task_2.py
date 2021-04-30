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

my_list = [random.randint(20, 100) for i in range(10)]

# Первый алгоритм
def find_min_1(lstobj: list[int]) -> int:
    """Function finds the minimum value of list objects.

    It takes list object on enter and return integer.
    The complication of function is equal O(N^2).
    """

    min_value = lstobj[0]
    for el in lstobj:
        if el < min_value:
            min_value = el
    return min_value


# Второй алгоритм
def find_min_2(lstobj: list[int]) -> int:
    """Function finds the minimum value of list objects.

    It takes list object on enter and return integer.
    The complication of function is equal O(N).
    """

    return min(lstobj)

print(find_min_1(my_list))
print(find_min_2(my_list))

