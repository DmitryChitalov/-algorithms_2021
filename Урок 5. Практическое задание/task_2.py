"""
2.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict

dig = '0123456789ABCDEF'
hex_num_dict = defaultdict(list)


def create(string):
    digit_list = []
    for i in string.upper():
        if i in dig:
            digit_list.append(i)
        else:
            raise ValueError('Неправильное число')
    return digit_list


def add_num(hex_dict):
    result = hex(int(''.join(hex_dict[0]), 16) + int(''.join(hex_dict[1]), 16))
    return create(result[2:])


def mul_num(hex_dict):
    result = hex(int(''.join(hex_dict[0]), 16) * int(''.join(hex_dict[1]), 16))
    return create(result[2:])


def get_numbers():
    try:
        hex_num_dict[0] = create(input('Введите первое число: '))
        hex_num_dict[1] = create(input('Введите второе число: '))
    except ValueError:
        print('Некорректный ввод числа.')
    else:
        print(f'Сумма чисел: {add_num(hex_num_dict)}\n'
              f'Произведение чисел: {mul_num(hex_num_dict)}')


if __name__ == '__main__':
    get_numbers()
