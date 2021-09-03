def calculator():
    def check_nums():
        try:
            first_num = int(input("введите первое число:"))
            second_num = int(input("Введите второе число:"))
            return first_num, second_num
        except ValueError:
            print("Введите именно числа!")
            check_nums()

    def check_sign():
        sign = input("Введите знак('+', '-', '*', '/', 0 - выход):")
        if sign not in ('+', '-', '*', '/', '0'):
            print("Выберите знак из перечисленных!")
            check_sign()
        return sign

    first_num, second_num = check_nums()
    sign = check_sign()
    if sign == "0":
        print("Выход")
        return
    try:
        print(eval(f"{first_num}{sign}{second_num}"))
    except ZeroDivisionError:
        print("Деление на ноль невозможно!")
    calculator()


calculator()
