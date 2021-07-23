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
from collections import defaultdict


def multiplication(n1, n2):
    hex_num = hex(n1 * n2)
    return list(hex_num[2:].upper())


def addition(n1, n2):
    hex_num = hex(n1 + n2)
    return list(hex_num[2:].upper())


try:
    num1 = input('Введите 1-е число в шестнадцатеричной системе счисления: ')
    num2 = input('Введите 2-е число в шестнадцатеричной системе счисления: ')
    int(num1, 16)
    int(num2, 16)
except ValueError:
    print('Ведены не корректные значения(е)')
else:
    dd1 = defaultdict(list)
    dd1[num1] = list(num1)
    dd1[num2] = list(num2)

    print(f"{num1} + {num2} = {addition(int(''.join(dd1[num1]), 16),int(''.join(dd1[num2]), 16))}")
    print(f"{num1} * {num2} = {multiplication(int(''.join(dd1[num1]), 16),int(''.join(dd1[num2]), 16))}")


# Второй вариант ООП

class HexNumber():
    def __init__(self, txt):
        self.txt = txt
        try:
            self.lst = list(txt)
            self.num = int(''.join(self.lst), 16)
        except ValueError:
            print('Не корректное значение')
            exit()

    def __str__(self):
        return self.txt

    def __add__(self, other):
        return HexNumber(hex(self.num + other.num)[2:].upper()).lst

    def __mul__(self, other):
        return HexNumber(hex(self.num * other.num)[2:].upper()).lst


a = HexNumber(input('Введите 1-е число в шестнадцатеричной системе счисления: '))
b = HexNumber(input('Введите 2-е число в шестнадцатеричной системе счисления: '))

print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')