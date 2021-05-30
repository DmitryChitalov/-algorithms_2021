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


def min_list_number1(numbers_list):             # Сложность функции: O(n**2) квадратичная
    for i in numbers_list:                      # O(n)
        is_lower = 0                            # O(1)
        for n in numbers_list:                  # O(n)
            if i <= n:                          # O(1)
                is_lower += 1                   # O(1)
            else:
                break
        if is_lower == len(numbers_list):       # O(1)
            min_num = i                         # O(1)
    return min_num                              # O(1)


def min_list_number2(numbers_list):             # Сложность функции: O(nlogn) линейно-логарифмическая
    min_number = numbers_list[0]                # O(1)
    for i in numbers_list:                      # O(n)
        if i < min_number:                      # O(1)
            min_number = i                      # O(1)
    return min_number                           # O(1)


test_numbers_list = [4, 3, 6, 7, 1, -9, 0]
print(min_list_number1(test_numbers_list))
print(min_list_number2(test_numbers_list))