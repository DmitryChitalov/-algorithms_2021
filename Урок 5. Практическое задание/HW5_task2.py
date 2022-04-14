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
import collections

def calc():
    nums = collections.defaultdict(list)

    i = 1
    while i < 3:
        n = input(f"Введите {i}-е натуральное шестнадцатиричное число: ")
        nums[int(n, 16)] = list(n)
        i += 1
    sum_current = hex(sum(nums))
    print(f'Сумма чисел : {sum_current}')

    mul_curr = 1
    for num in nums:
        mul_curr = mul_curr * num
    mul_curr = hex(mul_curr)
    print(f'Произведение чисел: {mul_curr} ')


calc()


class Hex_Calculator:
    def __init__(self, num):
        self.num = int(num,16)

    def __add__(self, other):
        return hex(self.num + other.num)

    def __mul__(self, other):
        return hex(self.num * other.num)


num1 = input('Введите первое шестнадцатиричное число: ')
num2 = input('Введите второе шестнадцатиричное число: ')

number1_hex = Hex_Calculator(num1)
number2_hex = Hex_Calculator(num2)
current_sum = number1_hex + number2_hex
current_mul = number1_hex * number2_hex

print(f'Сумма чисел = {current_sum}\nПроизведение чисел = {current_mul}')


