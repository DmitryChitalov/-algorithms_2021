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

el_count = int(input('введите количество элементов'))
n = 1.5
operator = 'minus'
numbers = 1
summ = 0


def plus_minus(length):
    global operator
    global summ
    global n
    global numbers
    summ += numbers
    if length == 1:
        return summ
    else:
        if operator == 'minus':
            numbers -= n
            n = n / 2
            operator = 'plus'
        elif operator == 'plus':
            numbers += n
            n = n / 2
            operator = 'minus'
        length -= 1
        return plus_minus(length)


plus_minus(el_count)
print(summ)
