﻿"""
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



def sum_row(my_number, n):
    if n > 1:
        return my_number + sum_row(my_number / -2, n - 1)
    else:
        return my_number

n = int(input("Введите количество элементов: "))
#print("Количество элементов: %d, их сумма: %.2f" % (n,sum_row(0, 1, n)))
print(sum_row(1, n))