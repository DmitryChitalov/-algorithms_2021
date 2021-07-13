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


def guess_number(hidden_number, attempts_count=0, is_guessed=False, attempts_number=10):
    if attempts_count == attempts_number or is_guessed:
        if is_guessed is False:
            print(f"Сожалею, вы не угадали за {attempts_count} попыток!")
        return hidden_number
    else:
        number = int(input("Введите ваш ответ: \n"))
        attempts_count += 1
        if number < hidden_number:
            print("Загаданное число больше!")
        elif number > hidden_number:
            print("Загаданное число меньше!")
        elif number == hidden_number:
            print(f"Поздравляю, вы угадали за {attempts_count} попыток!")
            is_guessed = True

        return guess_number(hidden_number, attempts_count, is_guessed)


hidden_num = random.randint(1, 100)
print("Комьютер загадал число от 1 до 100. Попробуйте отгадать за 10 попыток")
print(f"Было загадано: {guess_number(hidden_num)}")
