import random


def playing_with_a_pc(number, attempts=9, used=0):
    user = int(input('Введите число от 0 до 100: '))
    if number == user:
        return print(f'Вы угадали с {used} попытки.')
    elif attempts == 0:
        return print(f'У вас закончилось 10 попыток. Загаданное число {number}')
    else:
        if number > user:
            print(f'Загаданное число больше указаного. У вас осталось {attempts} попыток.')
            playing_with_a_pc(number, attempts - 1, used + 1)
        elif number < user:
            print(f'Загаданное число меньше указаного. У вас осталось {attempts} попыток.')
            playing_with_a_pc(number, attempts - 1, used + 1)


random_number = random.randint(0, 100)
try:
    playing_with_a_pc(random_number)
except ValueError:
    print('Вы ввели строку! Введите число цифрами')
    playing_with_a_pc(random_number)
