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
from memory_profiler import profile


# Вариант 1 с использованием collections
def get_int_from_16(lst):
    lst.reverse()
    lst = deque(lst)
    list_of_numbers = deque([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])
    number = deque()
    for i in range(len(lst)):
        if lst[i] == '1' and len(lst) == 1:
            number.append(list_of_numbers.index(lst[i]) * (16 ** i))
        elif lst[i] == '1' and lst[i + 1] == '0':
            number.append(16)
        else:
            number.append(list_of_numbers.index(lst[i]) * (16 ** i))
    return sum(number)


def calc_hex():
    num_1 = get_int_from_16(deque(input('Введите первое число в шестнадцатиричном формате: \n').upper()))
    num_2 = get_int_from_16(deque(input('Введите второе число в шестнадцатиричном формате: \n').upper()))
    oper = input('Укажите оператор "*" или "+": \n')
    operations = {'+': num_1 + num_2, '*': num_1 * num_2}
    result = operations.get(oper)
    print(hex(result).strip('0x'))


calc_hex()


# Вариант 2 С использованием встроенных инструментов
@profile
def calc_hex_2():
    num_1 = int(input('Введите первое число в шестнадцатиричном формате: \n'), 16)
    num_2 = int(input('Введите второе число в шестнадцатиричном формате: \n'), 16)
    oper = input('Укажите оператор "*" или "+": \n')
    operations = {'+': num_1 + num_2, '*': num_1 * num_2}
    result = operations.get(oper)
    print(hex(result).strip('0x'))


calc_hex_2()


"""
Результаты замера времени выполнения:
Выремя выполнения функции calc_hex_2(): 0.004190600000000003
Выремя выполнения функции calc_hex(): 0.0649981
"""