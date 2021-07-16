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


def find_sum(n, number=1.0, common=0):
    if n == 0:
        return common
    else:
        common += number
        number = number / 2 * -1
        return find_sum(n - 1, number, common)


num = int(input('Введите количество элементов: '))
print(f'Количество элементов: {num}, их сумма: {find_sum(num)}')
