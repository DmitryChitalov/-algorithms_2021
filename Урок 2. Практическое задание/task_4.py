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


def enter_number():
    try:
        val = abs(int(input('Please enter some number\n')))
    except ValueError:
        print("Error you've entered incorrect value")
        return enter_number()
    return val


def sum_numbers(vol, num=1, sum_num=0):
    if vol != 0:
        sum_num += num
        num /= -2
        return sum_numbers(vol - 1, num, sum_num)
    return print(sum_num)


number = enter_number()
sum_numbers(number)
