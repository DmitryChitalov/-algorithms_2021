import random
"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная."""
numbers_lst = [random.randint(1, 1000) for el in range(random.randrange(1, 1000))]
print(len(numbers_lst))
print(numbers_lst)


def min_number_1(lst):              # O(n^2)
    minimum = sum(lst)
    for i in range(len(lst) - 1):
        for el in lst:
            if lst[i] < el:
                minimum = (lst[i], minimum)[minimum < lst[i]]
    return minimum


print(min_number_1(numbers_lst))


"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""


def min_number_2(lst):              # O(n)
    minimum = list(set(lst))
    return minimum[0]


print(min_number_2(numbers_lst))

"""
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
"""

"""
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
