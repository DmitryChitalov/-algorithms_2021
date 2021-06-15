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

ф-ции min() и sort() не исп-ем!
"""
import random

lst = [random.randint(-100, 100) for _ in range(10)]
print(lst)


def finder_first(lst):  # Big O notation = O(n**2)
    for i in lst:  # O(n)
        trigger = 0  # O(1)
        for j in lst:  # O(n)
            trigger = 1 if j < i else trigger  # O(1)
        if not trigger:  # O(1)
            return i  # O(1)


def finder_second(lst):  # Big O notation = O(n)
    element = lst[0]  # O(1)
    for i in lst:  # O(n)
        element = i if i < element else element  # O(1)
    return element  # O(1)


print(f'Minimum O(n**2) = {finder_first(lst)}')
print(f'Minimum O(n) = {finder_second(lst)}')
