operator = ['+', '-', '*', '/', '0']


def total_value():
    v = input('Введите оператор "*", "/" , "+" , "-" или 0 для выхода: ')
    if v == '0':
        return print('Выход')
    if v in operator:
        try:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
        except ValueError:
            print('Введено неверное значение, необходимо ввести число!!!')
            return total_value()
        try:
            if v == '+':
                print(f'{num1} + {num2} = {num1 + num2}')
            elif v == '-':
                print(f'{num1} - {num2} = {num1 - num2}')
            elif v == '*':
                print(f'{num1} * {num2} = {num1 * num2}')
            elif v == '/':
                print(f'{num1} / {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('На ноль делить нельзя, повторите попытку!!!')
            return total_value()
    else:
        print('Неверный оператор, повторите ввод')
        return total_value()


total_value()
