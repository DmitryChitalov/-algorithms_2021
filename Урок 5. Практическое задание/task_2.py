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
from collections import deque

# Обычное решение

first_num = deque(input('Введите первое число, например A2: ').strip())
second_num = deque(input('Введите второе число, например С2F: ').strip())

hex_sum = deque(hex(int(''.join(first_num), 16) + int(''.join(second_num), 16)))
hex_sum.popleft()
hex_sum.popleft()
print(f'Сумма числа {list(first_num)} и {list(second_num)} равна {list(hex_sum)}')

hex_mul = deque(hex(int(''.join(first_num), 16) * int(''.join(second_num), 16)))
hex_mul.popleft()
hex_mul.popleft()
print(f'Произведение числа {list(first_num)} и {list(second_num)} равно {list(hex_mul)}')


# Решение через ООП

class HexNumber():

    def __init__(self, number):
        self.number = deque(number)

    def __add__(self, other):
        obj_sum = deque(hex(int(''.join(self.number), 16) + int(''.join(other.number), 16)))
        obj_sum.popleft()
        obj_sum.popleft()
        return HexNumber(obj_sum)

    def __mul__(self, other):
        obj_mul = deque(hex(int(''.join(self.number), 16) * int(''.join(other.number), 16)))
        obj_mul.popleft()
        obj_mul.popleft()
        return HexNumber(obj_mul)


a1 = HexNumber(first_num)
a2 = HexNumber(second_num)
a3 = a1 + a2
a4 = a1 * a2
print(a3.number)
print(a4.number)
