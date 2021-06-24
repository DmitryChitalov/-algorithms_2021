def recur(i):
    if i == 1:
        return i
    else:
        return i + recur(i-1)


def formula(i):
    return i*(i + 1)/2


num = 4
if recur(num) == formula(num):
    print('Равенство доказано')

