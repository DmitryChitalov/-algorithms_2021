num = list(input('Введите число '))


def even_odd(user_num, odd=0, even=0):
    if len(user_num) > 0:
        temp = int(user_num.pop())
        temp = temp % 2
        if temp == 1:
            odd += 1
        else:
            even += 1
        return even_odd(user_num, odd, even)
    if len(user_num) == 0:
        return f'Четных чисел {even}, а нечетных {odd}'


print(even_odd(num))
