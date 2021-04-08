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
def game(num_iter=1, random_int=randint(0,100),
         number=-1):
    if number != random_int:
        number = int(input('введите целое число от 0 до 100:'))
    if num_iter == 10:
        print("вы не угадали, правильный ответ:", random_int)
        return random_int
    elif number == random_int:
        print("вы угадали! правильный ответ:", random_int)
        return random_int
    else:
        if number > random_int:
            print("правильное число меньше", number)
            num_iter += 1
            return game(num_iter, random_int, number)
        else:
            print("правильное число больше", number)
            num_iter += 1
            return game(num_iter, random_int, number)
game()
