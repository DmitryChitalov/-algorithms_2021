operands = []


def sum_ints(number: int):
    '''
        Сумма ряда 1+2+3...n ...
    '''

    if number == 1:
        operands.append(str(number))
        return 1
    res = number + sum_ints(number - 1)
    operands.append(str(number))
    return res


def ask_user():
    '''
        Запрос пользоветелю
    '''

    number = input("Введите целое число! ")

    try:
        int_number = int(number)
        res = sum_ints(int_number)

        if res == (int_number * (int_number + 1) / 2):
            print(f'{" + ".join(operands)} = {number}({number} + 1)/2')

    except ValueError:
        print("Допускаются только целые числа.")


if __name__ == "__main__":
    ask_user()
