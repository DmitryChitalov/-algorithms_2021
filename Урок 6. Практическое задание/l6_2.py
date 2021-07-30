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
from time import time
from memory_profiler import memory_usage
from memory_profiler import profile
from collections import namedtuple
from recordclass import recordclass
from numpy import array
from pympler import asizeof
from functools import reduce


def timer_upd(func):
    def temporary(*args, **kwargs):
        start_time = time()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        memory = memory_usage()
        delta_memory = memory[0] - start_memory[0]
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        print(f'Объём затраченной папяти на выполнение функции {func.__name__} = {delta_memory}')
        return result

    return temporary

# Первый пример. Для сравнения данные введу сразу через код, чтобы не зависеть от времени ввода данных.


@timer_upd
def first_example_no_optimisation():

    number = 2

    while not number or number not in range(1, 4):
        try:
            number = int(input(f'Введите целое число предприятий большее нуля (для проверки не большее трёх): '))
        except ValueError:
            print(f'Введите целое число предприятий большее нуля (для проверки не большее трёх)!')

    data = []
    for j in range(1, number + 1):
        Company = namedtuple(f'Company_data{j}', 'name q1 q2 q3 q4')

        a = f'name{j} {j * 10} {j * 10} {j * 10} {j * 10}'.split()
        while len(a) != 5:
            a = input(f'Введите через пробел данные о предприятии №{j} (Название, прибыль за каждый квартал года):').split()

        company_data = Company(a[0], int(a[1]), int(a[2]), int(a[3]), int(a[4]))
        data.append(company_data)

    b = []
    for i in data:
        b.append(i.q1 + i.q2 + i.q3 + i.q4)

    average = sum(b)/number
    print(average)

    high = ''
    low = ''

    for i in data:
        if i.q1 + i.q2 + i.q3 + i.q4 > average:
            if high != '':
                high = high + ', ' + i.name
            else:
                high = high + i.name
        elif i.q1 + i.q2 + i.q3 + i.q4 < average:
            if low != '':
                low = low + ', ' + i.name
            else:
                low = low + i.name
    print(f'Предприятия, с прибылью выше среднего значения: {high}\nПредприятия, с прибылью ниже среднего значения: {low}')


@timer_upd
def first_example_with_optimisation():
    number = 2

    while not number or number not in range(1, 4):
        try:
            number = int(input(f'Введите целое число предприятий большее нуля (для проверки не большее трёх): '))
        except ValueError:
            print(f'Введите целое число предприятий большее нуля (для проверки не большее трёх)!')

    data = []
    for j in range(1, number + 1):
        Company = recordclass(f'Company_data{j}', 'name q1 q2 q3 q4')

        a = f'name{j} {j * 10} {j * 10} {j * 10} {j * 10}'.split()
        while len(a) != 5:
            a = input(
                f'Введите через пробел данные о предприятии №{j} (Название, прибыль за каждый квартал года):').split()

        company_data = Company(a[0], int(a[1]), int(a[2]), int(a[3]), int(a[4]))
        data.append(company_data)

    b = []
    for i in data:
        b.append(i.q1 + i.q2 + i.q3 + i.q4)

    average = sum(b) / number
    print(average)

    high = ''
    low = ''

    for i in data:
        if i.q1 + i.q2 + i.q3 + i.q4 > average:
            if high != '':
                high = high + ', ' + i.name
            else:
                high = high + i.name
        elif i.q1 + i.q2 + i.q3 + i.q4 < average:
            if low != '':
                low = low + ', ' + i.name
            else:
                low = low + i.name
    print(
        f'Предприятия, с прибылью выше среднего значения: {high}\nПредприятия, с прибылью ниже среднего значения: {low}')
    del number
    del data
    del b
    del average
    del high
    del low


first_example_no_optimisation()  # time = 0.2016913890838623 sec; mem = 0.01953125 Mib
first_example_with_optimisation()  # time = 0.20119190216064453 sec; mem = 0.015625 Mib

'''Не смотря на то, что на уроке recordclass приводился, как способ уменьшить использование памяти, в данном
случае использование namedtuple оказывается эффективнее по объёму затрачиваемой памаяти. 
Однако удалось минимизировать затраты за счёт использования del практически в два раза.'''

# Пример 2
# Основы: урок 4
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.


@timer_upd
def second_example_no_optimisation():
    list2021 = [str(i) for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
    print(f"В диапозоне чисел от 20 до 240: {', '.join(list2021)} — кратны 20 или 21.")
    print(asizeof.asizeof(list2021))


@timer_upd
def second_example_with_optimisation():
    list2021 = array([str(i) for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])
    print(f"В диапозоне чисел от 20 до 240: {', '.join(list2021)} — кратны 20 или 21.")
    print(asizeof.asizeof(list2021))


second_example_no_optimisation()  # time = 0.20069098472595215; memory = 0.01171875
second_example_with_optimisation()  # time = 0.20069146156311035; memory = 0.0078125

'''Использование array из numpy даёт значительный выигрыш в объёме используемой памяти. 
По времени разницы практически нет, что делает данный способ примелимым для оптимизации.'''

# Пример 3
# Основы: урок 6
'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''


@timer_upd
def third_example_no_optimisation():

    class Road:

        def __init__(self, length, width):
            self._length = length
            self._width = width

        def mass(self):
            return self._length * self._width * 25 * 5 / 1000

    a = Road(20, 5000)
    print(f"Масса асфальта необходимого для покрытия всего дорожного полотна равна {a.mass()} т")
    print(asizeof.asizeof(a))  # 328


@timer_upd
def third_example_with_optimisation():
    class Road:
        __slots__ = ('_length', '_width')

        def __init__(self, length, width):
            self._length = length
            self._width = width

        def mass(self):
            return self._length * self._width * 25 * 5 / 1000

    a = Road(20, 5000)
    print(f"Масса асфальта необходимого для покрытия всего дорожного полотна равна {a.mass()} т")
    print(asizeof.asizeof(a))  # 112 меньший в три раза объём памяти за счёт слотов


third_example_no_optimisation()  # time = 0.20069122314453125; memory = 0.0078125
third_example_with_optimisation()  # time = 0.20069122314453125; memory = 0.0

# Использование слотов в ООП даёт однозначный выигрыш в памяти.

# Пример 3
# Основы: урок 4
'''Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''


@timer_upd
def fourth_example_no_optimisation():
    def multy(a1, a2):
        return a1 * a2

    even = [i for i in range(100, 1001, 2)]
    print(asizeof.asizeof(even))  # 18184
    res = reduce(multy, even)
    print(f""
          f"Результат перемножения всех чётных чисел от 100 до 1000 равен: "
          f"{str(res)[0:1]}.{str(round(int(str(res)[1:4])))}+e{len(str(res)) - 1}\n")


@timer_upd
def fourth_example_with_optimisation():
    def multy(a1, a2):
        return a1 * a2

    even = (i for i in range(100, 1001, 2))  # 432 → значительное уменьшение занимаемой памяти в сравнение с []
    print(asizeof.asizeof(even))
    res = reduce(multy, even)
    print(
        f"Результат перемножения всех чётных чисел от 100 до 1000 равен: "
        f"{str(res)[0:1]}.{str(round(int(str(res)[1:4])))}+e{len(str(res)) - 1}\n")


fourth_example_no_optimisation()  # time = 0.2021925449371338; memory = 0.10546875
fourth_example_with_optimisation()  # time = 0.20119190216064453; memory = 0.0

# Использование кортежей вместо списков даёт выигрыш в памяти примерно в 10 раз и незначительно во времени исполнения.
