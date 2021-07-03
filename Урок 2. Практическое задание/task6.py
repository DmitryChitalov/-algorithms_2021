import random

number = random.randint(0,100)
i = 1

def recursion():
    global i
    user_number = int(input("Input number (from 0 to 100) "))
    if user_number == number:
        print("You win")
        print(f'numbers of try is {i}')
    elif i == 10:
        print(f"You lose:(\nThe number is {number}")
    else:
        if user_number > number:
            print("Your number is greater")
            i += 1
            recursion()
        elif user_number < number:
            print("Your number is smaller")
            i += 1
            recursion()

recursion()