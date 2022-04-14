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
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __add__(self, other):
        return list(hex(int(''.join(self.first), 16) + int(''.join(other.second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first), 16) * int(''.join(other.second), 16)))[2:]


hex_first = list(input('Введите первое число: '))
hex_second = list(input('Введите второе число: '))

print(HexNumber(hex_first, hex_second) + HexNumber(hex_first, hex_second))

print(HexNumber(hex_first, hex_second) * HexNumber(hex_first, hex_second))
