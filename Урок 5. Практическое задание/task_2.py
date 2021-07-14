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

    def __init__(self, hex_number):
        self.hex_number = hex_number.upper()

    def __str__(self):
        return str(list(self.hex_number))

    def __add__(self, other):
        return HexNumber(hex(int(self.hex_number, 16) +
                             int(other.hex_number, 16))[2:])

    def __mul__(self, other):
        return HexNumber(hex(int(self.hex_number, 16) *
                             int(other.hex_number, 16))[2:])


hn1 = HexNumber("A2")
hn2 = HexNumber("C4F")

print(hn1)
print(hn2)

print(hn1 + hn2)
print(hn1 * hn2)
