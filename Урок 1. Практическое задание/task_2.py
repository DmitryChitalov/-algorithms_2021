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


# O(n^2) - квадратичная

def min_0n2(_lst):
    my_list = _lst  # O(1) - константа
    for i in range(len(my_list) - 1):  # O(n) - линейная
        for j in range(i + 1, len(my_list)):  # O(n) - линейная (так как вложенный - то O(n^2) - квадратичная)
            if my_list[j] < my_list[i]:  # O(1) - константа
                my_list[j], my_list[i] = my_list[i], my_list[j]  # O(1) - константа
    return my_list[0]  # O(1) - константа


# O(n) - линейная

def min_0n(my_list):
    lw = my_list[0]  # O(n) - линейная
    for i in my_list:  # O(n) - линейная
        if i < lw:  # O(1) - константа
            lw = i  # O(1) - константа
    return lw  # O(1) - константа


if __name__ == '__main__':
    import numpy as np

    lst = np.random.randint(-1000, 10000, 200)
    print(min_0n2(lst))
    print(min_0n(lst))
