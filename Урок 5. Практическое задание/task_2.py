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

import collections as cl


class HexNum:

    def __init__(self, lst=None):
        if lst is None:
            lst = []
        mistake = False
        while True:
            if len(lst) != 0:
                self.value = lst
            else:
                self.value = [_.upper() for _ in input()]
            for j in self.value:
                if j not in '0123456789ABCDEF':
                    mistake = True
            if mistake:
                print('Не верное HEX-значение! Попробуйте еще раз!')
                mistake = False
            else:
                break

    def __str__(self):
        return f'{self.value}'

    def __add__(self, other):
        copy_1 = self.value
        copy_2 = other.value
        base = ['0' for _ in range(abs(len(self.value) - len(other.value)))]
        if len(self.value) > len(other.value):
            base.extend(other.value)
            other.value = base
        elif len(self.value) < len(other.value):
            base.extend(self.value)
            self.value = base
        deq = cl.deque()
        digits = '0123456789ABCDEF'
        mod = 0
        for i in range(-1, -len(self.value) - 1, -1):
            next_idx = digits.index(self.value[i]) + digits.index(other.value[i]) + mod
            to_append = f'{digits[next_idx % len(digits)]}'
            mod = next_idx // len(digits)
            deq.appendleft(to_append)
        if mod != 0:
            deq.appendleft(digits[mod])
        self.value = copy_1
        other.value = copy_2
        return HexNum([_ for _ in deq])

    def __mul__(self, other):
        digits = '0123456789ABCDEF'
        gap = []
        c = 0
        to_sum = []
        mod = 0
        for i in range(-1, -len(other.value) - 1, -1):
            element = cl.deque()
            for j in range(-1, -len(self.value) - 1, -1):
                next_idx = (digits.index(other.value[i]) * digits.index(self.value[j]) + mod)
                to_gap = digits[next_idx % len(digits)]
                mod = next_idx // len(digits)
                element.appendleft(to_gap)
            if mod != 0:
                element.appendleft(digits[mod])
                mod = 0
            element.extend(['0' for _ in range(c)])
            gap.append(element)
            c += 1
            to_sum.append([_ for _ in element])
        res = HexNum(['0'])
        for i in to_sum:
            res += HexNum(i)
        return res


print('Введите число 1: ', end='')
a = HexNum()
print('Введите число 2: ', end='')
b = HexNum()
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')