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


import random


def guessing(attempts=10, random_numer = random.randint(0, 100)):
    '''
    a function-game where you need to guess a pseudo-random number

    param attempts: number of attempts
    param random_numer: pseudo-random number

    return: None
    '''
    if attempts > 0:
        user_input = int(input(f'Отгадайте число! Счётчик попыток = [{attempts}] \n===>>> '))
        if random_numer == user_input:
            print(f'===>>> Вы вийграли!!! <<<===')
        elif random_numer > user_input:
            print(f'Вы ввели меньшее число')
            return guessing(attempts = attempts - 1)
        elif random_numer < user_input:
            print(f'Вы ввели большее число')
            return guessing(attempts = attempts - 1)
    else:
        print(f'Вы проиграли... Загаданное число = {random_numer}')
    
    

guessing(attempts=10)
