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


class WrongOperation(Exception):
    def __init__(self, message=f'Неверно выбрана операция!'):
        self.message = message
        super().__init__(self.message)


def calculate(result=None):
    try:
        operation = input(f'Введите операцию (+, -, *, / или 0 для выхода):')
        if operation not in ['+', '-', '*', '/', '0']:
            raise WrongOperation
        elif operation == '0':
            return result
        else:
            result = float(input(f'Введите первое число:')) if result is None else result
            second_number = float(input(f'Введите следующее число:'))
            if operation == '+':
                result += second_number
            elif operation == '-':
                result -= second_number
            elif operation == '*':
                result *= second_number
            elif operation == '/':
                result /= second_number
            return calculate(result)
    except ZeroDivisionError:
        print('Деление на ноль! Повторите ввод')
        return calculate(result)
    except WrongOperation:
        print('Неверно выбрана операция! Попробуйте снова')
        return calculate(result)
    except ValueError:
        print('Введено неверное значение! Необходимо ввести число (положительное, отрицательное или 0)')
        return calculate(result)
    