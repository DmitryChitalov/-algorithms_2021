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

TEXT_GENERATOR = {
    'OPERATION_INPUT': lambda: f'Введите операцию ({valid_operations[:-1]} или {valid_operations[-1]} для выхода): ',
    'NUMBER_INPUT': lambda number: f'Введите {number} число: ',
    'NUMBER_1_INPUT': lambda: TEXT_GENERATOR['NUMBER_INPUT']('первое'),
    'NUMBER_2_INPUT': lambda: TEXT_GENERATOR['NUMBER_INPUT']('второе'),
    'NUMBER_INPUT_ERROR': lambda input_value:
        f'Вы вместо числа ввели {input_value}. Исправьтесь.',
    'ZERO_DIVISION_ERROR': lambda: 'Нельзя делить на 0',
    'OPERATION_INPUT_ERROR': lambda input_value:
        f'Вы вместо разрешенных операций {valid_operations} ввели {input_value}',
    'RESULT': lambda result: f'Ваш результат {result}',
}

valid_operations = ['+', '-', '*', '/', '0']


def validate_operation(operation):
    return operation in valid_operations


def calc(number_1, operation, number_2):
    return eval(f'{number_1} {operation} {number_2}')


def calculator(operation=None, number_1=None, number_2=None):
    if operation is None:
        operation = input(TEXT_GENERATOR['OPERATION_INPUT']())
        if not validate_operation(operation):
            print(TEXT_GENERATOR['OPERATION_INPUT_ERROR'](operation))
            calculator()
        elif operation == '0':
            return 0

    if number_1 is None:
        number_1 = input(TEXT_GENERATOR['NUMBER_1_INPUT']())
        if not number_1.isnumeric():
            print(TEXT_GENERATOR['NUMBER_INPUT_ERROR'](number_1))
            calculator(operation)

    if number_2 is None:
        number_2 = input(TEXT_GENERATOR['NUMBER_2_INPUT']())
        if not number_2.isnumeric():
            print(TEXT_GENERATOR['NUMBER_INPUT_ERROR'](number_2))
            calculator(operation, number_1)

    if (operation == '/') & (number_2 == '0'):
        print(TEXT_GENERATOR['ZERO_DIVISION_ERROR']())
        calculator()

    result = calc(number_1, operation, number_2)
    print(TEXT_GENERATOR['RESULT'](result))
    calculator()


calculator()
