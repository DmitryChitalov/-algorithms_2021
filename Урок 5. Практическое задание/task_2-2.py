"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

HEX_DICT = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}

INT_DICT = {
    0: '0', 1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B',
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}


def create_hex_num(string):
    digit_list = deque()
    for ch in string.upper():
        if ch in HEX_DICT:
            digit_list.append(ch)
        else:
            raise ValueError('Недопустимое шестнадцатиричное чисело')
    return digit_list


def hex_to_int(h_num):
    h_num = h_num.copy()
    res = 0
    while h_num:
        res += HEX_DICT[h_num.popleft()] * 16 ** len(h_num)
    return res


def int_to_hec(num):
    res = deque()
    while num >= 16:
        num, div = divmod(num, 16)
        res.appendleft(INT_DICT[div])
    res.appendleft(INT_DICT[num])
    return res


def add_hex_num(num_1, num_2):
    return int_to_hec(hex_to_int(num_1) + hex_to_int(num_2))


def mul_hex_num(num_1, num_2):
    return int_to_hec(hex_to_int(num_1) * hex_to_int(num_2))


if __name__ == '__main__':
    try:
        n1 = create_hex_num(input('Введите первое 16-ричное число: '))
        n2 = create_hex_num(input('Введите второе 16-ричное число: '))
    except ValueError:
        print('Неверный ввод.')
    else:
        print(f'Сумма введённых чисел: {list(add_hex_num(n1, n2))}\n'
              f'Произведение введённых чисел: {list(mul_hex_num(n1, n2))}')
