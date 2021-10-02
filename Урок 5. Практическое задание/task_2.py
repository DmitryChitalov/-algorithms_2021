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
from collections import deque


def calculator():
    try:
        request1 = input('Введите число в шеснацетиричном формате:')
        request2 = input('Введите число в шеснацетиричном формате:')
        dec_request1 = deque([i for i in request1])
        print(dec_request1)
        dec_request2 = deque([i for i in request2])
        print(dec_request2)
        int_total_sum = format(int(request2, 16) + int(request1, 16), 'x')
        int_product_num = format(int(request2, 16) * int(request1, 16), 'x')
        total_sum = deque([i for i in int_total_sum])
        product_num = deque([i for i in int_product_num])
        print(f'Сумма чисел: {total_sum}')
        print(f'Произведение чисел: {product_num}')
    except:
        print('Не правильный ввод')
