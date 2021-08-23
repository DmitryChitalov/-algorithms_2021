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
import random

random_numbers = [random.randint(0, 100) for i in range(10)]


# O(n^2) - квадратичная
def minimal_value_quadratic_algorithm(lst):
    for i in lst:
        min_value = True
        for j in lst:
            if i > j:
                min_value = False
        if min_value:
            return i


# O(n) - линейная
def minimum_value_linear_algorithm(lst):
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


print(minimal_value_quadratic_algorithm(random_numbers))
print(minimum_value_linear_algorithm(random_numbers))
