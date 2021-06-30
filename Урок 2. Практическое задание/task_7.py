def sum_for_left(n):
    if n==1:
        return n
    return n+sum_for_left(n-1)


def n_input():
    try:
        num = int(input('Введите натуральное число чтобы проверить равенство: \n1 + 2 +...+ n = n(n + 1) / 2 \n'))
        if num <= 0:
            print('Error! т.е. ОШИБКА!!! может я забыл сказать, число должно быть натуральным')
            return n_input()
    except ValueError:
        print('Не похоже это на натуральное число')
        return n_input()
    return equality_cheking(num)


def equality_cheking(num):
    print(f'Итак наше сравнение: {sum_for_left(num)} и ', int(num * (num + 1) / 2))
    if sum_for_left(num) != num * (num + 1) / 2:
        print('Равество не сложилось')
    else:
        print('Равество выполняется')


n_input()
