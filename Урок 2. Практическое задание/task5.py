i = 1

def recursion(n):
    global i
    if n >= 32 and n <= 127:
        if i <= 10:
            i += 1
            print(f'{n} - {chr(n)}')
            recursion(n+1)
        else:
            i = 0
            print("\n")
            recursion(n)
    else:
        pass

recursion(32)