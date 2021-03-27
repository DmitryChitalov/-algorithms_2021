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


def fin_num(n, cnt=1):
    my_number = int(input('Твое число: '))
    if cnt == 10:
        return f'Успользовано максимальное количество попыток! Число было {n}'
    if my_number == n:
        return f'Вы Выйграли'
    else:
        if my_number > n:
            print('Много')
        else:
            print('Мало')
        cnt += 1
        return fin_num(n, cnt)

gen_num = random.randint(1, 100)

print(fin_num(gen_num))