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


def guesser(number, counter):
    if counter == 0:
        print(f'У вас не осталось попыток! Загаданное число - {number}')
        return
    elif counter > 4:
        print(f'Осталось {counter} попыток!')
    elif counter > 1:
        print(f'Осталось {counter} попытки!')
    else:
        print(f'Осталась последняя попытка!')
    guess = input('Введите целое число от 0 до 100: ')
    if not guess.isnumeric():
        print('Вы ввели строку вместо числа! Попробуйте ещё раз!')
        guesser(number)
    elif int(guess) == number:
        print('Вы угадали!')
        return
    elif int(guess) > number:
        print('Вы ввели число больше загаданного!')
        guesser(number, counter - 1)
    elif int(guess) < number:
        print('Вы ввели число меньше загаданного!')
        guesser(number, counter - 1)


gen_number = randint(0, 100)
print(gen_number)
guesser(gen_number, 10)
