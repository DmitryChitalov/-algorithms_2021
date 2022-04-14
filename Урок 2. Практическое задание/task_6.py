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

from random import random
def guess_the_number(k = 10):
    if k > 0:
        users_n = int(input('enter some random number from 0 to 100: '))
        n = int(random() * 100)
        if users_n == n:
            return f'you are right! the hidden number is {n}'
        else:
            print(f'your number is {"greater" if users_n > n else "less"} than the hidden number. try more!')
            return guess_the_number(k - 1)
    else:
        return f'attempts ended!'

if __name__ == "__main__":
    print(guess_the_number())

