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
from collections import defaultdict

dd = defaultdict(int)

hex_1 = input("Введите первое число:")
hex_2 = input("Введите второе число:")
dd["num_1"] = list(hex_1)
dd["num_2"] = list(hex_2)
dd["sum"] = list(hex(int(hex_1,16)+int(hex_2,16)).strip("0x").upper())
dd["mul"] = list(hex(int(hex_1,16)*int(hex_2,16)).strip("0x").upper())

print(f"{dd['num_1']} + {dd['num_2']} = {dd['sum']}")
print(f"{dd['num_1']} * {dd['num_2']} = {dd['mul']}")

print("\n","*"*20,"\n")

'''
ООП
'''
class HexNum:

    def __init__(self,input_str):
        self.__me = input_str

    def __str__(self):
        return str(self.__me)

    def __add__(self,hex_num):
        hex_out = hex(int(self.__me,16)+int(hex_num.__me,16)).strip("0x").upper()
        return HexNum(hex_out)
    
    def __mul__(self,hex_num):
        hex_out = hex(int(self.__me,16)*int(hex_num.__me,16)).strip("0x").upper()
        return HexNum(hex_out)


hex_1 = HexNum(hex_1)
hex_2 = HexNum(hex_2)
sum_hex = hex_1+hex_2
mul_hex = hex_1*hex_2

print(f"OOP: {list(str(hex_1))} + {list(str(hex_2))} = {list(str(sum_hex))}")
print(f"OOP: {list(str(hex_1))} * {list(str(hex_2))} = {list(str(mul_hex))}")