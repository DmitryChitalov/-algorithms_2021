"""
Создание слотов для класса комплексных чисел с курса основ.
Аналогично классу шестнадцатиричных чисел,
замеры показывают выигрыш в размере экземпляра класса
со слотами и уменьшение памяти, затрачиваемой на
его создание.

Функция __init__ (ComplexNumber):
Время выполнения: 0.21662749999999997 сек.
Использованная память: 0.00390625 Mib.

Функция __init__ (ComplexNumberSlot):
Время выполнения: 0.21972670000000005 сек.
Использованная память: 0.0 Mib.

Размер класса ComplexNumber 328 байт.
Размер класса ComplexNumberSlot 112 байт.
"""

from pympler.asizeof import asizeof
from task_1 import time_memo_prof


class ComplexNumber:

    @time_memo_prof
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)


class ComplexNumberSlot:

    __slots__ = ('real', 'imag')

    @time_memo_prof
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}+{self.imag}i"

    def __add__(self, other):
        if not isinstance(other, ComplexNumberSlot):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumberSlot):
            raise ValueError("Operand is not ComplexNumber")
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)


if __name__ == '__main__':

    c1 = ComplexNumber(2, 4)
    c2 = ComplexNumberSlot(2, 4)
    print(f'Размер класса ComplexNumber {asizeof(c1)} байт.')
    print(f'Размер класса ComplexNumberSlot {asizeof(c2)} байт.')
