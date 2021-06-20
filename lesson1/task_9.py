"""

Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""
try:
    NUM_1 = int(input('Введите 1-ое число:'))
    NUM_2 = int(input('Введите 2-ое число:'))
    NUM_3 = int(input('Введите 3-ое число:'))

    if NUM_2 < NUM_1 < NUM_3 or NUM_3 < NUM_1 < NUM_2:
        print(f'Среднее: {NUM_1}')
    elif NUM_1 < NUM_2 < NUM_3 or NUM_3 < NUM_2 < NUM_1:
        print(f'Среднее: {NUM_2}')
    else:
        print(f'Среднее: {NUM_3}')
except ValueError:
    print("Вы ввели не число")
