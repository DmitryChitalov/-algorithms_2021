"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить нельзя!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def func(num_x):
    if num_x == 1:
        return 1
    if num_x % 2:
        return func(num_x-1) + 1/(2**(num_x-1))
    else:
        return func(num_x-1) - 1/(2 ** (num_x-1))


if __name__ == '__main__':
    num = int(input('Введите количество элементов: '))
    print(f'Количество элементов: {num}, их сумма: {func(num)}')
