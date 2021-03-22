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

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


# --- Сложение -----------------------------------------------------------------
def addition(number_1, number_2):
    """Функция рекурсивного сложения"""

    if number_2 > 0:
        return addition(number_1, number_2 - 1) + 1
    elif number_2 < 0:
        return addition(number_1, number_2 + 1) - 1
    else:
        return number_1


# --- Вычитание ----------------------------------------------------------------
def subtraction(number_1, number_2):
    """Функция рекурсивного вычитания"""

    if number_2 > 0:
        return subtraction(number_1, number_2 - 1) - 1
    elif number_2 < 0:
        return subtraction(number_1, number_2 + 1) + 1
    else:
        return number_1


# --- Умножение -----------------------------------------------------------------
def multiplication(number_1, number_2):
    """Функция рекурсивного умножения"""

    if number_2 > 0:
        return number_1 + multiplication(number_1, number_2 - 1)
    elif number_2 < 0:
        return multiplication(number_1, number_2 + 1) - number_1
    else:
        return 0


# --- Деление. Погрешность от 0.01 до 0.1, точнее не получилось ))) ------------
def division_2(number_1, number_2, x=1):
    """Функция рекурсивного деления целой части числа"""

    if number_1 - number_2 <= number_2:
        return x + float('0.' + str(division_3((number_1 - number_2) * 100, number_2)))
    x += 1
    return division_2(number_1 - number_2, number_2, x)


def division_3(number_1, number_2, x=1):
    """Функция рекурсивного деления дробной части числа"""
    
    if number_1 - number_2 <= number_2:
        return x
    x += 1
    return division_3(number_1 - number_2, number_2, x)
# -------------------------------------------------------------------------------


def arithmetic():
    print('-' * 50, '\nДля выхода введите => 0')
    operation = input('Введите вид арифметической операции: ')

    if operation == '0':
        print('Выход')
        return

    try:
        number_1 = int(input('Введите первое число: '))
        number_2 = int(input('Введите второе число: '))
        if operation not in ['+', '-', '*', '/']:
            raise Exception('Не введена арифметическая операция!!!')
        if operation == '/' and number_2 == 0:
            raise ZeroDivisionError('Деление на ноль!!! Ввод данных отменен')
    except ValueError:
        print('Не введено целочисленное значение!!!')
        arithmetic()
    except Exception as e_in:
        print(e_in)
        arithmetic()
    except ZeroDivisionError as e_zero:
        print(e_zero)
        arithmetic()

    if operation == '+':
        answer = addition(number_1, number_2)
    elif operation == '-':
        answer = subtraction(number_1, number_2)
    elif operation == '*':
        answer = multiplication(number_1, number_2)
    else:
        if number_2 > number_1 and len(str(number_2)) > len(str(number_1)):
            len_ten = 10**(len(str(number_2)) - len(str(number_1))) * 10
            number_10 = number_1 * len_ten
            answer = division_2(number_10, number_2) / len_ten
        elif number_2 > number_1 and len(str(number_2)) == len(str(number_1)):
            len_ten = 100
            number_10 = number_1 * len_ten
            answer = division_2(number_10, number_2)
            answer = answer / len_ten
        elif number_1 == number_2:
            answer = division_2(number_1, number_2) - 0.1   # Костыль
        else:
            answer = division_2(number_1, number_2) + 0.01  # Костыль

    print(f'{number_1} {operation} {number_2} = {answer}')
    arithmetic()


# --- main ----------------------------------------------------------------------
arithmetic()
