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


def guess_game():
    while True:
        number = randint(0, 100)
        count = 10
        while count != 0:
            guess = int(input('Введите число от 0 до 100: '))
            if guess > number:
                print('Ваше число больше загаданного')
                count -= 1
            elif guess < number:
                print('Ваше число меньше загаданного')
                count -= 1
            else:
                print('Ура! Вы угадали!')
                break
        print(f'Извините, но Вы проиграли! Попорбуйте сыграть еще раз. Заганное число: {number}')


def guess_game_recurs(count=10, number=randint(0, 100)):
    if count == 0:
        print(f'Извините, но Вы проиграли! Попорбуйте сыграть еще раз. Заганное число: {number}')
        return
    guess = int(input('Введите число от 0 до 100: '))
    if guess == number:
        print('Ура! Вы угадали!')
        return
    else:
        if guess > number:
            print('Ваше число больше загаданного')
            guess_game_recurs(count - 1, number)
        elif guess < number:
            print('Ваше число меньше загаданного')
            guess_game_recurs(count - 1, number)
        else:
            print('Ура! Вы угадали!')


# guess_game()
guess_game_recurs()


