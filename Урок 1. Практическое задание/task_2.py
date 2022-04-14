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


def min_1(lst_obj):
    """
    Сложность: O(N^2)
    """
    min_number = lst_obj[0]  # O(1)
    min_in_iter = lst_obj[0]
    for el_1 in lst_obj:  # O(N)
        for el_2 in lst_obj:  # O(N)
            if el_1 < el_2:  # O(1)
                min_in_iter = el_1  # O(1)
        if min_in_iter < min_number:  # O(1)
            min_number = min_in_iter  # O(1)
    return min_number  # O(1)


def min_2(lst_obj):
    """
    Сложность: O(N)
    """
    min_number = lst_obj[0]  # O(1)
    for el in lst_obj:  # O(N)
        if el < min_number:  # O(1)
            min_number = el  # O(1)
    return min_number  # O(1)


print(min_1([1, 10, 15, 100, 20]))
print(min_2([1, 10, 15, 100, 20]))
