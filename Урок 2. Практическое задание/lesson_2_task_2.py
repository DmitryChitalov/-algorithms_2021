def get_result(num,even=0, odd=0):
    print(num,even,odd)
    if num == 0:
        return (f'Четных: {even}, нечетных: {odd}')
    else:

        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
        return get_result(num, even, odd)


number = int(input('Введите число: '))
print(get_result(number))

