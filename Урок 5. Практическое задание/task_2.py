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

d = defaultdict(list)


def add_dict(*args):
    for i in args:
        d[i] = [v for v in i]


def my_func(numb_1, numb_2):
    try:
        sum_numb = hex(int(numb_1, 16) + int(numb_2, 16)).upper()[2:]
        multi_numb = hex(int(numb_1, 16) * int(numb_2, 16)).upper()[2:]
        add_dict(numb_1, numb_2, sum_numb, multi_numb)
        return sum_numb, multi_numb
    except ValueError:
        print('Вы ввели не коректные данные')


numb_1 = input('Введите первое число 16 системы исчесления: ')
numb_2 = input('Введите первое число 16 системы исчесления: ')
result = my_func(numb_1, numb_2)
try:
    print(
        f'Сохраненные числа {d[numb_1]} и {d[numb_2]}\nИх сумма {result[0]} и сохранена как {d[result[0]]}\n'
        f'Их произведение {result[1]} и сохронены как {d[result[1]]}')
except TypeError:
    print('Вывод данных не возможен так как введены не коректные данные!')

print('\n' + '-' * 20 + '\n')


class MyClass:

    def __init__(self, numb):
        self.numb = numb

    def __str__(self):
        return f'{self.numb}'

    def __add__(self, other):
        try:
            return hex(int(self.numb, 16) + int(other.numb, 16)).upper()[2:]
        except ValueError:
            print("Вы ввели не коректные данные")
            return ''

    def __mul__(self, other):
        try:
            return hex(int(self.numb, 16) * int(other.numb, 16)).upper()[2:]
        except ValueError:
            print("Вы ввели не коректные данные")
            return ''


z = MyClass(input('Введите первое число 16 системы исчесления: '))
c = MyClass(input('Введите первое число 16 системы исчесления: '))
print('Сложение через классы', z + c)
print('Умножение чепез классы', z * c)
