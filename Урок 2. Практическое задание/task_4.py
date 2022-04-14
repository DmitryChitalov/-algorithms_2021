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


def summation_divided(el_num, el=1, total=0, count=0):
    if count == el_num:
        return total
    else:
        total += el
        el /= -2
        el_num -= 1
        return summation_divided(el_num, el, total)


data = int(input('Введите количество элементов: '))
print(summation_divided(data))

