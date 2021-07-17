count = 32
count_1 = 0
res = []


def table():
    global count
    global count_1
    if count < 128:
        print(f' {count} - {chr(count)}', end=' ')

        count += 1
        count_1 += 1
        if count_1 % 10 == 0:
            print('\n')
        return table()


table()
