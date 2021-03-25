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


def calc(num_1, num_2):
    operations_result = defaultdict(list)
    operations_result['number_1'] = list(num_1)
    operations_result['number_2'] = list(num_2)
    operations_result['add'] = list(hex(int(num_1, 16) + int(num_2, 16))[2:])
    operations_result['mul'] = list(hex(int(num_1, 16) * int(num_2, 16))[2:])

    print(f'первое число: {operations_result["number_1"]} \nвторое число: {operations_result["number_2"]}')
    print(f'результат сложения: {operations_result["add"]} \nрезультат умножения: {operations_result["mul"]}')


class HexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return list(hex(int(self.number, 16) + int(other.number, 16))[2:])

    def __mul__(self, other):
        return list(hex(int(self.number, 16) * int(other.number, 16))[2:])

    def __str__(self):
        return f'{list(self.number)}'


first_number = input('Введите первое чило в 16 сс: ')
second_number = input('Введите второе чило в 16 сс: ')
calc(first_number, second_number)

first_hex_num = HexNumber(first_number)
second_hex_num = HexNumber(second_number)
print(f'первое число: {first_hex_num} \nвторое число: {second_hex_num}')
print(f'результат сложения: {first_hex_num + second_hex_num} \nрезультат умножения: {first_hex_num * second_hex_num}')
