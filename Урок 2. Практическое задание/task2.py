number = 238650327
even = 0
odd = 0
def recursion(number):
    global even, odd
    if number == 0:
        print ((even, odd))
    else:
        if is_even(number % 10):
            even += 1
        else:
            odd += 1
        recursion(number // 10)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
#3517
recursion(number)