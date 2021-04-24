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


def min_quad(numbers):
    # Сложность O(N**2)

    min_val = numbers[0]  # O(1)
    for i in range(len(numbers)):  # O(N)
        for j in range(len(numbers)):  # O(N)
            if numbers[i] < numbers[j]:  # O(1)
                if numbers[i] < min_val:  # O(1)
                    min_val = numbers[i]  # O(1)

    return min_val  # O(1)


def min_line(numbers):
    # Сложность O(N)

    min_val = numbers[0]  # O(1)
    for i in range(len(numbers)):  # O(N)
        if numbers[i] < min_val:  # O(1)
            min_val = numbers[i]  # O(1)

    return min_val  # O(1)


my_list = [6, 23, -6, 0, 89, 14, -1, 2, -17]

print(f'Квадратичная: {min_quad(my_list)}')
print(f'Линейная: {min_line(my_list)}')
