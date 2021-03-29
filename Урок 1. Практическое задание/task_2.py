"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random

def find_min_value_1(lst_obj):
    min_value = lst_obj[0]                           # O(1)
    for i, val_i in enumerate(lst_obj[1:]):          # O(n) - линейная, где n = len(lst_obj)
        for j, val_j in enumerate(lst_obj[i:]):      # O(n) - линейная
            if val_j < min_value and val_j < val_i:  # O(2)
                min_value = val_j                    # O(1)
    return min_value                                 # 0


def find_min_value_2(lst_obj):
    min_value = lst_obj[0]                           # O(1)
    for i, val_i in enumerate(lst_obj[1:]):          # O(n) - линейная, где n = len(lst_obj)
        if val_i < min_value: min_value = val_i      # O(1)
    return min_value                                 # 0


lst = random.sample(range(1, 100), 5)                # Генерируем случайный список из 5-ти элементов
# Тест 1 Сложность O(n^2)
print(f'Элемент {find_min_value_1(lst)} является минимальным в списке {lst}')
# Тест 2 Сложность O(n)
print(f'Элемент {find_min_value_2(lst)} является минимальным в списке {lst}')