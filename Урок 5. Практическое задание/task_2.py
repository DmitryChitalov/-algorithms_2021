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

from functools import reduce
from collections import defaultdict

translator = defaultdict(int)
for i in '0123456789ABCDEF':
    translator[i] += int(i, 16)

first_number = list(input('Введите первое число в 16-ричной системе счисления: ').upper())
second_number = list(input('Введите второе число в 16-ричной системе счисления: ').upper())

print('Введенные числа:', first_number, second_number)

# Даже без функции list строка является последовательностью, по ней можно итерироваться и пр.
# Но раз написано, хранить в списке, храним в списке)

first_number.reverse()
second_number.reverse()

# Чтобы не усложнять, во всех вариантах кроме третьего работаем с развернутыми списками.

######################################### 1 вариант #########################################

print('**************************************** Вариант 1 ****************************************\n')


def my_func_for_reduce(my_sum, el):
    return my_sum + el


first_number_in_dec = reduce(my_func_for_reduce,
                             [translator[first_number[i]] * 16 ** i for i in range(len(first_number))])
second_number_in_dec = reduce(my_func_for_reduce,
                              [translator[second_number[i]] * 16 ** i for i in range(len(second_number))])

my_sum_in_dec = first_number_in_dec + second_number_in_dec
my_product_in_dec = first_number_in_dec * second_number_in_dec


def my_hex(number):
    answer = []
    while number:
        r = number % 16
        for i in translator:
            if translator[i] == r:
                answer.append(i)
        number //= 16
    answer.reverse()
    return answer


print('Сумма чисел из примера:', my_hex(my_sum_in_dec))
print('Произведение чисел из примера:', my_hex(my_product_in_dec), '\n')

######################################### 2 вариант #########################################

print('**************************************** Вариант 2 ****************************************\n')


#  translator создавался как defaultdict, чтобы была использована коллекция из модуля collections.
#  Его так же легко сделать не прибегая к этоу структуре. Так что это решение вроде как удовлетворяет условию решения
#  без collections.

class HexNumber:
    def __init__(self, number):
        self.number = number

    def number_to_dec(self):
        return reduce(my_func_for_reduce,
                      [translator[self.number[i]] * 16 ** i for i in range(len(self.number))])

    def __add__(self, other):
        return list(str(hex(self.number_to_dec() + other.number_to_dec())).upper())[2:]

    def __mul__(self, other):
        return list(str(hex(self.number_to_dec() * other.number_to_dec())).upper())[2:]


new_first_number = HexNumber(first_number)
new_second_number = HexNumber(second_number)

print('Сумма чисел из примера:', new_first_number + new_second_number)
print('Произведение чисел из примера:', new_first_number * new_second_number, '\n')

######################################### 3 вариант #########################################

#  Руки чешутся сделать вот так, но кажется, все же не совсем это требуется)

print('**************************************** Вариант 3 ****************************************\n')

first_number.reverse()
second_number.reverse()

print('Сумма чисел из примера:',
      list(str(hex(int(''.join(first_number), 16) + int(''.join(second_number), 16))).upper())[2:])
print('Произведение чисел из примера:',
      list(str(hex(int(''.join(first_number), 16) * int(''.join(second_number), 16))).upper())[2:])
