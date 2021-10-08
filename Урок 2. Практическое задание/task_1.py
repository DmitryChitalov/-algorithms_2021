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

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import re
import sys
# sys.setrecursionlimit(999999999) # установить глубину рекурсии
print(f'глубина рекурсии = {sys.getrecursionlimit()}')


def get_sum(first_num, second_num):
    '''
    param first_num: first term
    param second_num: second term

    return: sum of terms 
    '''
    if second_num > 0:
        return get_sum(first_num, second_num - 1) + 1
    elif second_num < 0:
        return get_sum(first_num, second_num + 1) - 1
    else:
        return first_num


def subtract_num(first_num,second_num):
    '''
    param first_num: minuend 
    param second_num: subtrahend

    return: residual
    '''
    if second_num > 0:
        return subtract_num(first_num, second_num-1) - 1
    elif second_num < 0:
        return subtract_num(first_num, second_num+1) + 1
    else:
        return first_num


def multiplication_num(first_num, second_num):
    '''
    param first_num: first factor 
    param second_num: second factor

    return: product of numbers
    '''
    if not second_num:
        return 0
    return first_num + multiplication_num(first_num, second_num-1)


def division(first_num, second_num):
    '''
    param first_num: dividend 
    param second_num: divider

    return: quotient
    '''
    if not second_num :
        return 'ОШИБКА! На ноль делить?'
    return first_num / second_num


def math_actions(sign, first_num, second_num):
    '''
    param sign: operation sign
    param first_num: what is to the left of the sign 
    param second_num: what is to the right of the sign

    return: mathematical action depending on the sign
    '''
    if sign == '+':
        print(f'Сумма = {get_sum(first_num, second_num)}')
    elif sign == '-':
        print(f'Разность = {subtract_num(first_num, second_num)}')
    elif sign == '*':
        print(f'Произведение = {multiplication_num(first_num, second_num)}')
    else:
        print(f'Частное = {division(first_num, second_num)}')


def loop():
    '''
    param: takes no parameters
    return: None if the selected operation is "0", 
            otherwise calls the function will call itself 
            up to the recursion limit
    '''
    selected_operation = input('Выбирите операцию (+, -, *, / или 0 для выхода): ')
    if selected_operation == '0':
        print('EXIT')
        return None
    elif selected_operation in ['+', '-', '*', '/']:
        first_num = input('Введите первое число: ')
        second_num = input('Введите второе число: ')
        if first_num.isdigit() and second_num.isdigit():
            first_num, second_num = int(first_num), int(second_num)
            math_actions(selected_operation, first_num, second_num)
        else:
            print('ОШИБКА! Нужны целые положительные числа.')
    else:
        print('ОШИБКА! Выбирите операцию (+, -, *, / или 0 для выхода)')
    loop()

            
loop()