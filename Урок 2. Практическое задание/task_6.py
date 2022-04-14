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


def guess_number(try_count=1, hidden_number=random.randint(0, 100)):
    print(f"Это ваша попытка №{try_count}")
    answer = int(input("Угадайте и введите число от 0 до 100: "))
    if try_count == 10 or answer == hidden_number:
        if answer == hidden_number:
            print(f"Вы угадали с {try_count} попытки")
        else:
            print("Вы исчерпали все попытки")
        print(f"Было загаданно число: {hidden_number}")
    else:
        if answer > hidden_number:
            print(f"Загаданное число меньше, чем {answer}")
        else:
            print(f"Загаданное число больше, чем {answer}")
        guess_number(try_count=try_count + 1, hidden_number=hidden_number)


if __name__ == '__main__':
    guess_number()
