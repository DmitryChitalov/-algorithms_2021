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

from collections import deque

numbs_dict = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

figureswords_dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def figureswords_to_int(num_toint):
    num_toint = num_toint.copy()
    result_f = 0
    while num_toint:
        result_f += figureswords_dict[num_toint.popleft()] * 16 ** len(num_toint)
    return result_f

def create_num(string):
    deq_list = deque()
    for i in string.upper():
        if i in figureswords_dict:
            deq_list.append(i)
        else:
            raise ValueError('Число неверного формата')
    return deq_list

def add_hex_num(num_1, num_2):
    return int_figureswords(figureswords_to_int(num_1) + figureswords_to_int(num_2))

def mul_hex_num(num_1, num_2):
    return int_figureswords(figureswords_to_int(num_1) * figureswords_to_int(num_2))

def int_figureswords(number):
    result_f = deque()
    while number >= 16:
        number, div = divmod(number, 16)
        result_f.appendleft(numbs_dict[div])
    result_f.appendleft(numbs_dict[number])
    return result_f

if __name__ == '__main__':
    try:
        numb1 = create_num(input('Введите первое число: '))
        numb2 = create_num(input('Введите второе число: '))
    except ValueError:
        print('Что-то пошло не так, повтори')
    else:
        print(f'Сумма чисел: {list(add_hex_num(numb1, numb2))}\n'
              f'Произведение чисел: {list(mul_hex_num(numb1, numb2))}')