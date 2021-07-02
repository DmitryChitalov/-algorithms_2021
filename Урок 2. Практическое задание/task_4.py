"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_row(n: int):
    if n == 0:
        return 1
    if n % 2 == 1:
        tmp = 1/pow(-2, n)
    else:
        tmp = 1/pow(2, n)
    return tmp + sum_of_row(n-1)


n = int(input(f'Введите количество элементов: '))
print(f'Количество элементов: {n}, их сумма: {sum_of_row(n-1)}')
