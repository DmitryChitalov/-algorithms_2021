from collections import defaultdict


def hex_sum(dic):
    res = 0
    for key in dic.keys():
        res += int(key, 16)
    return hex(res)[2:]


def hex_mul(dic):
    res = 1
    for key in dic.keys():
        res *= int(key, 16)
    return hex(res)[2:]


num_1 = input("Введите первое шестнадцатеричное число: ")
num_2 = input("Введите второе шестнадцатеричное число: ")
nums = defaultdict(list)
nums[num_1] = list(num_1)
nums[num_2] = list(num_2)
print(f'Сумма чисел: {list(hex_sum(nums).upper())}')
print(f'Произведение чисел: {list(hex_mul(nums).upper())}')

# OOП


class HexNumber:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))


num_1 = HexNumber(input("Введите первое шестнадцатеричное число: "))
num_2 = HexNumber(input("Введите второе шестнадцатеричное число: "))
print(f'Сумма чисел : {list(str(num_1 + num_2).upper())}')
print(f'Произведение чисел: {list(str(num_1 * num_2).upper())}')
