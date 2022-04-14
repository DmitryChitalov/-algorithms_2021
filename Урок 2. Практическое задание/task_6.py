"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint


def validate_number(number):
    try:
        tempnumber = int(number)
    except ValueError:
        return False
    else:
        if int(number) < 0 or int(number) > 100:
            return False
        else:
            return True


def input_number():
    while True:
        number = input(f'Введите целое число от 0 до 100: ')
        number = number.replace(' ', '')
        if validate_number(number):
            number = int(number)
            break
        print(f'Вы ввели {number}. Исправьтесь')
    return int(number)


counter = 0
mysterious_number = randint(0, 100)


def guessing(attempts):
    global counter
    global mysterious_number
    if attempts == counter:
        return print(f'Попытки закончились. Загаданноечисло: {mysterious_number}\n'
                     f'GAME OVER\n'
                     f'Вы проиграли!')
    else:
        user_number = input_number()
        if user_number == mysterious_number:
            return print(f'Подзравляю! Вы угадали! Попыток осталось {attempts}!')
        elif mysterious_number < user_number:
            attempts -= 1
            print(f'Вы не угадали! Попробуйте еще раз.\n'
                  f'Загаданное число меньше введёного\n'
                  f'Попыток осталось {attempts}')
            return guessing(attempts)
        elif mysterious_number > user_number:
            attempts -= 1
            print(f'Вы не угадали! Попробуйте еще раз.\n'
                  f'Загаданное число больше введёного\n'
                  f'Попыток осталось {attempts}')
            return guessing(attempts)


player_attempts = 10
print(f'Игра "Угадай число"\nВам необходимо отгадать загаданное число за {player_attempts} попыток.\n')
guessing(player_attempts)
