"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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

from memory_profiler import memory_usage, profile
from timeit import default_timer, timeit
from collections import namedtuple
from recordclass import recordclass
import sys


# script 1

def time_memory_measuring(func):
    def wrapper(*args, **kwargs):
        t = default_timer()
        memory_before = memory_usage()
        res = func(*args, **kwargs)
        memory_after = memory_usage()
        print(
            f'Время выполнения функции: {(default_timer() - t)}\n'
            f'Использовано памяти: {memory_after[0] - memory_before[0]} MiB\n')
        return res

    return wrapper


@time_memory_measuring
def create_list_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@time_memory_measuring
def create_list_2(nums):
    for i in nums:
        if nums[i] % 2 == 0:
            yield i


@time_memory_measuring
def generator_list_full(numbers):
    return list(i for i in create_list_2(numbers))


user_list = [el for el in range(0, 10000000)]
print('Create list with "for"')
create_list_1(user_list)
print('Create list with generator + filling list')
generator_list_full(user_list)

'''
Create list with "for"
Время выполнения функции: 1.1181155
Использовано памяти: 193.7421875 MiB

Create list with generator + filling list
Время выполнения функции: 0.2239603000000001
Использовано памяти: 0.0 MiB

Время выполнения функции: 1.3924622000000002
Использовано памяти: 38.87890625 MiB

На тесте видно что сам генератор не ест памяти в отличии от создания списка с помощью цикла for. 
Также по замеру скорости работы разница колосальная. 
НО имхо не корректно сравнивать именно объект генератора и сам список. Потому создана дополнительная функция на то 
чтобы генератор отработал столько раз чтобы вернуть требуемый список с индексами элементов, и тут уже видно что
скорость выполнения стала меньше, но по использованию памяти все еще преимущество на стороне генератора. 

'''


# script 2

@time_memory_measuring
def create_namedtuple(company_list):
    company_profit = namedtuple('Profit', 'name, first_quarter, second_quarter, third_quarter, fourth_quarter')
    result = []
    for i in range(len(company_list)):
        name = company_list[i][0]
        first_quarter, second_quarter, third_quarter, fourth_quarter = map(int, company_list[i][1])
        result.append(company_profit(name, first_quarter, second_quarter, third_quarter, fourth_quarter))
    return result


@time_memory_measuring
def create_recordclass(company_list):
    company_profit = recordclass('Profit', 'name, first_quarter, second_quarter, third_quarter, fourth_quarter')
    result = []
    for i in range(len(company_list)):
        name = company_list[i][0]
        first_quarter, second_quarter, third_quarter, fourth_quarter = map(int, company_list[i][1])
        result.append(company_profit(name, first_quarter, second_quarter, third_quarter, fourth_quarter))
    return result


company_list = (('q', (123456789012345, 123456789012345, 123456789012345, 123456789012345)),
                ('w', (123456789012345, 123456789012345, 123456789012345, 123456789012345)),
                ('e', (123456789012345, 123456789012345, 123456789012345, 123456789012345)),
                ('r', (123456789012345, 123456789012345, 123456789012345, 123456789012345)))

x = create_namedtuple(company_list)
y = create_recordclass(company_list)
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(type(x))
'''
namedtuple
Время выполнения функции: 0.2273119
Использовано памяти: 0.0859375 MiB

recordclass
Время выполнения функции: 0.224126
Использовано памяти: 0.0234375 MiB

Как показывают замеры при маленьких исходных данных recordclass выигрывает по использованию памяти. 
Скорость у обоих функций практически одинаковая. 
Объекты класса recordclass занимают меньше памяти чем объекты namedtuple.
'''

# script 3

from pympler import asizeof


class Worker:
    __slots__ = ('name', 'surname', 'position', 'income')  # использование слотов

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Positions(Worker):

    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


income_worker_1 = dict(wage=5000, bonus=3000)
income_worker_2 = dict(wage=11000, bonus=14000)

worker_1 = Positions('Maksim', 'Vaziulia', 'GitMaestro', income_worker_1)
print(asizeof.asizeof(worker_1))
worker_1.get_full_name()
worker_1.get_total_income()
worker_2 = Positions('Nikolai', 'Kopernik', 'Astronomer', income_worker_2)
print(asizeof.asizeof(worker_2))
worker_2.get_full_name()
worker_2.get_total_income()

'''
Размер экземпляра класса без использования слотов - 976
Размер экземляра класса при использование слотов - 832

Слоты дают экономию памяти для экземпляров класса. 
Минус слотов естественно невозможность добавления новых атрибутов вне конструктора класса.

'''
