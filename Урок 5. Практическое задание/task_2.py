"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
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
"""


class HexNumber:
    def __init__(self, number):
        self.hex_number = number

    def __add__(self, number):
        hex_sum = hex(int(self.hex_number, 16) + int(number.hex_number, 16))
        return str(hex_sum)[2:].upper()

    def __mul__(self, number):
        hex_mul = hex(int(self.hex_number, 16) * int(number.hex_number, 16))
        return str(hex_mul)[2:].upper()

    def __str__(self):
        return self.hex_number


if __name__ == '__main__':
    num_1 = HexNumber(input('Enter the first number: '))
    num_2 = HexNumber(input('Enter the second number: '))
    # num_1 = HexNumber('A2')
    # num_2 = HexNumber('C4F')

    print(f'Sum: {num_1 + num_2}\n'
          f'Mul: {num_1 * num_2}\n')
