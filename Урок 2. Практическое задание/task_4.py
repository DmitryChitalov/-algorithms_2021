def sum_dev(n):
    if n == 1:
        return n
    else:
        if n % 2 == 0:
            return (-(1 / 2 ** (n - 1))) + sum_dev(n - 1)
        else:
            return 1 / 2 ** (n - 1) + sum_dev(n - 1)


elem_count = int(input('Введите количество элементов: '))
print(sum_dev(elem_count))
print(sum_dev(3))
print(sum_dev(4))
