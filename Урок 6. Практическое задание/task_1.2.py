
'''
Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''


from memory_profiler import profile
from functools import reduce


N1 = '276C66'
N2 = '168967016E6'
print(f'Первое число: {list(N1)}')
print(f'Второе число: {list(N2)}')
print()

# Решение задачи через функцию
print('Первая реализация ЗАДАЧИ №2')


@profile
def my_func_1():
    def int16(num):
        my_str = ''
        for el in range(len(num)):
            my_str = my_str + num[el]
        return int(my_str, 16)

    sum_all = [el for el in format((reduce(lambda x, y: x + y, [int16(N1), int16(N2)])), 'X')]
    mul_all = [el for el in format((reduce(lambda x, y: x * y, [int16(N1), int16(N2)])), 'X')]
    print(f'Сумма чисел         => {sum_all}')
    print(f'Произведение чисел  => {mul_all}')


my_func_1()


# Решение задачи через функцию
print('Вторая реализация ЗАДАЧИ №2')


@profile
def my_func_2():
    print(f'Сумма чисел         => {list(format((int(N1, 16) + int(N2, 16)), "X"))}')
    print(f'Произведение чисел  => {list(format((int(N1, 16) * int(N2, 16)), "X"))}')


my_func_2()


# Решение задачи через ООП
print('Третья реализация ЗАДАЧИ №2')


@profile
def my_class():
    class MyClass:
        def __init__(self, num):
            self.num = num

        def __add__(self, other):
            return MyClass(format((self.num + other.num), 'X'))

        def __mul__(self, other):
            return MyClass(format((self.num * other.num), 'X'))

        def __str__(self):
            return f'{list(self.num)}'


    N_1 = MyClass(int(N1, 16))
    N_2 = MyClass(int(N2, 16))
    print(f'Сумма чисел         => {N_1+N_2}')
    print(f'Произведение чисел  => {N_1*N_2}')


my_class()
'''
    Замеры используемой памяти показывают, что для сложения двух чисел задействуется одинаковое количество памяти.
Память выделяется для запоминания двух объектов (суммы и произведения) в любом варианте решения задачи. Оптимизации
не нужна...
'''
