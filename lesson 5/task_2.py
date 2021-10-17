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

def sum_mul_defaultdict():
    default_dict = defaultdict(list)
    first_num_key = input('Введите первое первое число в шестнадцатиричной системе: ')
    second_num_key = input('Введите второе первое число в шестнадцатиричной системе: ')
    # first_num_key = 'A2'
    # second_num_key = 'C4F'
    first_num_val = hex(int(first_num_key, 16))[2:]
    default_dict[first_num_key] = list(first_num_val.upper())
    second_num_val = hex(int(second_num_key, 16))[2:]
    default_dict[second_num_key] = list(second_num_val.upper())
    sum_sec_num = hex(int(first_num_key, 16) + int(second_num_key, 16))[2:]
    default_dict['sum_sec_num'] = list(sum_sec_num.upper())
    mul_sec_num = hex(int(first_num_key, 16) * int(second_num_key, 16))[2:]
    default_dict['mul_sec_num'] = list(mul_sec_num.upper())
    return f'Сумма чисел: {default_dict["sum_sec_num"]}\n' \
           f'Произведение чисел: {default_dict["mul_sec_num"]}\n' \
           f'Словарь: {default_dict}'

print(sum_mul_defaultdict())
