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

def recursiv_method(count, numb):
    print(f"Попытка {count}")
    answer = int(input("Введите число от 0 до 100"))
    if count == 10 or answer == numb:
        if answer == numb:
            print("Правильно!")
        print(f"Загаданное число {numb}")
    else:
        if answer > numb:
            print("Число меньше")
        else:
            print("Число больше")
        recursiv_method(count + 1, numb)

recursiv_method(1, random.randint(0, 100))