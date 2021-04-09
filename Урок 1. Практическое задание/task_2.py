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
import random


# Алгоритм 1, сложность O(n^2)
def min_in_list_n2(list_obj):
    list_compared = list_obj
    min_number = list_obj[0]
    for i in list_obj:
        flag_not_min = False
        for j in list_compared:
            if i > j:
                flag_not_min = True
        if not flag_not_min:
            min_number = i
    return min_number


# Алгоритм 2, сложность O(n)
def min_in_list_n(list_obj):
    min_number = list_obj[0]
    for i in list_obj:
        if i < min_number:
            min_number = i
    return min_number


test_list = [random.randint(0, 10000) for _ in range(100)]
print(test_list)
print(min_in_list_n2(test_list))
print(min_in_list_n(test_list))
