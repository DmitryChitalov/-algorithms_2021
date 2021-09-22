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
from memory_profiler import profile
from pympler import asizeof
from numpy import array
from random import randint
from collections import namedtuple
from recordclass import recordclass

# ----------------------------------------------------------------------------------------------------------------------
n = 200


@profile
def elem_sum():
    sum_elms = 0
    el = 1
    count = 0
    while count != n - 1:
        el = -(el / 2)
        sum_elms = sum_elms + el
        count += 1
    print(sum_elms + 1)


@profile
def wrapper_func():
    def elem_sum_recurs(n, sum_elms=0.0, count=0, el=1.0):
        if count == n - 1:
            print(sum_elms + 1)
        else:
            el = -(el / 2)
            sum_elms = sum_elms + el
            count += 1
            return elem_sum_recurs(n, sum_elms, count, el)

    return elem_sum_recurs(n, sum_elms=0.0, count=0, el=1.0)


"""
Вывод:

В данном случае лучше использовать цикл, т.к. использование рекурсии даёт инкремент из-за создания стека.

"""

# Использование slots --------------------------------------------------------------------------------------------------
class Cell:
    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        pass

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        if self.cell > other.cell:
            return self.cell / other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __floordiv__(self, other):
        if self.cell > other.cell:
            return self.cell // other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def make_order(self, rows):
        result = ''
        for i in range(self.cell // rows):
            result += f'{"*" * rows}\n'
        result += f'{"*" * (self.cell % rows)}\n'
        return result


class Cell1:
    __slots__ = 'cell'

    def __init__(self, cell):
        self.cell = int(cell)

    def __str__(self):
        pass

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __mul__(self, other):
        return self.cell * other.cell

    def __truediv__(self, other):
        if self.cell > other.cell:
            return self.cell / other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def __floordiv__(self, other):
        if self.cell > other.cell:
            return self.cell // other.cell
        else:
            return f'Количество ячеек первой клетки меньше количества ячеек второй клетки'

    def make_order(self, rows):
        result = ''
        for i in range(self.cell // rows):
            result += f'{"*" * rows}\n'
        result += f'{"*" * (self.cell % rows)}\n'
        return result


"""
Вывод: 
При создании экземпляров классов с одинаковым значением параметра cell, экзмепляр класса, в котором используется 
инструмент slots занимает значительно меньше памяти (без slots - 240, с slots - 40).

"""

# Использование объекта array модуля numpy -----------------------------------------------------------------------------

list_1 = [randint(1, 1000) for n in range(50000)]
list_2 = array([randint(1, 1000) for num in range(50000)])


def min_val_check(lst):
    for i in range(len(lst)):
        min_val = lst[i]
        check_lst = lst[i + 1:]
        for val in check_lst:
            if val < min_val:
                min_val = val
        return min_val


"""
Вывод:
В данном случае создание массива с использованием объекта array модуля numpy позволяет сократить объем занимаемой памяти
более чем в 8 раз. 

"""
# Использование recordclass --------------------------------------------------------------------------------------------


@profile
def average_annual_income():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    INFO = namedtuple('Company', 'name income')
    aver_ann_inc = {}
    total_aver = 0
    higher_inc = []
    lower_inc = []
    aver_inc = []
    for i in range(count):
        COMP_INFO = INFO(
            name=input('Введите название предприятия: '),
            income=input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        )
        print(f'Размер namedtuple: {asizeof.asizeof(COMP_INFO)}')
        aver_ann_inc[COMP_INFO.name] = \
            (int(COMP_INFO.income.split(' ')[0]) + int(COMP_INFO.income.split(' ')[1])
             + int(COMP_INFO.income.split(' ')[2]) + int(COMP_INFO.income.split(' ')[3])) / 4

    for val in aver_ann_inc.values():
        total_aver += val
    total_aver = total_aver / count

    print(f'Средняя годовая прибыль всех предприятий: {total_aver}')

    for k, v in aver_ann_inc.items():
        if v > total_aver:
            higher_inc.append(k)
        elif v < total_aver:
            lower_inc.append(k)
        else:
            aver_inc.append(k)


@profile
def average_annual_income_1():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    INFO = recordclass('Company', 'name income')
    aver_ann_inc = {}
    total_aver = 0
    higher_inc = []
    lower_inc = []
    aver_inc = []
    for i in range(count):
        COMP_INFO = INFO(
            name=input('Введите название предприятия: '),
            income=input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        )
        print(f'Размер recordclass: {asizeof.asizeof(COMP_INFO)}')
        aver_ann_inc[COMP_INFO.name] = \
            (int(COMP_INFO.income.split(' ')[0]) + int(COMP_INFO.income.split(' ')[1])
             + int(COMP_INFO.income.split(' ')[2]) + int(COMP_INFO.income.split(' ')[3])) / 4

    for val in aver_ann_inc.values():
        total_aver += val
    total_aver = total_aver / count

    print(f'Средняя годовая прибыль всех предприятий: {total_aver}')

    for k, v in aver_ann_inc.items():
        if v > total_aver:
            higher_inc.append(k)
        elif v < total_aver:
            lower_inc.append(k)
        else:
            aver_inc.append(k)

"""
Вывод:
Размер объекта namedtuple почти в 6 раз больше размера объекта recordclass, поэтому целесообразнее использовать 
recordclass для сохранения данных.

"""

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    elem_sum()
    wrapper_func()
    cell_1 = Cell(40)
    print(asizeof.asizeof(cell_1))
    cell_2 = Cell1(40)
    print(asizeof.asizeof(cell_2))
    min_val_check(list_1)
    print(asizeof.asizeof(list_1))
    min_val_check(list_2)
    print(asizeof.asizeof(list_2))
    print(average_annual_income())
    print(average_annual_income_1())
