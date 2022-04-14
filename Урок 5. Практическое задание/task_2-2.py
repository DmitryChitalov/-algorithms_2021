# -- Вариант 2 для Task 2.

# Создадим класс HexNumber, где будем выполнять все операции по условию задачи

class HexNumber:

    def __init__(self, my_hex):
        self.my_hex = my_hex
        self.int_hex = int(my_hex, 16)

    def __add__(self, other):
        return HexNumber(hex(int(self.my_hex, 16) + int(other.my_hex, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.my_hex, 16) * int(other.my_hex, 16)))

    def __sub__(self, other):
        return HexNumber(hex(int(self.my_hex, 16) - int(other.my_hex, 16)))

    def __str__(self):
        return self.my_hex[2:]


a = HexNumber(input('Введите первое число в шестнадцатеричной системе: '))
b = HexNumber(input('Введите второе число в шестнадцатеричной системе: '))
add = a + b
print(f' Результат сложения: {a.my_hex} + {b.my_hex} = {add.my_hex[2:]}'
      f'  ({a.int_hex} + {b.int_hex} = {add.int_hex})')
mul = a * b
print(f' Результат умножения: {a.my_hex} * {b.my_hex} = {mul.my_hex[2:]}'
      f'  ({a.int_hex} * {b.int_hex} = {mul.int_hex})')
sub = a - b
print(f' Результат вычитания: {a.my_hex} - {b.my_hex} = {sub.my_hex[2:]}'
      f'  ({a.int_hex} + {b.int_hex} = {sub.int_hex})')
