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

first_number = input('Введите первое шестнадцатиричное число ').upper()
second_number = input('Введите второе шестнадцатиричное число ').upper()

numbers_dict = defaultdict(list)
numbers_dict[first_number] = list(first_number)
numbers_dict[second_number] = list(second_number)

first_number_again = ''.join(numbers_dict[first_number])
second_number_again = ''.join(numbers_dict[second_number])


numbers_sum = hex(int(first_number_again, 16) + int(second_number_again, 16))
numbers_composition = hex(int(first_number_again, 16) * int(second_number_again, 16))

numbers_sum_no_0x = list(numbers_sum.replace('0x', '').upper())
numbers_composition_no_0x = list(numbers_composition.replace('0x', '').upper())


print(f'Введенные числа: {numbers_dict[first_number]} и {numbers_dict[second_number]}')
print(f'Сумма чисел: {numbers_sum_no_0x}')
print(f'Произведение чисел: {numbers_composition_no_0x}')

