from pympler import asizeof


class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        result = ''
        real = self.re + other.re
        imaginary = self.im + other.im
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Сумма равна: ' + result

    def __mul__(self, other):
        result = ''
        real = self.re * other.re + (- self.im * other.im)
        imaginary = self.re * other.im + self.im * other.re
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Произведение равно: ' + result

    def __str__(self):
        result = ''
        if self.re == 0 and self.im < 0:
            result += f"-j{abs(self.im)}"
        elif self.re == 0 and self.im > 0:
            result += f"j{self.im}"
        elif self.re != 0:
            result += f"{self.re} {'+ j' if self.im > 0 else '- j'}{abs(self.im)}"
        else:
            result = '0'
        return result


a = ComplexNum(123, 234)
print(f"Память, занимаемая объектом класса со словарем: {asizeof.asizeof(a)}")


class ComplexNum:
    __slots__ = ['re', 'im']

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        result = ''
        real = self.re + other.re
        imaginary = self.im + other.im
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Сумма равна: ' + result

    def __mul__(self, other):
        result = ''
        real = self.re * other.re + (- self.im * other.im)
        imaginary = self.re * other.im + self.im * other.re
        if real == 0 and imaginary < 0:
            result += f"-j{abs(imaginary)}"
        elif real == 0 and imaginary > 0:
            result += f"j{imaginary}"
        elif real != 0:
            result += f"{real} {'+ j' if imaginary > 0 else '- j'}{abs(imaginary)}"
        else:
            result = '0'
        return 'Произведение равно: ' + result

    def __str__(self):
        result = ''
        if self.re == 0 and self.im < 0:
            result += f"-j{abs(self.im)}"
        elif self.re == 0 and self.im > 0:
            result += f"j{self.im}"
        elif self.re != 0:
            result += f"{self.re} {'+ j' if self.im > 0 else '- j'}{abs(self.im)}"
        else:
            result = '0'
        return result


a = ComplexNum(1003, 2003)
print(f"Память, занимаемая объектом класса со слотом: {asizeof.asizeof(a)}")

"""
Первый вариант реализации класса - со словарем
Память, занимаемая объектом класса со словарем: 328
Оптимизация состоит в использовании слотов для атрибутов класса
Память, занимаемая объектом класса со слотом: 112
"""