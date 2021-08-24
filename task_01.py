user_number = int(input(f'Введите трехзначное число: '))
a = user_number // 100
b = (user_number - a * 100) // 10
c = user_number - (a * 100 + b * 10)

result_sum = a + b + c
result_mult = a * b * c

print(f'Сумма цифр числа: {result_sum} \n'
      f'Произведение цифр числа: {result_mult}')
