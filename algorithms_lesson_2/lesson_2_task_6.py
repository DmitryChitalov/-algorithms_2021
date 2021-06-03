import random


def guess_game(user_input, count=1, guess_num=random.randint(0, 100)):
    if user_input == guess_num or count == 2:
        if user_input == guess_num:
            print('You are the winner!')
        else:
            print('You have blown your chance!')
        return f'The game is over'
    else:
        if user_input > guess_num:
            print('Your number is too big!')
        if user_input < guess_num:
            print('Your number is too small!')
        count += 1
        user_input = int(input('Try again: '))
        return guess_game(user_input, count)


start_num = int(input('Enter a number: '))
print(guess_game(start_num))
