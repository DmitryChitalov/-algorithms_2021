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
42 3151 3313
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


def numbers_list(numb):
    numbers = defaultdict(list)
    numbers[numb] = list(numb)
    return numbers


def sum_numbers(numb_1, numb_2):
    return list(format(int("".join(numb_1.keys()), 16) + int("".join(numb_2.keys()), 16), 'X'))


def multiplication_numbers(numb_1, numb_2):
    return list(format(int("".join(numb_1.keys()), 16) * int("".join(numb_2.keys()), 16), 'X'))


x = numbers_list("A2")
y = numbers_list("C4F")
print(f"Сумма {list(x.values())} и {list(y.values())} равняется: {sum_numbers(x, y)}")
print(f"Произведение {list(x.values())} и {list(y.values())} равняется: {multiplication_numbers(x, y)}")


class HexNumber:
    def __init__(self, numb):
        self.numb = list(numb)

    def __str__(self):
        return f"{self.numb}"

    def to_str(self):
        return "".join(self.numb)

    def __add__(self, other):
        result = list(format(int(self.to_str(), 16) + int(other.to_str(), 16), 'X'))
        return result

    def __mul__(self, other):
        result = list(format(int(self.to_str(), 16) * int(other.to_str(), 16), 'X'))
        return result


a = HexNumber('A2')
b = HexNumber('C4F')
print(f"Сумма {a} и {b} равняется: {a + b}")
print(f"Произведение {a} и {b} равняется: {a * b}")