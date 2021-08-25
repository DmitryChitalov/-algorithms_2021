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


def sum_digits(num, tmp=1.0, sum=0.0):
    return num < 0 and sum or sum_digits(num - 1, (tmp / 2) * -1, sum + tmp)


try:
    number = int(input('Введите количество элементов: '))
    print(sum_digits(number-1))
except ValueError:
    print('Не число')
