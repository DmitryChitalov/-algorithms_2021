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

# 1 вариант - Велосипедный

# first_operand_string = input("Введите первое значение: ")
first_operand_string = "A2"
first_operand = defaultdict(int)
for i, k in enumerate(list(first_operand_string)):
    first_operand[i] = k
print(first_operand)

# second_operand_string = input("Введите второе значение: ")
second_operand_string = "C4F"
second_operand = defaultdict(int)
for i, k in enumerate(list(second_operand_string)):
    second_operand[i] = k
print(second_operand)


max_elements = max(len(first_operand), len(second_operand))
reversed_range = reversed(range(max_elements))
for iterator in range(1, max_elements+1):
    print(iterator)
    print(f"{first_operand[len(first_operand) - iterator]} + {second_operand[len(second_operand) - iterator]}")
