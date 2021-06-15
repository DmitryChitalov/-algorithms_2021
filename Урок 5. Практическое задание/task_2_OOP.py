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

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict

class HexNumber:
    def __init__(self, x, y):
        self.x = int(f'0x{x}', 16)
        self.y = int(f'0x{y}', 16)

    def __add__(self):
        return self.x + self.y

    def __mul__(self):
        return self.x * self.y

    def get_hex_numb(self, numb):
        self.numb = numb
        return hex(self.numb).split('x')[1].upper()

    def get_dec_numb(self, hex_numb):
        self.hex_numb = int(f'0x{hex_numb}', 16)
        return self.hex_numb

    def get_hex_dict(self, *args):
        self.dict = args
        dct = defaultdict(list)
        for item in self.dict:
            dct[item] = list(item)
        return dct

x, y = 'A2', 'C4F'

hx = HexNumber(x, y)

res1 = hx.get_hex_numb(hx.x * hx.y)
res2 = hx.get_hex_numb(hx.x + hx.y)

print(f"Введены два числа: \n{hx.get_hex_dict(x)} - ({hx.get_dec_numb(x)}) "
      f"и {hx.get_hex_dict(y)} - ({hx.get_dec_numb(y)})\n"
      f"Их произведение: {hx.get_hex_dict(res1)} - {hx.get_dec_numb(res1)}\n"
      f"Их сумма: {hx.get_hex_dict(res2)} - {hx.get_dec_numb(res2)}")

