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


class Overload:

    def __init__(self, hex_list):
        self.num = int(''.join(hex_list), 16)

    def __add__(self, other):
        return hex(self.num + other.num)

    def __mul__(self, other):
        return hex(self.num * other.num)


def integral_func(numbers):
    num_1 = ''.join(numbers[0])
    num_2 = ''.join(numbers[1])
    sum_hex = int(num_1, 16) + int(num_2, 16)
    mul_hex = int(num_1, 16) * int(num_2, 16)
    return hex(sum_hex), hex(mul_hex)


def hex_dict(hex_list):
    hex_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    num = defaultdict(str)
    for i in hex_list:
        if i.isalpha() and i in hex_dict:
            num[i] = hex_dict[i]
        elif i.isdigit():
            num[i] = int(i)
    return num


def default_dict(numbers):
    num_1 = hex_dict(numbers[0])
    list_val = [val for val in num_1.values()][::-1]
    num_dec_1 = sum([list_val[i] * 16 ** i for i in range(len(list_val))])

    num_2 = hex_dict(numbers[1])
    list_val = [val for val in num_2.values()][::-1]
    num_dec_2 = sum([list_val[i] * 16 ** i for i in range(len(list_val))])

    sum_hex = num_dec_1 + num_dec_2
    mul_hex = num_dec_1 * num_dec_2
    return hex(sum_hex), hex(mul_hex)


if __name__ == '__main__':
    hex_simbol = '0123456789abcdef'
    while True:
        numbers_list = []
        print('=' * 50)
        print('Для выхода введите "q"')
        num1 = input('Введите первое шестнадцетиричное число: ')
        if num1 == "q":
            print('Выход')
            break
        num2 = input('Введите второе шестнадцетиричное число: ')
        if num2 == "q":
            print('Выход')
            break

        numbers_list.append([x for x in num1])
        numbers_list.append([x for x in num2])

        try:
            for i in range(2):
                for j in numbers_list[i]:
                    if j not in hex_simbol:
                        raise Exception('Введенное число не соответствует параметрам!!!')
                    break
        except Exception as e_hex:
            print(e_hex)
            continue

        a = Overload(numbers_list[0])
        b = Overload(numbers_list[1])

        print('-' * 20, 'Сложение', '-' * 20)
        print(f'Встроенные функции          : {integral_func(numbers_list)[0][2:].upper()}')
        print(f'С использованием defaultdict: {default_dict(numbers_list)[0][2:].upper()}')
        print(f'Перегрузка операторов       : {(a + b)[2:].upper()}')

        print('-' * 20, 'Умножение', '-' * 20)
        print(f'Встроенные функции          : {integral_func(numbers_list)[1][2:].upper()}')
        print(f'С использованием defaultdict: {default_dict(numbers_list)[1][2:].upper()}')
        print(f'Перегрузка операторов       : {(a * b)[2:].upper()}')







