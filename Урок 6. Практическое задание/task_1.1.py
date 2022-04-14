from memory_profiler import profile

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

length = 900

# до
@profile
def for_in(length_val):
    elem = 1
    amount = 0
    for i in range(length_val):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length_val} элементов равна {amount}')


for_in(length)

# после
@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)
    print(
        f'Сумма последовательности из {length} элементов равна '
        f'{sum_series_numbers(length)}')


recursion(length)


'''
Исходя из результатов видно, что рекурсия требует больше памяти, 
т.к. при ее работе хранится стек вызовов.
'''
