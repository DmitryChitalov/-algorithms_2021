"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""

def sequence_sum(number, cur_el = 1, seq_sum = 1):
    number -= 1
    if number == 0:
        return seq_sum
    else:
        seq_sum += (cur_el / -2)
        cur_el = cur_el / -2
        return sequence_sum(number, cur_el, seq_sum)

try:
    number = int(input("Введите количество элементов:"))
except ValueError:
    print('Вы вместо числа ввели строку. Выходим' )

print('Количество элементов:', number, ', их сумма:', sequence_sum(number))
