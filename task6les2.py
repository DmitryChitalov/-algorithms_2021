def guess_number(attemp, number):
    if attemp == 10:
        print(f"Ваши попытки кончились! Вы не угадали! Загаданное число: {number}")
    try:
        user_number = int(input(f'Угадайте число от 0 до 100 (осталось попыток {10 - attemp}): '))
    except ValueError:
        print(f'Некорректный ввод! Попробуйте еще раз!')
        return guess_number(attemp+1, number)
    if user_number == number:
        print("Вы угадали число!")
        print("Загаданное число: ", number)
    else:
        if user_number > number:
            print("Вы не угадали! Загаданное число меньше!")
            return guess_number(attemp+1, number)
        if user_number < number:
            print("Вы не угадали! Загаданное число больше!")
            return guess_number(attemp+1, number)

guess_number(0, 43)