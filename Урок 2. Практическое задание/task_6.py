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

from random import randint


def play_guess(count=0, rand_num=None):
    if rand_num == None:
        rand_num = randint(0, 100)
    number = int(input('Please enter number: '))
    count += 1
    if number == rand_num:
        print(f'You won on the {count} try')
        return
    elif count == 10:
        print(f'You lose \n hidden number {rand_num}')
        return
    elif number < rand_num:
        print(f'you entered a small number \n {count} try')
        return play_guess(count, rand_num)
    elif number > rand_num:
        print(f'you entered a big number \n {count} try')
        return play_guess(count, rand_num)
    else:
        return play_guess(count, rand_num)


if __name__ == '__main__':
    play_guess()