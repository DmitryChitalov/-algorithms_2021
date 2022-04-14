def numerical_series(number: int):
    '''
        Функция - подсчитывает сумм числового ряда 1 -0.5 0.25 -0.125 ...
    '''

    if number == 1:
        return 1

    sign = -1 if (number - 1) % 2 == 0 else 1

    return (-sign) * 1 / pow(2, number - 1) + numerical_series(number - 1)


def ask_user():
    '''
        Запрос пользоветелю
    '''
    
    number = input("Введите целое число! ")

    try:
        print(numerical_series(int(number)))
    except ValueError:
        print("Допускаются только целые числа.")


if __name__ == "__main__":
    ask_user()
