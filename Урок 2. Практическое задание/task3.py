def calculation(number):
    return number if number < 10 else str(number % 10) + str(calculation(number // 10))


value = int(input('Введите число: '))
print(f'Перевернутое число: {calculation(value)}')
