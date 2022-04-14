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

my_list = [0, 3, 1, 9, 7, 5, 8]


def min_count_list(some_list):  # O(n^2)
    for i in some_list:
        min_check = True
        for j in some_list:
            if j < i:
                min_check = False
        if min_check:
            return i


def min_count_list_2(some_list):  # O(n)
    min_val = some_list[0]
    for i in some_list:
        if i < min_val:
            min_val = i
    return min_val


print(min_count_list(my_list))
print(min_count_list_2(my_list))
