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


def sum_n(n, i=0, el=1, s=0):
    s += el
    el /= -2
    i += 1
    if n == 1:
        return f'Количество элементов: {i}, их сумма: {s}.'
    return sum_n(n-1, i, el, s)


print(sum_n(int(input('Введите количество элементов: '))))
