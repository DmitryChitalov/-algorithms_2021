"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

"""


def fun(n, i=0, j=0):
    if n == 0:
        return i, j
    else:
        n_1 = n % 10
        n = n // 10
        if n_1 % 2 == 0:
            i += 1
        else:
            j += 1
        return fun(n, i, j)


n = int(input("Введите число: "))
print(fun(n))
