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

Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""

import random


def find_max_1(lst):
    """
    Сложность: O(N^2).
    """
    min_item = None
    for item1 in range(len(lst)):
        min_item = lst[item1]
        for item2 in range(len(lst)):
            if lst[item2] < min_item:
                min_item = lst[item2]
    return min_item


def find_max_2(lst, my_max):
    """
    Сложность: O(N).
    """
    min_item = my_max
    for item in lst:
        if item < min_item:
            min_item = item
    return min_item


MAX_VALUE = 100000
random_lst = random.sample(range(-MAX_VALUE, MAX_VALUE), 10)
print(random_lst)
print(find_max_1(random_lst))
print(find_max_2(random_lst, MAX_VALUE))
