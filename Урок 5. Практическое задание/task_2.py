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


alphabet = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

number_1 = list(input('Введите первое число - '))
number_2 = list(input('Введите второе число - '))
nummul1 = number_1
nummul2 = number_2


def number_16_add(number_1, number_2):
    number_2.reverse()
    number_1.reverse()
    if len(number_1) > len(number_2):
        for i in range(len(number_1) - len(number_2)):
            number_2.append('0')
    elif len(number_2) > len(number_1):
        for i in range(len(number_2) - len(number_1)):
            number_1.append('0')

    res = []
    count = len(number_1)
    alphabet_1 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    remains = False

    for i in range(len(number_1)):

        count -= 1

        if number_1[i] in alphabet:
            val_1 = alphabet[number_1[i]]
        else:
            val_1 = int(number_1[i])

        if number_2[i] in alphabet:
            val_2 = alphabet[number_2[i]]
        else:
            val_2 = int(number_2[i])

        if remains is True:
            val_sum = val_1 + val_2 + 1
        else:
            val_sum = val_1 + val_2

        if val_sum <= 9:
            res.append(val_sum)
            remains = False
        elif val_sum < 16:
            res.append(alphabet_1[val_sum])
            remains = False
        else:
            remains = True
            val_sum = val_sum - 16

            if val_sum <= 9:
                res.append(val_sum)
                if count == 0:
                    res.append(1)

            else:
                res.append(alphabet_1[val_sum])
                if count == 0:
                    res.append(1)

    res.reverse()
    return res


def number_16_mul(nummul1, nummul2):
    nummul1_str = ''.join(nummul1)
    nummul1_int = int(nummul1_str, 16)

    nummul2_str = ''.join(nummul2)
    nummul2_int = int(nummul2_str, 16)

    res_int = nummul1_int * nummul2_int
    res_mul = list(hex(res_int))
    res_mul.remove('0')
    res_mul.remove('x')
    return res_mul


class number_16:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.res = number_16_add(self.number, other.number)
        return self.res

    def __mul__(self, other):
        self.res_mul = number_16_mul(self.number, other.number)
        return self.res_mul


test_1 = number_16(number_1)
test_2 = number_16(number_2)

print('Произведение введенных чисел: ', (test_1 * test_2))
print('Сумма введенных чисел: ', (test_1 + test_2))
