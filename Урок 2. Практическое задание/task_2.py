def even_check(number, even=0, odd=0):
    if number == 0:
        return f'Четных чисел: {even} , нечетных чисел: {odd}'
    else:
        check_number = number % 10
        new_number = number // 10
        if check_number % 2 == 0:
            even += 1
        else:
            odd += 1
    return even_check(new_number, even, odd)


my_number = int(input('Введите целое число: '))
print(even_check(my_number))
