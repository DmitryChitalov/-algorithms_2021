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


class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


def req_guess_number(n, tries):
    while True:
        try:
            user_number = int(input(f"Ваш ответ? "))
            if user_number < 0 or user_number > 100:
                raise OwnError("Введено число не от 0 до 100!")
            # Основной блок, ввод пользователя валидный
            if user_number == n:
                print('Число угадано, поздравляем')
            elif tries == 1:
                print(f'Попытки закончились, повезет в другой раз. Было загадано число {n}')
            else:
                tries -= 1
                if user_number > n:
                    print(f'Мимо, Ваше число больше. Осталось попыток {tries}')
                else:
                    print(f'Мимо, Ваше число меньше. Осталось попыток {tries}')
                req_guess_number(n, tries)
            # Конец основного блока
            break # Выход из Вайлтру
        except ValueError:
            print('Введено не число!')
        except OwnError as err:
            print(err)


max_tries = 6
print(f'Вам загадано число от 1 до 100. У Вас {max_tries} попыток.')
random_number = random.randint(1, 100)
req_guess_number(random_number, max_tries)
