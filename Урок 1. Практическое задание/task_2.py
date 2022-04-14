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
# 1.


def min_ver1(lst):      # O(n**2)
    for i in lst:
        min_val = True
        for j in lst:
            if j < i:
                min_val = False
        if min_val:
            return i


# 2.

def min_ver2(lst):      # O(n)
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val


if __name__ == '__main__':

    my_list = [5, 8, 12, 86, 93, 7, 24, 4, 75, 2]
    print(min_ver1(my_list))
    print(min_ver2(my_list))
