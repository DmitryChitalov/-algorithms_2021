REVERS_SUM = 0
TRAILING_ZEROS = 0
IS_THIS_TRAILING_ZERO = True

def int_revers(number: int):
    '''
        Функция - реверс целого числа
    '''
    global REVERS_SUM
    global TRAILING_ZEROS
    global IS_THIS_TRAILING_ZERO

    if number // 10 == 0 and number == 0:
        return None

    if number > 0:
        last_digit = number % 10
        if last_digit != 0:
            IS_THIS_TRAILING_ZERO = False
        if IS_THIS_TRAILING_ZERO:
            TRAILING_ZEROS += 1

        REVERS_SUM = (REVERS_SUM * 10) + last_digit
        int_revers(number // 10)
    return REVERS_SUM if TRAILING_ZEROS == 0 else TRAILING_ZEROS * "0" + str(REVERS_SUM)


def ask_user():
    number = input("Введите целое число!")

    try:
        print(int_revers(int(number)))
    except ValueError:
        print("Допускаются только целые числа.")


if __name__ == "__main__":
    ask_user()
