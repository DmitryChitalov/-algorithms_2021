#калькулятор




def calculation(value_type = 'operation'):
    if value_type = 'operation':
        input_value = input('Введите операцию (+, - , /, * или 0, если хотите завершить работу калькулятора)')
        if input_value in ('+', '-', '*', '/'):
            action = input_value
            x = calculation('number')
            y = calculation('number')
            if action == '+':
                # Выводим сумму x и y
                print('%.2f + %.2f = %.2f' % (x, y, x + y))
                calculation()
            # Если action равен - то
            elif action == '-':
                # Выводим разность x и y
                print('%.2f - %.2f = %.2f' % (x, y, x - y))
                calculation()
            # Если action равен * то
            elif action == '*':
                # Выводим результат умножения x на y
                print('%.2f * %.2f = %.2f' % (x, y, x * y))
                calculation()
            # Если action равен / то
            elif action == '/':
                if y == 0:
                    print('Деление на ноль невозможно')
                    y = calculation('number')
                else:
                    # Выводим результат деления x на y
                    print('%.2f / %.2f = %.2f' % (x, y, x / y))
                    calculation()
        elif input_value == '0':
            print('Всего доброго!')
            return
        else:
            print('Вы ввели неверную операцию')
            calculation('operation')
    else:
        input_value = input('Введите число')
        try:
            number_input = float(input_value)
            return number_input
        except:
            print('Вы ввели неверное число')
            calculation('number')
 