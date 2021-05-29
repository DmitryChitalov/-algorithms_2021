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
def guess():
    import random
    random_number = random.randint(0, 100)
    guess_recurtion(number=random_number)

def guess_recurtion(number, current_attempt=1, max_attempt = 10):
    if current_attempt > max_attempt:
        return print(f'Количество попыток исчерпано. Вы проиграли. Правильное число: {number}')
    user_number = int(input('Введите число: '))
    if user_number == number:
        return print(f'Вы угадали! Правильное число: {number}')
    elif user_number > number:
        print('Введеное число больше загаданного')
        return guess_recurtion(current_attempt=current_attempt + 1, number=number)
    elif user_number < number:
        print('Введеное число меньше загаданного')
        return guess_recurtion(current_attempt=current_attempt + 1, number=number)

guess()


