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

#сложность O(N)
def min_func_1(lst_obj):
    min_num = lst_obj[0]
    for j in range(len(lst_obj)):
        if lst_obj[j] < min_num:
            min_num = lst_obj[j]
    return min_num

#сложность O(N^2)
def min_func_2(lst_obj):
    min_num = lst_obj[0]
    for j in range(len(lst_obj)):
        lst_copy = lst_obj[:]
        if lst_copy[j] < min_num:
            min_num = lst_copy[j]
    return min_num
