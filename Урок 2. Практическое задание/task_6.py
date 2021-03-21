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


def game(rand_num=randint(0, 100), count=10):
    if count == 0:
        return print(f"Game over. The hidden number: {rand_num}")
    try:
        user_num = int(input("Enter number: "))
        if user_num == rand_num:
            return print(f"Excellent. You are irresistible. The hidden number: {rand_num}")
        elif user_num > rand_num:
            print("Your number is greater than the hidden one")
        elif user_num < rand_num:
            print("Your number is less than the hidden one")
        game(rand_num, count - 1)
    except ValueError:
        print("Invalid number")
        game(rand_num, count)
    except UnboundLocalError:  # Срабатывает в конце, если был ввод строки.
        pass


game()
