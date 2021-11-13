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

from collections import namedtuple


class HexNumber:
    def __init__(self, x = '', y = ''):
        self.x = int(x, 16)
        self.y = int(y, 16)

    def add(self):
        return list(hex(self.x + self.y).upper())[2:]

    def mul(self):
        return list(hex(self.x * self.y).upper())[2:]


hx = HexNumber('A2', 'C4f')
print(hx.add())
print(hx.mul())

# =====================================================


class HexNumber_1:
    def __init__(self, x = ''):
        self.x = int(x, 16)

    def __add__(self, other):
        self.x += other.x
        return list(hex(self.x)[2:].upper())

    def __mul__(self, other):
        self.x *= other.x
        return list(hex(self.x)[2:].upper())


hx1 = HexNumber_1('A2')
hx2 = HexNumber_1('C4f')
print(hx1 + hx2)
print(hx1 * hx2)

# =====================================================


def add_and_multiply(num_1, num_2):
    nums = namedtuple("nums", "num_1 num_2")
    nums.num_1, nums.num_2 = int(num_1, 16), int(num_2, 16)
    print(f'Сумма чисел: {list(hex(nums.num_1 + nums.num_2).upper())[2:]}')
    print(f'Произведение чисел: {list(hex(nums.num_1 * nums.num_2).upper())[2:]}')

add_and_multiply('A2', 'C4F')

# =====================================================
# Как по мне очень интересное задание
# Специально искал решения через ООП - так как для меня это лес
# Я хорошо уяснил что такое переопределение метода или атрибута.
# Но к сожалению так и не понял до конца перегрузку..Первое решение через ООП - 
# истинно мое, которое легко написал. Второе - много интернета, ошибок, тыканья наугад=)