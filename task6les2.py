def generator(attemp, n):
    print("У вас осталось",10 - attemp , "попыток")
    you = int(input())
    if attemp == 10 or you == n:
        if you == n:
            print("Вы угадали число!")
        print("Загаданное число: ", n)

    else:
        if you > n:
            print("Вы не угадали! Загаданное число меньше!")
        if you < n:
            print("Вы не угадали! Загаданное число больше!")
        generator(attemp+1, n)

generator(0, 43)