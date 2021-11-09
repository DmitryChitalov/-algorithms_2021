"""
Проверка введенных параметров.
"""


def check_input(input_string, is_operation=False):

    if input_string == "0" and is_operation:
        exit()
    elif input_string == "+" or input_string == "-" or input_string == "*" or input_string == "/":
        return True if is_operation else False
    elif input_string.isdigit():
        return True if is_operation is False else False
    else:
        print("Вы ввели что-то не то!\n")
        return False


def calc(operation, first_number, second_number):

    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        #  Skip ZeroDivisionError.
        if second_number != 0:
            return first_number / second_number
        else:
            return 0


"""
Основная рекурсивная функция.
"""


def main_calc():

    operation = (input("Введите операцию (+, -, *, / или 0 для выхода): \n")).lower()
    if check_input(operation, True):
        first_number = input("Введите первое число: \n")
        if check_input(first_number):
            first_number = int(first_number)
            second_number = input("Введите второе число: \n")
            if check_input(second_number):
                second_number = int(second_number)

                print(f"{first_number} {operation} {second_number} = {calc(operation, first_number, second_number)};\n")
                return main_calc()

            else:
                return main_calc()
        else:
            return main_calc()
    else:
        return main_calc()


main_calc()
