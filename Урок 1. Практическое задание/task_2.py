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


# O(n^2)

def sort_values(lst):
    for i in range(0, len(lst) - 1):         # O(n)
        for j in range(i + 1, len(lst)):     # O(n)
            if lst[j] < lst[i]:    # O(log n)
                lst[i], lst[j] = lst[j], lst[i]    # O(1)


lst = [2, 10, 1]
sort_values(lst)
print(lst[0])


# O(n)

def min_value(lst):
    low = lst[0]    # 0(1)
    for el in lst:   # 0(n)
        if el < low:    # 0(1)
            low = el   # 0(1)
    return low     # O(1)


print(min_value([7, 5, 4]))