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


# Начнем с ООП, это мне представляется гораздо более простым заданием

class HexNumber:  # hex() я не буду пользоваться из-за лидирующих 0x. Их можно убрать, но так проще. Можно и f-строки
    # тоже.

    def __init__(self, num):
        self.num = int(num, 16)

    def __add__(self, other):
        return format(self.num + other.num, 'X')

    def __mul__(self, other):
        return format(self.num * other.num, 'X')  # Вывод не тот, что запрошен в ТЗ, но сделать его - добавление
        # одной операции, list(string). Просто это не очень красиво. Будет так
        # return list(format(self.num * other.num, 'X')) - для умножения, аналогично для сложения


# Предлагаю рекурсию, это интересный алгоритм преобразования чисел

def conv_hex_to_dec(one, rank=0, list_of_dec=None):
    if list_of_dec is None:
        list_of_dec = []
    list_of_match = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if len(one) == 1:
        list_of_dec.append(list_of_match.index(one[0]) * 16 ** rank)
    else:
        conv_hex_to_dec(one.pop(), rank, list_of_dec)
        rank += 1
        conv_hex_to_dec(one, rank, list_of_dec)
    return sum(list_of_dec)  # Вывод не в list, но это легко, выше показано, как


def conv_dec_to_hex(two, list_of_rems=None):
    list_of_match = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if list_of_rems is None:
        list_of_rems = []
    if not two // 16:
        list_of_rems.append(list_of_match[two])
    else:
        list_of_rems.append(list_of_match[two % 16])
        conv_dec_to_hex(two // 16, list_of_rems)
    return ''.join(reversed(list_of_rems))  # Вывод не в list, но это легко - просто убрать join


# По условию задания требуется использование коллекции из соотсветствующего модуля. Не ясно, для чего, честно сказать,
# но пусть будет например вот так(для демонстрации возможностей, наверное)


def try_with_coll(one, two):
    hex_dict = defaultdict(list)
    hex_dict[one] = list(one)
    hex_dict[two] = list(two)
    _sum = format(int(one, 16) + int(two, 16), 'X')
    _mul = format(int(one, 16) * int(two, 16), 'X')
    hex_dict[_sum] = list(_sum)
    hex_dict[_mul] = list(_mul)
    print(f'Сумма равна: {hex_dict[_sum]}')                   # Тут решил оставить вывод как в условии
    print(f'Произведение равно: {hex_dict[_mul]}')            # Тут решил оставить вывод как в условии


if __name__ == '__main__':
    a = HexNumber('A2')
    b = HexNumber('C4F')
    print(a + b, a * b)
    c = conv_hex_to_dec(list(input('Введите число в шестнадцатеричном формате: ')))
    d = conv_hex_to_dec(list(input('Введите число в шестнадцатеричном формате: ')))
    print(conv_dec_to_hex(c + d), conv_dec_to_hex(c * d))
    try_with_coll(input('Введите число в шестнадцатеричном формате: '), input('Введите число в шестнадцатеричном '
                                                                              'формате: '))
