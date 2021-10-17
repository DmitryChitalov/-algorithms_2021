def separation_of_digits(user_number):
    global counter_of_even
    global odd_counter
    if user_number == 0:
        return print(f'в числе {user_number}:\n'
                     f'четных чисел - {counter_of_even} {even_numbers}\n'
                     f'нечетных чисел - {odd_counter} {odd_number}')
    else:
        even = user_number % 10
        user_number //= 10
        if even % 2 == 0:
            counter_of_even += 1
            even_numbers.append(even)
        else:
            odd_number.append(even)
            odd_counter += 1
        return separation_of_digits(user_number)


even_numbers = []
odd_number = []
counter_of_even = 0
odd_counter = 0
try:
    number = int(input('Введите число: '))
    print(separation_of_digits(number))
except ValueError:
    print('Вы ввели строку! Введите число цифрами')
    number = int(input('Введите число: '))
    print(separation_of_digits(number))