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
# сложность O(n)
def get_min_number(lst):
    min_number = lst[0]                                     # O(1)
    for i in lst:                                           # O(n)
        if i < min_number:                                  # O(1)
            min_number = i                                  # O(1)
    return min_number                                       # O(1)


# Сложность O(n**2)
def get_min_number_2(lst):
    min_number_2 = lst[0]                                   # O(1)
    for i in lst:                                           # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_number_2 > lst[j]:                       # O(1)
                min_number_2 = lst[j]                       # O(1)
    return min_number_2                                     # O(1)


first_list = [100, 50, 3, 4, 23, 10]

print(get_min_number(first_list))

print(get_min_number_2(first_list))
