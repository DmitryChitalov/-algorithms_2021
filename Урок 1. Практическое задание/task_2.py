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


def find_min_quad(data: list):
    """Сложность:
        1n * 2n + 1 = O(n^2)
    """
    for i in data:  # O(n)
        minimum = i  # O(1)
        for j in data:  # O(n)
            if minimum > j:  # O(1)
                minimum = j  # O(1)
    return minimum  # O(1)


def find_min_line(data: list):
    """Сложность:
        1 + 2n + 1 = O(n)
    """
    minimum = data[0]  # O(1)
    for i in data:  # O(2n)
        if i < minimum:
            minimum = i
    return minimum  # O(1)
