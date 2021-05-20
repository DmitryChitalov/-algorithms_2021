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
from collections import deque


def my_hex(numb):
    signs = '0123456789ABCDEF'
    table = defaultdict(int)
    counter = 0
    for key in signs:
        table[key] += counter
        counter += 1

    num = deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()

    return list(num)



class HexMath:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        num_1 = int(''.join(self.number_1), 16)
        num_2 = int(''.join(self.number_2), 16)
        return list(hex(num_1 + num_2).upper())[2:]

    def __mul__(self, other):
        num_1 = int(''.join(self.number_1), 16)
        num_2 = int(''.join(self.number_2), 16)
        return list(hex(num_1 * num_2).upper())[2:]



if __name__ == '__main__':
    number_1 = list(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
    number_2 = list(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

    print('Решение с использованием collections:')
    print(f'Сумма чисел: '
          f'{my_hex(int("".join(number_1), 16) + int("".join(number_2), 16))}')
    print(f'Произведение чисел: '
          f'{my_hex(int("".join(number_1), 16) * int("".join(number_2), 16))}')

    print()
    print('=' * 100)
    print()

    print('Решение с применением методов ООП:')
    result_sum = HexMath(number_1, number_2) + HexMath(number_1, number_2)
    result_mul = HexMath(number_1, number_2) * HexMath(number_1, number_2)
    print(f'Сумма чисел: {result_sum}')
    print(f'Произведение чисел: {result_mul}')

