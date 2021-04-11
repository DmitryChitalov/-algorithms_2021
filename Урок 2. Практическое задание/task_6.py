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


class Game:
    incorrect_number = 101

    def __init__(self):
        self.__number_to_guess = random.randint(0, 100)
        self.users_number = self.incorrect_number
        self.attempt_count = 10

    def is_guessed(self):
        if self.users_number == self.__number_to_guess:
            print("Верно!!! УРРРАААААААААААААА!!!!")
            return True
        elif self.users_number > self.__number_to_guess:
            print("Введите число поменьше")
        elif self.users_number < self.__number_to_guess:
            print("Введите число побольше")
        self.users_number = self.incorrect_number
        return False

    def users_number_check(self):
        try:
            self.users_number = int(self.users_number)
            if 0 < self.users_number < 100:
                return True
            else:
                return False
        except ValueError:
            return False

    def enter_number(self):
        self.users_number = input("Введите число от 0 до 100: ")

    def are_there_any_attempts(self):
        return self.attempt_count > 1

    def play(self):
        print(f'Осталось попыток: {self.attempt_count}')
        while not self.users_number_check():
            self.enter_number()
        if self.is_guessed() or not self.are_there_any_attempts():
            if not self.are_there_any_attempts():
                print(f'Загаданное число: {self.__number_to_guess}')
            return
        else:
            self.attempt_count -= 1
            self.play()


game = Game()
game.play()
