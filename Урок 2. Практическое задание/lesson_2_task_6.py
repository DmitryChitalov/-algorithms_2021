import random

def get_num(num, i ):
    if i == 10:
        print('Вы исчерпали 10 попыток. Было загадано', num)
    u = int(input(str(i) + '-я попытка: '))
    if u > num:
        print('Загаданное число меньше')
        return get_num(num, i+1)
    elif u < num:
        print('Загаданное число больше')
        return get_num(num, i+1)
    else:
        print('Вы угадали с %d-й попытки' % i)
        return

print('Число загадано, у Вас 10 попыток')
num = random.randint(1,100)
get_num(num, 1)