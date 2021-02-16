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

import random


def checkinput():
    user_input = input('Ведите целое число от 1 до 100: ')
    try:
        int(user_input)
    except ValueError:
        print('Вы ошибочно ввели строку. Попробуйте ещё раз')
        return checkinput()
    else:
        if int(user_input) in range(1, 100):
            return int(user_input)
        else:
            print('Вы ошибочно ввели число не входящее в заданный диапазон. Попробуйте ещё раз')
            return checkinput()


def ugadaika(number, counter):
    user_number = checkinput()
    if counter < 10:
        if number != user_number:
            if number < user_number:
                print("Вы указали большое число")
                counter += 1
                ugadaika(number, counter)
            else:
                print("Вы указали маленькое число")
                counter += 1
                ugadaika(number, counter)
        else:
            print(f"Поздравляем! Вы угадали число за {counter} попыток.")
    else:
        print("Вы проиграли")
        return


number = random.randint(1, 100)
print("Здравствуйте! Компьютер загадал число")
counter = 0
ugadaika(number, counter)
