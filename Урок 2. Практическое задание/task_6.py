import random


def guess_the_number(hiden=random.randint(0, 100), n=10):
    user_answer = int(input(f'Какое число я загадал? у тебя {n} попыток.'))
    if n == 0:
        return f'Вы проиграли. Загаданное число {hiden}'
    try:
        if user_answer == hiden:
            return 'Вы выиграли'
        elif user_answer > hiden:
            print('Меньше')
            return guess_the_number(hiden, n - 1)
        else:
            print('Больше')
            return guess_the_number(hiden, n - 1)
    except ValueError:
        print('а я просил число')
        return guess_the_number(hiden, n - 1)


print(guess_the_number())
# не пойму что со счетчиком, если подряд несколько раз ввести не числа программа ломается
