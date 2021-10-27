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
"""модуль collections один(!), но решения два. Пока без ООП"""

number = defaultdict(list)
number[1] = list(input('Введите первое число: ').upper())
number[2] = list(input('Введите второе число: ').upper())


def default_dict_1():    # первый вариант решения
    number_one = ''    # создаём новый словарь, с ним у будем работать
    number_two = ''    # создаём новый словарь, с ним у будем работать
    for position, numbers in number.items():
        if position == 1:
            for num in numbers:
                number_one = number_one + num
        if position == 2:
            for num in numbers:
                number_two = number_two + num
    print(f'Сумма чисел {number_one} и {number_two} = '
          f'{hex(int(number_one, 16) + int(number_two, 16))[2:].upper()}')
    print(f'Произведение чисел {number_one} и {number_two} = '
          f'{hex(int(number_one, 16) * int(number_two, 16))[2:].upper()}')


def default_dict_2():    # второй вариант решения (покороче, он не очень то и простой)
    lst_one = list(hex(int("".join(number[1]), 16) + int("".join(number[2]), 16))[2:].upper())
    lst_two = list(hex(int("".join(number[1]), 16) * int("".join(number[2]), 16))[2:].upper())
    # выводим почти как в примере (можно ведь совсем без скобок, как в первом карианте)
    print(f'Сумма чисел {number[1]} и {number[2]} = '
          f'{lst_one}')
    print(f'Произведение чисел {number[1]} и {number[2]} = '
          f'{lst_two}')


default_dict_1()
default_dict_2()

