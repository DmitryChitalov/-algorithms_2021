def count_even_odd(n, even=0, odd=0):
    if n == 0:
        return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
    n, digit = divmod(n, 10)
    if not digit & 1:
        even += 1
    else:
        odd += 1
    return count_even_odd(n, even, odd)


print(count_even_odd(int(input('Введите число: '))))
