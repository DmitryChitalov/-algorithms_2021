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


from collections import defaultdict, namedtuple
from functools import reduce


# Вариант_1 "defaultdict"
def hex_result(n_1, n_2):
    collect = defaultdict(list)
    collect['summ'] = list(hex(int(n_1, 16) + int(n_2, 16))[2:].upper())
    collect['mult'] = list(hex(int(n_1, 16) * int(n_2, 16))[2:].upper())
    return f'Сумма чисел {list(n_1.upper())} и {list(n_2.upper())} = {collect["summ"]}\n' \
           f'Произведение чисел {list(n_1.upper())} и {list(n_2.upper())} = {collect["mult"]}'


# Вариант_2 "defaultdict" и reduce
def hex_reduce(n_1, n_2):
    collect = defaultdict(list)
    collect['first'] = list(n_1)
    collect['second'] = list(n_2)
    return f'Сумма чисел {str(collect["first"]).upper()} и {str(collect["second"]).upper()} =' \
           f' {list(hex(reduce(lambda x, y: x + y, [int("".join(i), 16) for i in collect.values()]))[2:].upper())}\n' \
           f'Произведение чисел {str(collect["first"]).upper()} и {str(collect["second"]).upper()} = ' \
           f'{list(hex(reduce(lambda x, y: x * y, [int("".join(i), 16) for i in collect.values()]))[2:].upper())}'


# Вариант_3 "namedtuple"
def hex_tuple(n_1, n_2):
    collect = namedtuple('hex_tuple', 'numb')
    first = collect(numb=list(n_1))
    second = collect(numb=list(n_2))
    summ = hex(int(''.join(first.numb), 16) + int(''.join(second.numb), 16))
    mult = hex(int(''.join(first.numb), 16) * int(''.join(second.numb), 16))
    return f'Сумма чисел {first.numb} и {second.numb} = {list(summ.upper())[2:]}\n' \
           f'Произведение чисел {first.numb} и {second.numb} = {list(mult.upper())[2:]}'


# Вариант_3 ООП
class CalcHex:
    def __init__(self, number):
        self.number = number

    def __add__(self, second):
        return hex(int(self.number, 16) + int(second.number, 16)).upper()[2:]

    def __mul__(self, second):
        return hex(int(self.number, 16) * int(second.number, 16)).upper()[2:]


if __name__ == '__main__':
    input_number_1 = input(f'Введите первое шестнадцатеричное число: ')
    input_number_2 = input(f'Введите второе шестнадцатеричное число: ')
    print(f'{"*" * 25} Первый вариант "defaultdict" {"*" * 25}')
    print(hex_result(input_number_1, input_number_2))
    print(f'{"*" * 25} Второй вариант "defaultdict" {"*" * 25}')
    print(hex_reduce(input_number_1, input_number_2))
    print(f'{"*" * 25} Третий вариант "namedtuple" {"*" * 25}')
    print(hex_tuple(input_number_1, input_number_2))
    print(f'{"*" * 35} ООП {"*" * 35}')
    print(f"Сумма чисел {list(CalcHex(input_number_1) + CalcHex(input_number_2))}")
    print(f"Произведение чисел  {list(CalcHex(input_number_1) * CalcHex(input_number_2))}")
