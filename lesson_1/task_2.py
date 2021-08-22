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


def get_min_1(lst):
    """
    перебираем массив, используя каждый элемент для сравнения со всеми остальными
    если все остальные элементы массива меньше - возвращаем результат

    Сложность: O(n^2)
    """
    for i in range(len(lst)):  # O(n)

        i_is_min = True  # O(1)

        for j in range(i + 1, len(lst)):  # O(n)
            if lst[i] > lst[j]:  # O(1)
                i_is_min = False  # O(1)
                break

        if i_is_min:  # O(1)
            return lst[i]  # O(1)


items = [11, 10, 2, 9, 3, 8, 4, 7, 5, 6]

print(get_min_1(items))
