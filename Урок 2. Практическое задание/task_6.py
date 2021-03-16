"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
from random import randint


def guess_the_number(hidden_num, attempts=10):
    if attempts == 0:
        print(f'Попытки закончились, было загадано число {hidden_num}')
    else:
        print(f'Осталось попыток: {attempts}')
        try:
            user_num = int(input('Попробуйте угадать число:'))
        except ValueError:
            print("Вы ввели не число. Попытка не считается, попробуйте еще раз. ")
            guess_the_number(hidden_num, attempts)
        else:
            if user_num == hidden_num:
                print(f'Победа!!! Вы отгадали число!!!')
            elif user_num < hidden_num:
                print(f'Неправильно, загаданное число больше.')
                guess_the_number(hidden_num, attempts - 1)
            else:
                print(f'Неправильно, загаданное число меньше.')
                guess_the_number(hidden_num, attempts - 1)


hidden_num = randint(0, 100)
guess_the_number(hidden_num)
