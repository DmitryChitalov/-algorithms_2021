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

from random import randint


# Алгоритм с квадратичной сложностью
def search_minimal_q(target_list):
    if len(target_list) == 0:    # O(1) - Константная
        return 0    # O(1) - Константная

    minimal_value = target_list[0]  # Условимся, что первое значение по дефолту минимальное, O(1) - Константная

    for element in target_list:  # O(N) - Линейная
        for sub_element in target_list:  # O(N) - Линейная
            if element < sub_element and element < minimal_value:   # O(len(sub_element)) and O(len(minimal_value))
                minimal_value = element    # O(1) - Константная

    return minimal_value    # O(1) - Константная


def search_minimal_l(target_list):
    if len(target_list) == 0:  # O(1) - Константная
        return 0  # O(1) - Константная

    minimal_value = target_list[0]  # O(1) - Константная

    for element in target_list:
        if element < minimal_value:
            minimal_value = element

    return minimal_value


number_list = [randint(0, 100) for index in range(10)]
print(f'Исходный список: {number_list}')
minimal_int_q = search_minimal_q(number_list)
minimal_int_l = search_minimal_l(number_list)
print(f'Значение квадротичной функции: {minimal_int_q}. Значение линейной функции: {minimal_int_l}.')
