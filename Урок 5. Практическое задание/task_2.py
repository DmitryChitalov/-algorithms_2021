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


class Hex:
    def __init__(self, value):
        self.value = list(value)

    def __add__(self, other):
        result = self.get_int(self.value) + self.get_int(other.value)
        return Hex(hex(result)[2:].upper())

    def __mul__(self, other):
        result = self.get_int(self.value) * self.get_int(other.value)
        return Hex(hex(result)[2:].upper())

    def __str__(self):
        return str(self.value)

    @staticmethod
    def get_int(value):
        return int('0x'+''.join(value), 16)


if __name__ == "__main__":

    a = Hex(input('Ведите первое HEX число: '))
    b = Hex(input('Ведите второе HEX число: '))

    summ = a + b
    mult = a * b

    print('Вы ввели', a, 'и', b)
    print('Сумма', summ)
    print('Произведение', mult)

"""
вывод
    Ведите первое HEX число: A2
    Ведите второе HEX число: C4F
    Вы ввели ['A', '2'] и ['C', '4', 'F']
    Сумма ['C', 'F', '1']
    Произведение ['7', 'C', '9', 'F', 'E']
"""