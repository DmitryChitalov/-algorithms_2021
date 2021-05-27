def acii(a = 32):
    if a == 128:
        return True
    print(a, "-", chr(a), end=" ")
    if (a-31)%10 == 0:
        print()

    acii(a+1)


acii()