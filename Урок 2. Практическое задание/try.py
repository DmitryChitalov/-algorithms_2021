def calc():
    operator = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operator == 0:
        print('Exit')
    elif operator == '-' or operator == '+' or operator == '*' or operator == '/':
        try:
            num1 = int(input('Введите первое число: '))
            if not isinstance(num1, int):
                print('Вы ввели строку!!!')
                return calc()
            num2 = int(input('Введите второе число: '))
            if not isinstance(num2, int):
                print('Вы ввели строку!!!')
                return calc()
        except ValueError:
            print('Вы ввели не число!!!')
            return calc()
        if operator == '+':
            result = num1 + num2
            print(result)
            return calc()
        elif operator == '-':
            result = num1 - num2
            print(result)
            return calc()
        elif operator == '*':
            result = num1 * num2
            print(result)
            return calc()
        elif operator == '/':
            result = num1 / num2
            print(result)
            return calc()
        else:
            return calc()

calc()
