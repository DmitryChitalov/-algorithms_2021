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


class GuessTheNumber:
    from random import randrange as rdr

    def __init__(self):
        self.__riddle = self.rdr(100)
        self.__iter = 0
        # print("init:", self.__riddle)

    def play_game(self):
        if self.__iter < 10:
            self.__iter += 1
            guess = int(input("Guess my number? "))
            if guess == self.__riddle:
                print("YOU GUESSED IT! YOU WINN!!!")
            elif guess > self.__riddle:
                print("My number is LESS than that! Try again?")
                self.play_game()
            elif guess < self.__riddle:
                print("My number is GRATER than that! Try again?")
                self.play_game()
        else:
            print("Out of tries, sorry you lost!")


if __name__ == '__main__':
    gtn = GuessTheNumber()
    gtn.play_game()

