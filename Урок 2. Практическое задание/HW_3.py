def reverse():
    user_num = input('Введите число: ')
    num_lst = list(user_num)

    def recur(num, res=''):
        if len(num) > 0:
            temp = num.pop()
            res = res + temp
            return recur(num, res)
        else:
            return f'Результат: {res}'

    return recur(num_lst)


print(reverse())
