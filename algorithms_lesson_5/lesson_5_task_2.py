from collections import defaultdict


def hex_calc():
    numbers = defaultdict(list)
    for d in range(2):
        user_num = input(f'Введите {d + 1}-е 16-ное число: ')
        numbers[f'{user_num}'] = list(user_num)

    sum_res = 0
    mul_res = 1
    for val in numbers.values():
        sum_res += int(''.join(val), 16)
        mul_res *= int(''.join(val), 16)
    print(f'Сумма чисел равна {list(hex(sum_res))[2:]}')         # переводим обратно в 16-ричную систему счисления 
    print(f'Произведение чисел равно {list(hex(mul_res))[2:]}')


hex_calc()
