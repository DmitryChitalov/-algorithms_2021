def even_odd_numbers_input():
    try:
        number = int(input('Введите число - '))
    except ValueError:
        print("Вводить можно только натуральные числа")
        return even_odd_numbers_input()
    else:
        print(f'\nВ числе {number} ')
        return number


def even_odd_numbers(number, even=0, odd=0):
    if number == 0:
        print(f'четных чисел - {even}, нечетных - {odd}')

    else:
        remains = number % 10
        number = number // 10
        if remains % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd_numbers(number, even, odd)


even_odd_numbers(even_odd_numbers_input())
