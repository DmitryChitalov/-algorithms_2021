def funk(n, num=1, sum_num=0):
    if n == 0:
        print(sum_num)

    else:
        n -= 1
        sum_num = (sum_num + num)
        num = num / -2
        return funk(n, num, sum_num)


funk(int(input('Введите количество элементов - ')))
