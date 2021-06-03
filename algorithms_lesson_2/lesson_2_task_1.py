def addition(num_1, num_2):
    return num_1 + num_2


def subtraction(num_1, num_2):
    return num_1 - num_2


def multiplication(num_1, num_2):
    return num_1 * num_2


def division(num_1, num_2):
    try:
        print(num_1 / num_2)
    except ZeroDivisionError:
        print('Division by 0 is not possible!')


def calc_func():
    operation = input('Enter operation or 0 to quit: ')
    if operation == '0':
        return 'Exit'
    else:
        if operation in '+ - * /':
            try:
                num_1 = int(input('Enter an integer: '))
                num_2 = int(input('Enter an integer: '))

                if operation == '+':
                    print(addition(num_1, num_2))
                    return calc_func()

                elif operation == '-':
                    print(subtraction(num_1, num_2))
                    return calc_func()

                elif operation == '*':
                    print(multiplication(num_1, num_2))
                    return calc_func()
                else:
                    division(num_1, num_2) # print - в функции, чтобы избежать None при делении на 0
                    return calc_func()

            except ValueError:
                print("You've entered a string! Enter a number.")
                return calc_func()
        else:
            print('Wrong operation sign!')
            return calc_func()


calc_func()
