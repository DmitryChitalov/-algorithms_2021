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
from functools import reduce

def sum_func():
    def multiply_two(a, b):
        return a * b

    n_dict = defaultdict(list)
    for i in range(1, 3):
        n_dict[i] = input(f'Введите шестнадцатеричное число\n'
                          f'Please enter a hexadecimal number {i}: ').split()
    total_sum = sum([int(''.join(num), 16) for num in n_dict.values()])

    total_multiply_two = reduce(multiply_two, [int(''.join(num), 16) for num in n_dict.values()])

    return f'Сумма двух шестнадцатеричных чисел:\n' \
           f'The sum of two hexadecimal numbers: {list(str(hex(total_sum)[2:]))}\n' \
           f'Произведение двух шестнадцатеричных чисел:\n' \
           f'Product of two hexadecimal numbers: {list(str(hex(total_multiply_two)[2:]))}'


print(sum_func())

'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm5.2.py"
Введите шестнадцатеричное число
Please enter a hexadecimal number 1: A2
Введите шестнадцатеричное число
Please enter a hexadecimal number 2: C4F
Сумма двух шестнадцатеричных чисел:
The sum of two hexadecimal numbers: ['c', 'f', '1']
Произведение двух шестнадцатеричных чисел:
Product of two hexadecimal numbers: ['7', 'c', '9', 'f', 'e']

Process finished with exit code 0

'''
