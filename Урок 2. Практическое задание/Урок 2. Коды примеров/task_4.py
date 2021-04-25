"""Конвертация"""

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())


def convert_to_str(n, base_val):
    convert_str = "0123456789ABCDEF"
    # Базовый случай, в котором n должно быть меньше,
    # чем основание, по которому мы конвертируем
    if n < base_val:
        return convert_str[n]
    # Здесь выполняются 2-й и 3-й законы рекурсии
    # выполняется рекурсивный вызов и происходит
    # уменьшение размера задания с помощью деления
    else:
        return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]


print(convert_to_str(5, 2))
print(convert_to_str(10, 16))

# convert_to_str(5, 2)
# convert_to_str(2, 2) + 1
# convert_to_str(1, 2) + 0
# convert_to_str(1, 2) -> 1

# все!

# 1 + 0
# 1 + 0 + 1
# 101

