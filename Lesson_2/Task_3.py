def reverse_num(n, rev=''):
    if n == 0:
        return f'Перевернутое число: {rev}'
    n, digit = divmod(n, 10)
    rev += str(digit)
    return reverse_num(n, rev)


print(reverse_num(int(input('Введите число, которое требуется перевернуть: '))))
