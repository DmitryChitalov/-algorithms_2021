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

# решение через ООП

class HexNumber:
    def __init__(self, letters):
        self.letters = letters.upper()

    def __repr__(self):
        return str(list(self.letters))

    def __add__(self, other):
        return HexNumber(str(hex(int(self.letters, 16) + int(other.letters, 16)))[2:])

    def __mul__(self, other):
        return HexNumber(str(hex(int(self.letters, 16) * int(other.letters, 16)))[2:])

first = HexNumber('A2')
second = HexNumber('C4F')

print(first)
print(second)
print(first + second)
print(first * second)

# решение через collections
# к сожалению, каким боком тут приплести collections, я так и не придумал.
# Выполнил только сложение с использованием deque. Признаю, что получилось кривовато.

from collections import deque

def add_numbers(a, b):
    min_number, max_number = map(deque, sorted([a, b], key=len))
    while len(min_number) < len(max_number):
        min_number.appendleft('0')

    order = 0
    result = 0
    while min_number:
        result += (int(min_number.pop(), 16) + int(max_number.pop(), 16)) * 16**order
        print(result)
        order += 1
    print(list(str(hex(result)))[2:])

