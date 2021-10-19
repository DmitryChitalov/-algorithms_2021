from collections import defaultdict


def add_to_dict(number, add_dict):
    for i in number:
        add_dict[number].append(i)


def to_sixteen(num):
    num_str = '0123456789ABCDEF'
    if num // 16 == 0:
        return num_str[num]
    else:
        return to_sixteen(num // 16) + num_str[num % 16]


num_dict = defaultdict(list)

num_1 = input('Введите первое число шестнадцатиричной системы: ')
num_2 = input('Введите второе число шестнадцатиричной системы: ')

add_to_dict(num_1, num_dict)
add_to_dict(num_2, num_dict)

num_sum = to_sixteen(int(num_1, 16) + int(num_2, 16))
num_mul = to_sixteen(int(num_1, 16) * int(num_2, 16))

add_to_dict(num_sum, num_dict)
add_to_dict(num_mul, num_dict)

print(f'Сумма чисел равна: {num_dict[num_sum]}')
print(f'Произведение чисел:  {num_dict[num_mul]}')


# Сделала только через defaultdict