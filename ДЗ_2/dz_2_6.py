from random import randint
from sys import exit


def guess_number(guesses=[], mynum=[], attempts=10):

    if attempts == 0:
        print("Попыток больше не осталось.")
        return

    if not guesses:
        user_guess = int(input("Введите число между 0 и 100: "))
        mystery_num = randint(0, 100)
        turn = compare_nums(user_guess, mystery_num)

        # Если не угадали
        guesses.append(user_guess)
        mynum.append(mystery_num)
        guess_number(guesses, mynum, attempts-1)
    else:
        user_guess = int(input("Попытайте еще раз.\n Введите число между 0 и 100: "))
        if user_guess in guesses:
            print("Вы уже вводили это число")
            guess_number(guesses, mynum, attempts-1)
        else:
            turn = compare_nums(user_guess, mynum[0])

            # Если не угадали
            guesses.append(user_guess)
            guess_number(guesses, mynum,attempts-1)


def compare_nums(your_guess, my_num):
    if your_guess == my_num:
        print("Поздравляю, Вы угадали!")
        exit()
    else:
        if your_guess < my_num:
            print("Заданное число - больше")
        else:
            print("Заданное число - меньше")
        return


guess_number()