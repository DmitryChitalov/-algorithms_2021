'''Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.'''


def is_number(parametr_x):
    try:
        parametr_x = float(parametr_x)
    except:
        parametr_x = is_number(input('Вы ввели не число, введите, пожалуйста, число: '))
    return parametr_x

def div_0(number):
    if number == 0:
        number = input('На 0 делить нельзя/n введите новое число: ')
        number = is_number(number)
        number = div_0(number)

    return number


def calculator(znak):
    if znak == '0':
        return
    if znak == '+' or znak == '-' or znak == '/' or znak == '':

        first_number = is_number(input('Введите первое число: '))
        second_number = is_number(input('Введите второе число: '))
        if znak == '/':
            second_number = div_0(second_number)
            print(first_number / second_number)
        elif znak == '':
            print(first_number * second_number)
        elif znak == '+':
            print(first_number + second_number)
        elif znak == '-':
            print(first_number - second_number)
        calculator(input('Введите операцию +, -, *, / , или 0 для выхода: '))
    else:
        calculator(input('неверная команда, попробуйте еще раз: '))


calculator(input('Введите операцию +, -, *, / , или 0 для выхода: '))