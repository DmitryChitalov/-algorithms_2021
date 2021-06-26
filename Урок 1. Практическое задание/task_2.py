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


def minimal_value_1(list_object):
    """ Return a minimal value from list. Made in O-Big Linear time"""
    min_value = list_object[0]
    for el in range(1, len(list_object)):
        if list_object[el] < min_value:
            min_value = list_object[el]
    return min_value


def minimal_value_2(list_object):
    """Return a minimal value from list. Made in O-Big Logarithmic time"""
    if len(list_object) == 1:
        return list_object[0]
    else:
        min_value = minimal_value_2(list_object[1:])
        if list_object[0] < min_value:
            return list_object[0]
        else:
            return min_value


if __name__ == '__main__':
    some_list = [7, 3, 8, 4, 10, 9, 2, 10, 8, 5]
    print(minimal_value_1(some_list))
    print(minimal_value_2(some_list))
