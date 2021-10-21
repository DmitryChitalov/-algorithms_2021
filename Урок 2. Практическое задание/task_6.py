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

MAX_RETRIES = 10


def ugadayka(digit, num=MAX_RETRIES) -> int:
    if num:
        asked_num = int(input(f'Try {MAX_RETRIES - num + 1} from {MAX_RETRIES}, your step: '))
        if asked_num == digit:
            print(f'You win. Digit if {digit}')
            # return None
        elif asked_num < digit:
            print('So small? Try again')
            ugadayka(digit, num - 1)
        else:
            print('So big? Try again...')
            ugadayka(digit, num - 1)
    else:
        print('Retries away.... You failed.')
        # return None


if __name__ == '__main__':
    ugadayka(65)
