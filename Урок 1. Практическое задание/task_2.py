"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.
"""
import random


def min_value(list_value):          # O(n**2) - квадратичная сложность
    """Функция возвращает минимальное значение приятого списка"""  # такая как эта, я думаю, в природе не встречается

    min_val_i = list_value[0]       # O(1)
    for i in list_value:            # O(n)
        min_val_j = i               # O(1)
        for j in list_value:        # O(n)
            if j < min_val_j:       # O(1)
                min_val_j = j       # O(1)
        min_val_i = min_val_j       # O(1)
    return min_val_i                # O(1)
# O(1) + O(n) * (O(1) + O(n) * (O(1) + O(1)) + O(1)) + O(1)
# сокращаем const, получаем O(n**2)


def max_value(list_value):          # O(n) - линейная сложность
    """Функция возвращает максимальное значение приятого списка"""

    max_val = list_value[0]         # O(1)
    for i in list_value:            # O(n)
        if max_val < i:             # O(1)
            max_val = i             # O(1)
    return max_val                  # O(1)
# O(1) + O(n) * (O(1) + O(1)) + O(1)
# сокращаем const, получаем O(n)

# Формирование списка из случайных 10 int(значений)
rand_list = []
for i in range(10):
    rand_values = random.randint(1, 10)
    rand_list.append(rand_values)

print(rand_list)

print(f'Минимальное значение списка: {min_value(rand_list)}')
print(f'Максимальное значение списка: {max_value(rand_list)}')

# Можно всё упростить
print(min(rand_list))
print(max(rand_list))
