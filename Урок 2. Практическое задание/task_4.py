"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_sum_descending_row(number: int, reminder=1, sum_of_row=0, depth_value=1):
    """
        Считает сумму чисел убывающего ряда (sum_of_row) чисел вида: : 1 -0.5 0.25 -0.125 ...
        где number - количество (depth_value) чисел этого ряда, т.е. натуральное число
    """
    if number == 1:
        sum_of_row += reminder
        reminder /= 2
        return f'Количество элементов: {depth_value} , их сумма: {sum_of_row}'
    if number % 2:
        sum_of_row += reminder
        reminder /= 2
        new_number = number - 1
    else:  # not number % 2
        sum_of_row -= reminder
        reminder /= 2
        new_number = number - 1

    depth_value += 1
    return get_sum_descending_row(new_number, reminder, sum_of_row, depth_value)


user_number = int(input('Введите количество элементов: '))
print(get_sum_descending_row(user_number))
