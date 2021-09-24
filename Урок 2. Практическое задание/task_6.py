import random


def guess_number(number, attempt=9):
    try:
        user_input = int(input("Введите число от 0 до 100: "))
        if user_input == number:
            print("Поздравляю, вы угадали!")
        elif attempt == 0:
            print(f"Закончились попытки, загаданное число было {number}")
        else:
            if user_input > number:
                print(f"Ваше число больше загаданного! Осталось кол-во попыток: {attempt}")
                guess_number(number, attempt - 1)
            elif user_input < number:
                print(f"Ваше число меньше загаданного! Осталось кол-во попыток: {attempt}")
                guess_number(number, attempt - 1)
    except ValueError:
        print("Вы ввели не число!")
        guess_number(number, attempt)


if __name__ == '__main__':
    guess_number(random.randint(0, 100))
