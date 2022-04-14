#!/usr/bin/env python3

"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
Правой части в рекурсии быть не должно!!! Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def propcess_left_side(value: int) -> int:
    return value + propcess_left_side(value - 1) if value > 0 else 0


def propcess_right_side(value: int) -> int:
    return int(value * (value + 1) / 2)


def main():
    try:
        value = int(input('Введите число: '))
        result_symbol = '=' if propcess_left_side(value) == propcess_right_side(value) else '!='
        print(f"{'+'.join([str(x) for x in range(1, value + 1)])} {result_symbol} {value}({value}+1)/2")
    except ValueError:
        print('Введены неверные данные.')


if __name__ == '__main__':
    main()
