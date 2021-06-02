def even_odd(number, even, odd):
    if number == 0:
        return f'четных {even} и нечетных {odd}'
    elif number % 2:
        return even_odd(number // 10, even, odd + 1)
    else:
        return even_odd(number // 10, even + 1, odd)


launch = True

while True:
    try:
        print(even_odd(abs(int(input('Введите число: '))), 0, 0))
        break
    except ValueError:
        print("return")





















