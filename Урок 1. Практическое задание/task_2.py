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


# O(n^2)
def find_min_n2(lst):
    for i in range(len(lst)):                       # O(n)
        for j in range(len(lst)):                   # O(n)
            if lst[i] < lst[j]:                     # O(1)
                lst[i], lst[j] = lst[j], lst[i]     # O(1)
    return lst[0]                                   # O(1)


# O(n)
def find_min_n(lst):
    min_val = lst[0]            # O(1)
    for i in lst:               # O(n)
        if i < min_val:         # O(1)
            min_val = i         # O(1)
    return min_val              # O(1)

lst = [24, 12 ,43, 2, 5]
