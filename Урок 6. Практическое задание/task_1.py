"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from collections import namedtuple
from recordclass import recordclass
from timeit import default_timer
import memory_profiler
from random import randint


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper


"""
Алгоритм 1
задача из основ
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


@decor
def my_task_1_1(list_):
    """
    Вариант 1 изначальный
    Выполнение заняло 0.01171875 Mib и 2.2767754 sec
    """

    for item in range(10000):
        number = randint(0, 20)
        list_.append(number)
    return [item for item in list_ if list_.count(item) == 1]

@decor
def my_task_1_2(list_):
    """
    Вариант 2
    Заменив список на генератор, мы снижаем потребление памяти до минимума
    Выполнение заняло 0.0 Mib и 0.20923960000000008 sec
    """
    for item in range(10000):
        number = randint(0, 20)
        list_.append(number)
    yield (item for item in list_ if list_.count(item) == 1)


@decor
def my_task_1_3(list_):
    """
    Вариант 3
    также можно использовать SET еще на этапе заполнения
    Выполнение заняло 0.0078125 Mib и 0.20088309999999998 sec
    """
    my_set = set()
    for item in range(10000):
        number = randint(0, 20)
        my_set.add(number)
    return my_set


list_1 = []
if __name__ == '__main__':

    res, mem_diff, time_diff = my_task_1_1(list_1)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")

list_2 = []
if __name__ == '__main__':

    res, mem_diff, time_diff = my_task_1_2(list_1)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")

list_3 = []
if __name__ == '__main__':

    res, mem_diff, time_diff = my_task_1_3(list_1)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")
"""
Аналитика 1
С помощью генераторов и правильного использования типов данных, можно экономить память
"""

"""
Алгоритм 2
"""
@decor
def my_task_2_1(a, b):

    for i in range(21):
        a += b
        b *= a


class HexNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return hex(int(self.value, 16))[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.value, 16) + int(other.value, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.value, 16) * int(other.value, 16)))


a = 'A2'
b = 'C4F'

a = HexNumber(a)
b = HexNumber(b)


if __name__ == '__main__':

    res, mem_diff, time_diff = my_task_2_1(a, b)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")
'''
Стандартный варинат 1
Выполнение заняло 0.31640625 Mib и 8.9384087 sec
'''

'''
Модифицируем класс
'''
class HexNumber2:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return hex(int(self.value, 16))[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.value, 16) + int(other.value, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.value, 16) * int(other.value, 16)))


c = 'A2'
d = 'C4F'

c = HexNumber2(c)
d = HexNumber2(d)


if __name__ == '__main__':

    res, mem_diff, time_diff = my_task_2_1(c, d)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")
"""
Аналитика 2
Вариант со слотами серъезно экономит память
Выполнение заняло 0.19140625 Mib и 9.0148781 sec
"""

"""
Алгоритм 3
"""
"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
Класс collections.namedtuple()"""


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res, mem_diff, time_diff
    return wrapper


@decor
def companies_average(obj):
    sum_all_average = sum(company.average for company in obj)
    return sum_all_average / len(obj)


def companies_up(obj, average):
    up_list = []
    for company in obj:
        if company.average > average:
            up_list.append(company.name)
    return up_list


def companies_down(obj, average):
    down_list = []
    for company in obj:
        if company.average < average:
            down_list.append(company.name)
    return down_list


RES = namedtuple('Company_profit', 'name profit_1 profit_2 profit_3 profit_4 average')
RES2 = recordclass('Company_profit', 'name profit_1 profit_2 profit_3 profit_4 average')
companies_number = int(input('Введите количество предприятий для расчета прибыли: '))
companies_list = []
companies_list2 = []
for i in range(companies_number):
    temp_name = input('Введите название предприятия: ')
    temp_profit = [int(x) for x in input('через пробел введите прибыль данного предприятия\
за каждый квартал(Всего 4 квартала): ').split()]

    companies_list.append(RES(
        name=temp_name,
        profit_1=temp_profit[0],
        profit_2=temp_profit[1],
        profit_3=temp_profit[2],
        profit_4=temp_profit[3],
        average=sum(temp_profit) / len(temp_profit)
    ))
    companies_list2.append(RES2(temp_name, temp_profit[0], temp_profit[1], temp_profit[2], temp_profit[3],
                             sum(temp_profit) / len(temp_profit)))


if __name__ == '__main__':

    res, mem_diff, time_diff = companies_average(companies_list)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")

if __name__ == '__main__':

    res, mem_diff, time_diff = companies_average(companies_list2)
    print(f"Выполнение заняло {mem_diff} Mib и {time_diff} sec")


"""
Аналитика:
Заменив namedtuple на recordclass, потребление памяти снизилось. 
Что делает его предпочтительнее для работы в условиях ограниченности памяти
Выполнение заняло 0.0078125 Mib и 0.20737189999999828 sec
Выполнение заняло 0.0 Mib и 0.22384780000000148 sec
"""


