"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
"""


def sum_of_the_elements(quantity: int):
    result = 1
    if quantity == 0:
        return 0
    result += sum_of_the_elements(quantity - 1) / -2
    return result


user_input = int(input('Введите количество элементов: '))
print(f'Количество элементов: {user_input}, их сумма: {sum_of_the_elements(user_input)}')
