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
    def __init__(self, number):
        self.number = list(number)

    @staticmethod
    def get_number(value):
        return int('0x' + ''.join(value), 16)

    def __add__(self, other):
        result = self.get_number(self.number) + self.get_number(other.number)
        return hex(result)[2:].upper()

    def __mul__(self, other):
        result = self.get_number(self.number) * self.get_number(other.number)
        return hex(result)[2:].upper()

    def __str__(self):
        return ''.join(self.number)


numb_one = HexNumber(input('Введите первое шестнадцатиричное число: '))
numb_two = HexNumber(input('Введите второе шестнадцатиричное число: '))
print(f'Сумма введеных вами шестнадцатиричных числе равна: {numb_one + numb_two}, '
      f'Произведение введеных вами шестнадцатиричных числе равно: {numb_one * numb_two}')
