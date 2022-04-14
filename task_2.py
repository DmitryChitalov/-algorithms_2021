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


# Первый
def first_finding_minimum(list):
    min_number = 100
    for i in list:
        for j in range(0, len(list) - 1):
            if i > list[j] & list[j] < min_number:
                min_number = list[j]
    return min_number


# Второй
def second_finding_minimum(list):
    min_number = list[0]
    for j in range(0, len(list) - 1):
        if list[j] < min_number:
            min_number = list[j]
    return min_number


list_search = [41, 15, 22, 16, 120, 51, 4, 22, 27, 100]
print(first_finding_minimum(list_search))
print(second_finding_minimum(list_search))
