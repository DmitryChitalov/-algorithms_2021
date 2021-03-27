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
# я решила использовать deque, надеюсь, такой вид хранения соответствует условиям задачи

from collections import deque

first_num = deque(input('Введите первое число: '))
second_num = deque(input('Введите второе число: '))

str_first_num = ''
str_second_num = ''

while first_num:
    str_first_num += first_num.popleft()

while second_num:
    str_second_num += second_num.popleft()


hex_sum = hex(int(str_first_num, 16) + int(str_second_num, 16))

list_sum = list(str(hex_sum)[2:].upper())

print(f'Сумма чисел из примера: {list_sum}')

hex_mul = hex(int(str_first_num, 16) * int(str_second_num, 16))
list_mul = list(str(hex_mul)[2:].upper())
print(f'Произведение - {list_mul}')
