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


def check_min(lst_obj):
    """
    Сложность: O(N)
    """
    min_value = lst_obj[0]  # O(1)
    for j in range(len(lst_obj)):  # O(N)
        if lst_obj[j] < min_value:  # O(1)
            min_value = lst_obj[j]  # O(1)
    return min_value  # O(1)


print(check_min([44, 2, 3, 1, 5, 10]))


def check_min_2(lst_obj):
    """
    Сложность: O(N^2)
    """
    for i in lst_obj:
        for j in lst_obj:  # O(N^2)
            if i > j:  # O(1)
                i = j  # O(1)
        return i  # O(1)


print(check_min_2([44, 26676, 34, 9, 56, 11]))
