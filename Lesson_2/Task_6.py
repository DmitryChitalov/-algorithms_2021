from random import randint


def guessing(num, count):
    if count == 0:
        return 'У Вас закончились попытки. Вы проиграли.'
    user_num = int(input('Введите число: '))
    if user_num == num:
        return 'Вы угадали!'
    else:
        print('Ваше число {}'.format('меьше' if user_num < num else 'больше'))
        return guessing(num, count-1)


print(guessing(randint(1, 100), 10))