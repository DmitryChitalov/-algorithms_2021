import random


def my_game(a, try_count):
    if try_count == 0:
        print(f'Game over! The number was {a}')
    else:
        user_num = int(input('Введите число от 1 до 100: '))
        if user_num == a:
            print(f'You win! Number is {a}')
        else:
            print(f'Fail! Try one more time! осталось попыток: {try_count-1}!')
            return my_game(a, try_count-1)


my_game(random.randint(1, 100), 10)
