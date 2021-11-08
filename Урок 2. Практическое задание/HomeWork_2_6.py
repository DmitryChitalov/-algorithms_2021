def lucky(number, count=0):
    chance = f'Пожалуйста введите число! У вас осталось {10-count} попыток'
    print(chance)
    my_number = int(input())

    if count > 10:
        return f'К сожалению Вам не удалось угадать число'

    if my_number == number:
        return f'Вы угадали число!'

    else:
        if my_number < number:
            print('Загаданное число больше!')
        else:
            print('Загаданное число меньше!')
    count += 1
    return lucky(number, count)

print(lucky(17))