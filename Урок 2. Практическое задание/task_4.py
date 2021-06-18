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


def sum_of_row(n, first_value=1.0):
    if n == 1:
        return first_value
    else:
        return first_value + sum_of_row(n - 1, first_value / -2)


def sum_of_row_2(n, first_value=1.0):
    return first_value if n == 1 else first_value + sum_of_row(n - 1, first_value / -2)


if __name__ == '__main__':
    while True:
        try:
            num_of_elements = int(input('Введите количество элементов ряда'))
            if num_of_elements < 1:
                raise ValueError
            break
        except ValueError:
            print('Ошибка ввода! В ряду должен быть минимум 1 элемент')

    print(f'Количество элементов: {num_of_elements}, их сумма: {sum_of_row(num_of_elements)}')
    print(f'Количество элементов: {num_of_elements}, их сумма: {sum_of_row_2(num_of_elements)}')