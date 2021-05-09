"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexNumber:
    __DIGITS = '0123456789ABCDEF'

    def __init__(self, string):
        self.digit_list = []
        for ch in string.upper():
            if ch in self.__DIGITS:
                self.digit_list.append(ch)
            else:
                raise ValueError('Недопустимое шестнадцатиричное чисело')

    def __add__(self, other):
        if not isinstance(other, HexNumber):
            raise TypeError(f"unsupported operand type(s) for +: 'HexNumber' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 + num_2)
        return HexNumber(res[2:])

    def __mul__(self, other):
        if not isinstance(other, HexNumber):
            raise TypeError(f"unsupported operand type(s) for *: 'HexNumber' and {type(other)}")

        num_1 = int(''.join(self.digit_list), 16)
        num_2 = int(''.join(other.digit_list), 16)
        res = hex(num_1 * num_2)
        return HexNumber(res[2:])

    def __repr__(self):
        return f'HexNumber {self.digit_list}'

    def __str__(self):
        return str(self.digit_list)


if __name__ == '__main__':
    try:
        n1 = HexNumber(input('Введите первое 16-ричное число: '))
        n2 = HexNumber(input('Введите второе 16-ричное число: '))
    except ValueError:
        print('Неверный ввод.')
    else:
        print(f'Сумма введённых чисел: {n1 + n2}\n'
              f'Произведение введённых чисел: {n1 * n2}')
