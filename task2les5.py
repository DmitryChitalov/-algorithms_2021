from collections import defaultdict
from functools import reduce

new_dict = defaultdict(list)

new_dict.update({'первое число': list('A2')})
new_dict.update({'второе число': list('C4F')})

add1 = list(hex(sum([int(''.join(i), 16) for i in new_dict.values()])))
mul2 = list(hex(reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in new_dict.values()])))

print("Рещультат сложения: ", add1[2:])
print("Результат произведения: ", mul2[2:])