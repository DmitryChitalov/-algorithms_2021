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


def sum_of_elements(amount_of_numbers, result=0.0, number=1.0):
    if amount_of_numbers == 0:
        return result
    result = result + number
    if amount_of_numbers % 2 == 0:
        number = (-1 ** (amount_of_numbers + 1) * number) / 2
    else:
        number = (-1 ** amount_of_numbers * number) / 2

    return sum_of_elements(amount_of_numbers - 1, result, number)


print(sum_of_elements(4))
