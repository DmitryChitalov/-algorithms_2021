from random import randint


def rand_num(value, count=9):
    answer = int(input('Введите число от 0 до 100: '))
    if value == answer:
        return print(f'Верно правильный ответ {value}')
    else:
        if count == 0:
            return print(f'Вы проиграли, правильный ответ {value}')
        elif answer != value and value < answer:
            count -= 1
            print('Неверно, загаданное число меньше')
        elif answer != value and value > answer:
            count -= 1
            print('Неверно, загаданное число больше')
        return rand_num(number, count)


number = randint(0, 100)
rand_num(number)
