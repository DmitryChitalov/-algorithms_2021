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


def enter_number():
    try:
        val = abs(int(input('Please enter some number\n')))
    except ValueError:
        print("Error you've entered incorrect value")
        return enter_number()
    return val


def formula(n):
    if n == 1:
        return n
    else:
        return n + formula(n - 1)
    

number = enter_number()
if float(formula(number)) == number * (number + 1) / 2:
    print('True')
else:
    print('False')
