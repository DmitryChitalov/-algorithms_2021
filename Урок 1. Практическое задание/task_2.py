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


# O(N^2)
def min_value_1(list_to_check):
    for item_to_check in list_to_check:
        is_min = True
        for item in list_to_check:
            if item_to_check <= item and is_min:
                is_min = True
            else:
                is_min = False
                break
        if is_min:
            return item_to_check


# O(N)
def min_value_2(list_to_check):
    min_value = list_to_check[0]
    for item in list_to_check[1:]:
        if item < min_value:
            min_value = item
    return min_value


# O(N)
def min_value_3(list_to_check):
    return min(list_to_check)


user_input = input('Введите значения типа int через пробел:')
lst = [int(item) for item in user_input.split()]

print(min_value_1(lst))
print(min_value_2(lst))
print(min_value_3(lst))
