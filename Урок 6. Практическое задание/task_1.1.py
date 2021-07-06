from memory_profiler import profile


@profile
def var_1():
    class HexOperation:
        def __init__(self, a, b):
            self.a = list(a)
            self.b = list(b)

        def __add__(self, other):
            return list(hex(int(''.join(self.a), 16) + int(''.join(other.b), 16)))[2:]

        def __mul__(self, other):
            return list(hex(int(''.join(self.a), 16) * int(''.join(other.b), 16)))[2:]

    num_1 = input('Введите первое число в шестнадцатиричном формате: ')
    num_2 = input('Введите второе число в шестнадцатиричном формате: ')

    summa = HexOperation(num_1, num_2) + HexOperation(num_1, num_2)
    mul = HexOperation(num_1, num_2) * HexOperation(num_1, num_2)

    print(f'Сумма чисел составляет: {summa}')
    print(f'Произведение чисел: {mul}')


@profile
def var_2():
    class HexOperation:
        __slots__ = ('a', 'b')

        def __init__(self, a, b):
            self.a = list(a)
            self.b = list(b)

        def __add__(self, other):
            return list(hex(int(''.join(self.a), 16) + int(''.join(other.b), 16)))[2:]

        def __mul__(self, other):
            return list(hex(int(''.join(self.a), 16) * int(''.join(other.b), 16)))[2:]

    num_1 = input('Введите первое число в шестнадцатиричном формате: ')
    num_2 = input('Введите второе число в шестнадцатиричном формате: ')

    summa = HexOperation(num_1, num_2) + HexOperation(num_1, num_2)
    mul = HexOperation(num_1, num_2) * HexOperation(num_1, num_2)

    print(f'Сумма чисел составляет: {summa}')
    print(f'Произведение чисел: {mul}')


var_1()
var_2()

"""
результаты не изменились, т.к. очень небольшой объем данных, при большем объеме слоты будут занимать меньше памяти,
т.к. не будет использоваться словарь для хранения аттрибутов класса
"""