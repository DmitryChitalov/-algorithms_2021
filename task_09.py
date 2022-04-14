user_num_1 = int(input('Введите первое число: '))
user_num_2 = int(input('Введите второе число: '))
user_num_3 = int(input('Введите третье число: '))

if user_num_1 < user_num_2 < user_num_3:
    print(f'Среднее число: {user_num_2}')
elif user_num_1 > user_num_2 > user_num_3:
    print(f'Среднее число: {user_num_2} ')
elif user_num_2 > user_num_1 > user_num_3:
    print(f'Среднее число: {user_num_1}')
elif user_num_2 < user_num_1 < user_num_3:
    print(f'Среднее число: {user_num_1}')
elif user_num_1 > user_num_3 > user_num_2:
    print(f'Среднее число: {user_num_3}')
elif user_num_1 < user_num_3 < user_num_2:
    print(f'Среднее число: {user_num_3}')
else:
    print(f'Имеются одинаковые значения')
