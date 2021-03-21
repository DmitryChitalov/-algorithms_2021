"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""

numerical_series = [1]

def numerical_series_sum(user_number, next_number = 1.0):
    if user_number > 0:
        new_number = -next_number / 2
        numerical_series.append(new_number)
        user_number -= 1
        return numerical_series_sum(user_number - 1, new_number)
    else:
        return sum(numerical_series)

user_number = int(input('Введите количество элементов: '))
print(f'Количество элементов: {user_number}, их сумма: {numerical_series_sum(user_number)}')

