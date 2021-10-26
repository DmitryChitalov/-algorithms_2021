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


class HexNumber:
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __add__(self, other):

        return list(hex(int(''.join(self.hex_num), 16) + int(''.join(other.hex_num), 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.hex_num), 16) * int(''.join(other.hex_num), 16)).upper())[2:]


first_number = list(input('Введите первое число: '))
second_number = list(input('Введите второе число: '))
hx_1 = HexNumber(first_number)
hx_2 = HexNumber(second_number)
res_sum = hx_1 + hx_2
res_mul = hx_1 * hx_2
print(f'Сумма: {res_sum}')
print(f'Произведение: {res_mul}')
