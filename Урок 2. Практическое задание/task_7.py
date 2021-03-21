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
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def equality(number):
    def equality_left(num):
        if num != 0:
            return num + equality_left(num - 1)
        else:
            return 0

    def equality_right(num):
        return num * (num + 1) / 2

    try:
        number = int(number)
        if equality_left(number) == equality_right(number):
            print(f'{equality_left(number)} = {equality_right(number)}')
        else:
            print('Доказательство пошло не по плану')
    except ValueError:
        print('Ошибка, введите корректное число!')
        return equality(input('Введите число: '))


equality(input('Введите число: '))
