import collections
import functools

def calculator():
    numbers = collections.defaultdict(list)
    for i in range(2):
        n = input(f'Введите число номер {i+1}: ')
        numbers[f"{i+1}-{n}"] = list(n)
    print(numbers)

    result1 = sum([int(''.join(i), 16) for i in numbers.values()])
    print("Сумма: ", list('%X' % result1))

    result2 = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение: ", list('%X' % result2))

calculator()


