def num_reverse(number):
    if len(str(number)) == 1:
        return str(number)
    else:
        moving_digit = number % 10
        new_number = number // 10
        return str(moving_digit) + str(num_reverse(new_number))


my_number = int(input('Введите целое число: '))
print(f'Обратное число: {num_reverse(my_number)}')
