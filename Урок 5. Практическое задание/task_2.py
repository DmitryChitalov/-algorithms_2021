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


def str_to_hex(s='0'):
    tmp = ''
    for i in s:
        tmp += i
    return int(tmp, 16)


print("Cложения и умножения двух шестнадцатиричных чисел.\n")
user_num_i = input("Введите первое число.")
user_num_ii = input("Введите второе число.")
# 1
num_dict = defaultdict(str)
num_dict['i'] = [s.upper() for s in user_num_i]
num_dict['ii'] = [s.upper() for s in user_num_ii]
number_sum = [s.upper() for s in str(hex(str_to_hex(num_dict['i']) + str_to_hex(num_dict['ii'])))[2:]]
number_mult = [s.upper() for s in str(hex(str_to_hex(num_dict['i']) * str_to_hex(num_dict['ii'])))[2:]]
print(f"Сумма чисел из примера: {number_sum}, произведение - {number_mult}.")

# 2
class Hexnumber:
    str_to_num = 1
    def __init__(self):
        pass

    def __add__(self):
        return 1 + 1

    def __mul__(self):
        return 1 * 1


