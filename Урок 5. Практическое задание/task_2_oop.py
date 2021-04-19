class HexNumber:
    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __add__(self, other):
        hex_sum = hex(int(self.hex_number, 16) + int(other.hex_number, 16))
        return str(hex_sum)[2:].upper()

    def __mul__(self, other):
        hex_mul = hex(int(self.hex_number, 16) * int(other.hex_number, 16))
        return str(hex_mul)[2:].upper()

    def __str__(self):
        return self.hex_number


if __name__ == "__main__":
    num_1 = HexNumber('A2')
    num_2 = HexNumber('C4F')

    print(f'{num_1} + {num_2} =', num_1 + num_2)
    print(f'{num_1} * {num_2} =', num_1 * num_2)
