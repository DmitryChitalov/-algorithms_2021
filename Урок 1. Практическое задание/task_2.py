"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
"""
import random


def find_min_item_quad(lst):                # O(N^2)

    min_value = lst[0]                      # O(1)

    for i in range(len(lst)):               # O(N)
        for j in range(len(lst)):           # O(N)
            if i != j:                      # O(1)
                if lst[i] < lst[j]:         # O(1)
                    if lst[i] < min_value:  # O(1)
                        min_value = lst[i]  # O(1)
                else:
                    if lst[j] < min_value:  # O(1)
                        min_value = lst[j]  # O(1)

    return min_value


"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""


def find_min_item_line(lst):        # O(N)

    min_value = lst[0]              # O(1)

    for i in range(len(lst)-1):     # O(N)
        if lst[i+1] < min_value:    # O(1)
            min_value = lst[i+1]    # O(1)

    return min_value


"""
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

sample_lst = random.sample(range(-100000, 100000), 100)
print(sample_lst)
print(find_min_item_quad(sample_lst))
print(find_min_item_line(sample_lst))
