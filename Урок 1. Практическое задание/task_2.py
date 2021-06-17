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

ф-ции min() и sort() не исп-ем!
"""


def first_min(my_list):  # O(N^2)

    for smallest in my_list:  # O(N)
        for num in my_list:  # O(N)
            if smallest > num:  # O(len(smallest)) ?
                smallest = num  # O(1)
    return smallest  # O(1)


def second_min(my_list):  # O(N)

    smallest = my_list[0]  # O(1)
    for i in my_list:  # O(N)
        if i < smallest:  # O(len(i)) ?
            smallest = i  # O(1)
    return smallest  # O(1)


lst = [11, 12, 13, - 14, - 1, 2, 3, 4, 13, - 18, - 1, 2, 3, 4, 5, -3, 7, 8, 9, - 10, 43, 15]
print(first_min(lst))
print(second_min(lst))


def example(my_list):

    a = my_list[0]
    for i in my_list:
        if i < a:
            a = i
        else:
            my_list.remove(i)
    return my_list


print(example(lst))
