"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def programme():
    sign = input('Please choose an action: +, -, *, / or enter 0 for exit): ')
    if sign == '0':
        return print('Exit')
    elif sign in '+-*/':
        try:
            num_1 = int(input('Enter the first number: '))
            num_2 = int(input('Enter the second number: '))
            if sign == '+':
                print(f'Your result is {num_1 + num_2}')
                return programme()
            if sign == '-':
                print(f'Your result is {num_1 - num_2}')
                return programme()
            if sign == '*':
                print(f'Your result is {num_1 * num_2}')
                return programme()
            if sign == '/':
                if num_2 == 0:
                    print('Zero division is impossible!')
                    return programme()
                else:
                    print(f'Your result is {num_1 / num_2}')
                    return programme()
        except ValueError:
            print('You entered str-class, but you need int-class. Please adjust it!')
            return programme()
    else:
        print('The sign is incorrect!')
        return programme()


programme()


