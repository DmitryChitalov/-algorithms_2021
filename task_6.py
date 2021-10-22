"""
6. В программе генерируется случайное целое число от 0 до 100.
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
"""Решение циклом"""
NumberToGuess = random.randint(1,100)
guesses_made = 0

while guesses_made < 3:
    userGuess=int(input("Угадай число от 1 до 100: "))
    guesses_made += 1

    if userGuess > NumberToGuess:
        print("Число должно быть меньше!")
    elif userGuess < NumberToGuess:
        print("Число должно быть больше!")
    else:
        break
if NumberToGuess == userGuess:
    print("Ты угадал, это число = ", str(NumberToGuess))
else:
    print ("Не угадал! Я загадал число {0}".format(NumberToGuess))




def random_number(i):
    """Рекурсия"""
    userGuess = int(input("Угадай число от 1 до 100: "))

    if i == 0:
        print("Не угадал! Я загадал число {0}".format(NumberToGuess))
    else:
        if userGuess > NumberToGuess:
            print("Число должно быть меньше!")
            return random_number(i-1)
        elif userGuess < NumberToGuess:
            print("Число должно быть больше!")
            return random_number(i-1)
        else:
            print("Ты угадал, это число = ", str(NumberToGuess))

NumberToGuess = random.randint(1, 100)
random_number(9)

"""
i - счетчик для кол-ва попыток
"""