"""Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь"""
try:
    number = int(input("Введите трехзначное число: "))
    if number // 1000 == 0:
        hundred = number % 10
        ten = number // 10 % 10
        one = number // 100
        print(f'Сумма цифр числа: {hundred + ten + one}\n'
              f'Произведение цифр числа: {hundred * ten * one}')
    else:
        print("Вы ввели не трехзначное число")
except ValueError:
    print("Вы ввели не число")
