"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import randint


def number_compare(user_number, hidden_number):
    if user_number == hidden_number:
        print('Поздравляю, вы угадали!')
        return None
    elif user_number > hidden_number:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')
    return True


def guess(number: int, try_counter: int):
    if try_counter <= 0:
        print(f'Попытки закончились =( Мы загадали число {number}')
        return None
    print(f'Осталось попыток: {try_counter}')
    user_input = int(input('Введите число: '))
    if number_compare(user_input, number):
        guess(number, try_counter - 1)


magic_number = randint(0, 100)
guess(magic_number, 10)
