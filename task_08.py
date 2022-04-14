user_year = int(input('Введите год, для проверки на високосность: '))
if user_year % 4 == 0 & user_year % 100 == 0 & user_year % 400:
    print(f'Год високосный')
else:
    print(f'Год невисокосный')
