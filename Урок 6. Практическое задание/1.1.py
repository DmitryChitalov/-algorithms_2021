"""
Класс шестнадцатиричных чисел.
Во вторую реализацию добавлены слоты.
Теперь класс имеет в качестве атрибутов только
список цифр заданного числа, хранимый в кортеже.
Замер занимаемой памяти экземпляров классов показывает
10-икратную разницу:
Размер класса HexNumber 472 байт.
Размер класса HexNumberSlot 40 байт.
А так же уменьшение используемой памяти при создании
Экземпляра класса со слотами:
Функция HexNumber __init__:
Время выполнения: 0.21132100000000004 сек.
Использованная память: 0.00390625 Mib.
Функция HexNumberSlot __init__:
Время выполнения: 0.21876600000000002 сек.
Использованная память: 0.0 Mib.
"""

from pympler.asizeof import asizeof
from task_1 import time_memo_prof


class HexNumber:
    __DIGITS = '0123456789ABCDEF'

    @time_memo_prof
    def __init__(self, string):
        self.digit_list = []
        for ch in string.upper():
            if ch in self.__DIGITS:
                self.digit_list.append(ch)
            else:
                raise ValueError('Недопустимое шестнадцатиричное чисело')

    def __add__(self, other):
        if not isinstance(other, HexNumber):
            raise TypeError(f"unsupported operand type(s) for +: 'HexNumber' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 + num_2)
        return HexNumber(res[2:])

    def __mul__(self, other):
        if not isinstance(other, HexNumber):
            raise TypeError(f"unsupported operand type(s) for *: 'HexNumber' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 * num_2)
        return HexNumber(res[2:])

    def __repr__(self):
        return f'HexNumber {self.digit_list}'

    def __str__(self):
        return str(self.digit_list)


class HexNumberSlot:
    __slots__ = ('digit_list')
    __DIGITS = '0123456789ABCDEF'

    @time_memo_prof
    def __init__(self, string):
        self.digit_list = []
        for ch in string.upper():
            if ch in self.__DIGITS:
                self.digit_list.append(ch)
            else:
                raise ValueError('Недопустимое шестнадцатиричное чисело')

    def __add__(self, other):
        if not isinstance(other, HexNumberSlot):
            raise TypeError(f"unsupported operand type(s) for +: 'HexNumberSlot' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 + num_2)
        return HexNumberSlot(res[2:])

    def __mul__(self, other):
        if not isinstance(other, HexNumberSlot):
            raise TypeError(f"unsupported operand type(s) for *: 'HexNumberSlot' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 * num_2)
        return HexNumberSlot(res[2:])

    def __repr__(self):
        return f'HexNumberSlot {self.digit_list}'

    def __str__(self):
        return str(self.digit_list)


n1 = HexNumber('ABC')
n2 = HexNumberSlot('ABC')

print(f'Размер класса HexNumber {asizeof(n1)} байт.')
print(f'Размер класса HexNumberSlot {asizeof(n2)} байт.')
