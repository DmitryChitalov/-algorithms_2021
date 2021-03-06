"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import memory_usage
from timeit import default_timer
from functools import reduce
from pympler import asizeof
from collections import namedtuple
from recordclass import recordclass


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()

        res = func(*args)

        m2 = memory_usage()
        t2 = default_timer()
        print(f'Программа занимает {m2[0] - m1[0]} памяти и выполняется за время {t2 - t1}')
        return res
    return wrapper


"""
№ 1. Условие 
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
"""


@decor
def binary_array_to_number(arr):
    arr = [str(el) for el in arr]
    return int(''.join(arr), 2)


@decor
def binary_array_to_number_optim(arr):
    return int(''.join(map(str, arr)), 2)


print('Задача 1')
print('Для исходного варианта:')
binary_array_to_number([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1])  # -> 0.00390625 Mib и 0.10078006 с
print('Для оптимизированного варианта:')
binary_array_to_number_optim([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1])   # -> 0.0 Mib и 0.10070126900000004 с
print()

'''
Встроенная функция map существенно сократила расход памяти. 
'''

"""
№ 2. Условие:

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то
получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""


@decor
def max_num(max_number):
    numbers = []
    for number in range(max_number):
        if number % 3 == 0 or number % 5 == 0:
            numbers.append(number)
    return sum(numbers)


@decor
def max_num_optim(max_number):
    gen_el = (el for el in range(max_number) if el % 3 == 0 or el % 5 == 0)
    return reduce(lambda a, b: a + b, gen_el)


print('Задача 2')
print('Для исходного варианта:')
max_num(10000000)  # -> 0.3984375 Mib и 2.122513316
print('Для оптимизированного варианта:')
max_num_optim(10000000)  # -> 0.0 Mib и 2.2468729599999997
print()
'''
В данном случае для оптимизации мы применили "ленивые вычисления", а именно генератор. 
Благодаря тому, что в оптимизированном варианте в памяти не хранится весь список, 
расход памяти существенно снизился.
'''


"""
№ 3. Условие:
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

"""


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}i'
        else:
            return f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


class ComplexNumberOptimize:
    __slots__ = ['re', 'im']

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f'{self.re} + {self.im}i'
        else:
            return f'{self.re} - {abs(self.im)}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)


print('Задача 3')
num1 = ComplexNumber(5, 6)
print(num1.__dict__)
print('Размер объекта класса в случае с динамическим словарем:', asizeof.asizeof(num1))  # -> 184

num1 = ComplexNumberOptimize(5, 6)
print(num1.__slots__)
print('Размер объекта класса в случае со слотами:', asizeof.asizeof(num1))  # -> 56
print()
'''
В результате замеров видим, что размер объекта класса при использовании слотов в данном 
случае оказался более чем в 3 раза меньше.
'''


"""
№ 4. 
Задача 1 из урока 5 по данному курсу, немного измененная

Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


@decor
def middle_profit(n):
    list_of_firms = []
    sum_profit = 0

    number_of_firms = n

    for firm in range(number_of_firms):
        name = f'firm_{firm}'
        profit = '45542656464 2346363336 2344446233634536436 24652363453'.split()

        Profit_quartals = namedtuple('по_кварталам', 'кв_1 кв_2 кв_3 кв_4')
        quartals = Profit_quartals(*profit)
        mid_profit = round(sum(map(int, profit)) / 4, 2)
        sum_profit += mid_profit
        Firms = namedtuple(name, 'прибыль средняя_прибыль')
        firm_i = Firms(quartals, mid_profit)
        list_of_firms.append(firm_i)
    total_middle_profit = round(sum_profit / number_of_firms, 2)

    print(f'Средняя годовая прибыль всех предприятий: {total_middle_profit}')

    higher_middle_firms = []
    lower_middle_firms = []
    for el in list_of_firms:
        if el.средняя_прибыль >= total_middle_profit:
            higher_middle_firms.append(el)
        else:
            lower_middle_firms.append(el)
    return higher_middle_firms, lower_middle_firms



@decor
def middle_profit_optim(n):
    list_of_firms = []
    sum_profit = 0

    number_of_firms = n

    for firm in range(number_of_firms):
        name = f'firm_{firm}'
        profit = '45542656464 2346363336 2344446233634536436 24652363453'.split()

        Profit_quartals = recordclass('по_кварталам', 'кв_1 кв_2 кв_3 кв_4')
        quartals = Profit_quartals(*profit)
        mid_profit = round(sum(map(int, profit)) / 4, 2)
        sum_profit += mid_profit
        Firms = recordclass(name, 'прибыль средняя_прибыль')
        firm_i = Firms(quartals, mid_profit)
        list_of_firms.append(firm_i)
    total_middle_profit = round(sum_profit / number_of_firms, 2)

    print(f'Средняя годовая прибыль всех предприятий: {total_middle_profit}')

    higher_middle_firms = []
    lower_middle_firms = []
    for el in list_of_firms:
        if el.средняя_прибыль >= total_middle_profit:
            higher_middle_firms.append(el)
        else:
            lower_middle_firms.append(el)
    return higher_middle_firms, lower_middle_firms


print('Задача 4')
middle_profit(3000)  # -> 23.62109375 Mib и 0.5623322850000001 с
middle_profit_optim(3000)  # -> 12.5078125 Mib и 0.5873320990000002 с

'''
Программа с использованием модуля recordclass по сравнению с namedtuple в данном случае 
оказалась почти в два раза экономичнее по занимаемой памяти
'''
