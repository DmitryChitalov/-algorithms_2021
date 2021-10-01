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

BASE16 = 16


class Hexnumber:
    def __init__(self, first: str):
        self.first = int(first, BASE16)

    def __add__(self, other):
        # return '%X' % (self.first+other.first)
        return f'{[*("%X" % (self.first + other.first))]}'

    def __mul__(self, other):
        # return '%X' % (self.first*other.first)
        return f'{[*("%X" % (self.first * other.first))]}'

    def __str__(self):
        return f'{[*("%X" % self.first)]}'


class Hexnumber2:
    def __init__(self, first):
        self.first = list(first)

    def __add__(self, other):
        return list("%X" % (int(''.join(self.first), BASE16) + int(''.join(other.first), BASE16)))

    def __mul__(self, other):
        return list("%X" % (int(''.join(self.first), BASE16) * int(''.join(other.first), BASE16)))

    def __str__(self):
        return f'{self.first}'


class Hexnumber3:
    def l_to_num(self, l):
        return int(''.join(l), BASE16)

    def __init__(self, first):
        self.first = list(first)

    def __add__(self, other):
        return list("%X" % (self.l_to_num(self.first) + self.l_to_num(other.first)))

    def __mul__(self, other):
        return list("%X" % (self.l_to_num(self.first) * self.l_to_num(other.first)))

    def __str__(self):
        return f'{self.first}'


def main1():
    x = Hexnumber('A2')
    y = Hexnumber('C4F')
    print('x,y:', x, y)
    print('x+y:', x + y)
    print('x*y:', x * y)
    x += y
    print('x (x+=y):', x)


def main2():
    x = Hexnumber2('A2')
    y = Hexnumber2('C4F')
    print('x,y:', x, y)
    print('x+y:', x + y)
    print('x*y:', x * y)
    x += y
    print('x (x+=y):', x)


def main3():
    x = Hexnumber3('A2')
    y = Hexnumber3('C4F')
    print('x,y:', x, y)
    print('x+y:', x + y)
    print('x*y:', x * y)
    x += y
    print('x (x+=y):', x)


if __name__ == '__main__':
    print(str.center('HEXNUMBER нелаконичный', 40, '*'))
    main1()
    print(str.center('HEXNUMBER2 лаконичный', 40, '*'))
    main2()
    print(str.center('HEXNUMBER3 соответствует ТЗ', 40, '*'))
    main3()
    exit(0)

'''
*********HEXNUMBER нелаконичный*********
x,y: ['A', '2'] ['C', '4', 'F']
x+y: ['C', 'F', '1']
x*y: ['7', 'C', '9', 'F', 'E']
x (x+=y): ['C', 'F', '1']
*********HEXNUMBER2 лаконичный**********
x,y: ['A', '2'] ['C', '4', 'F']
x+y: ['C', 'F', '1']
x*y: ['7', 'C', '9', 'F', 'E']
x (x+=y): ['C', 'F', '1']
******HEXNUMBER3 соответствует ТЗ*******
x,y: ['A', '2'] ['C', '4', 'F']
x+y: ['C', 'F', '1']
x*y: ['7', 'C', '9', 'F', 'E']
x (x+=y): ['C', 'F', '1']

выводы:
1. для данного решения найти какие типы из collections применить мне не удалось.
- Counter - подсчитывать нечего
- deque - задач стека и очереди не стоит
- namedtuple - сильно усложняет алгоритм
- defaultdict - не требуется словарь
- OrderedDict - тоже не требуется словарь
2. не для всех решений требуются типы collections
3. ряд решений довольно легко получаются из стандартных типов питон

'''
