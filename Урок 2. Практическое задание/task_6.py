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

# answer = None
# number = 13
# while answer != number:
#     answer = int(input('Угадай число: '))
#     if answer == number:
#         print("Ты выиграл!")
#     elif answer > number:
#         print("Загаданное число меньше")
#     else:
#         print("Загаданное число больше")


def guess_number(answer, number, attempt):
    answer = int(input('Угадай число: '))
    attempt -= 1
    if answer == number:
        return 'Ты выиграл'
    elif attempt == 0:
        return 'Попытки кончились'
    elif answer > number:
        print('Загаданное число меньше')
        return guess_number(answer, number, attempt)
    else:
        print('Загаданное число больше')
        return guess_number(answer, number, attempt)


print(guess_number(None, 13, 10))
