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


def calc(n, result):
    if n == 0:
        return 0
    return result + calc(n - 1, result / -2) if n > 1 else result


count = int(input('Введите количество элементов: '))
print(f'Количество элементов: {count}, их сумма: {calc(count, 1)}')
