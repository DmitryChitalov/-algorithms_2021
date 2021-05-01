from random import randint

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


def guess_the_number(num=0, hiddNumber=randint(0, 100), attempts=3):
    # print(hiddNumber) # Для удобства
    if attempts == 0:
        return print(f'Attempts ended.\n'
                     f'Number is {hiddNumber}.\n')
    num = int(input(f'Enter your number: \n'))
    if num == hiddNumber:
        return print(f'You Win!\n'
                     f'The hidden number is {hiddNumber}.\n')
    else:
        attempts -= 1
        print(f'Wrong! {attempts} attempts left\n'
              f'The number is {"greater" if num < hiddNumber else "less"}.\n')
        return guess_the_number(num, hiddNumber, attempts)


guess_the_number()
