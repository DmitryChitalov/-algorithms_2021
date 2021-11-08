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
import re
RE_Nat_number = re.compile(r'^\d+$')


def do_n_half(n, sum = 0):
    if n == 1:
        return sum + 1/(-2)**(n-1)
    else:
        return do_n_half(n-1, sum + 1/(-2)**(n-1))


def input_number():
    number = input('\n(Для выхода - символ "X")'
                   '\nВведите количество элементов: ')

    if RE_Nat_number.fullmatch(number):
        print(f'\nКоличество элементов: {number}, их сумма: {do_n_half(int(number))}')

    elif number.lower() == 'x' or number.lower() == 'х':
        exit()

    else:
        print(f'"{number}" - не натуральное число, исправьтесь.\n')
        input_number()


if __name__ == '__main__':
    input_number()
