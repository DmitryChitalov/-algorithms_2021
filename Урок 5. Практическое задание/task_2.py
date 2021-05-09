"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
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

DIGITS = '0123456789ABCDEF'
hex_num_dict = defaultdict(list)


def create_hex_num(string):
    digit_list = []
    for ch in string.upper():
        if ch in DIGITS:
            digit_list.append(ch)
        else:
            raise ValueError('Недопустимое шестнадцатиричное чисело')
    return digit_list


def add_hex_num(hex_dict):
    res = hex(int(''.join(hex_dict[0]), 16) + int(''.join(hex_dict[1]), 16))
    return create_hex_num(res[2:])


def mul_hex_num(hex_dict):
    res = hex(int(''.join(hex_dict[0]), 16) * int(''.join(hex_dict[1]), 16))
    return create_hex_num(res[2:])


def get_numbers():
    try:
        hex_num_dict[0] = create_hex_num(input('Введите первое 16-ричное число: '))
        hex_num_dict[1] = create_hex_num(input('Введите второе 16-ричное число: '))
    except ValueError:
        print('Неверный ввод.')
    else:
        print(f'Сумма введённых чисел: {add_hex_num(hex_num_dict)}\n'
              f'Произведение введённых чисел: {mul_hex_num(hex_num_dict)}')


if __name__ == '__main__':
    get_numbers()
