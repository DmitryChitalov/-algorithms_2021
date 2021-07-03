number = 35609

reversed_number = []
def recursion(number):
    if number == 0:
        print(int(''.join(map(str,reversed_number))))
    else:
        reversed_number.append(number % 10)
        recursion(number // 10)


recursion(number)
