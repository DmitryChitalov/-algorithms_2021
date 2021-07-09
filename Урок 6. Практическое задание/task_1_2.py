from pympler import asizeof

"""
Задача № 2
Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


# Реализация без оптимизации
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


numb_one = HexNumber('5124975134657812')
print('Использование объекта класса без __slots__:', asizeof.asizeof(numb_one))


# Реализация с наиболее эффективным использованием памяти
class HexNumber2:

    __slots__ = ['number']

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


numb_two = HexNumber2('5124975134657812')
print('Использование объекта класса с использованием __slots__:', asizeof.asizeof(numb_two))

"""
Использование объекта класса без __slots__: 896
Использование объекта класса с использованием __slots__: 728

Вывод:
Сохранине атрибутов с помощью слотов в списке более экономично в отношении используемой памяти, 
ежели сохранение атрибутов в словаре по дефолту.
"""
