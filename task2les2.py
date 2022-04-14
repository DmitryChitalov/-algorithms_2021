def amount_of_even_odd(number: int, even: int = 0, odd: int = 0):
    if number != 0:
        if (number % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return amount_of_even_odd(number // 10, even, odd)
    else:
        print(f'Количество четных цифр: {even}, нечетных цифр {odd})')
        return

while True:
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Некорректный ввод!")
        continue
    amount_of_even_odd(n)
