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
from collections import defaultdict as defdict


# 1 Способ.
def hexad_operat():
    nums = defdict(list)
    print("Эта программа выполняет сложение и умножение для чисел 16-ой системы.")
    nums['1 num'] = list(input('Введите первое число из 16-ой системы: '))
    nums['2 num'] = list(input('Введите второе число из 16-ой системы: '))
    try:
        num1, num2 = int(''.join(nums['1 num']), 16), int(''.join(nums['2 num']), 16)
    except ValueError:
        return "Введенные символы не соответсвуют 16-ой системе."
    else:
        nums['sum'] = list(str(hex(num1 + num2))[2:].upper())
        nums['mul'] = list(str(hex(num1 * num2))[2:].upper())
        return f'Результат сложения: {nums["sum"]}.\n' \
            f'Результат произведения чисел: {nums["mul"]}.'


print(hexad_operat())


# 2 Способ.
class Hexnumber:

    def __init__(self, num):
        self.num = num.upper()

    def __add__(self, other):
        return str(hex(int(self.num, 16) + int(other.num, 16)))[2:].upper()

    def __mul__(self, other):
        return str(hex(int(self.num, 16) * int(other.num, 16)))[2:].upper()


hh = Hexnumber('a2')
hh2 = Hexnumber('C4F')
print(hh.num)
print(f'Сумма чисел {hh.num} и {hh2.num}: {hh + hh2}')
# Сумма чисел  и C4F: CF1
print(f'Произведение чисел {hh.num} и {hh2.num}: {hh * hh2}')
# Произведение чисел A2 и C4F: 7C9FE
