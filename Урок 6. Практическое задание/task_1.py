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

from memory_profiler import memory_usage, profile
from random import randint
import json
import numpy as np
from pympler.asizeof import asizeof

# 1. Курс основ, урок 4, задание 2
# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# Старое решение:

m1 = memory_usage()[0]
income = [randint(0, 100) for i in range(1_000_000)]
outcome = [num for order, num in enumerate(income) if num > income[order-1] and order != 0]
print(memory_usage()[0] - m1)
# Замеры памяти: 12.4609375 MiB

# Для улучшения мы можем использотвать библиотеку numpy для генерации и хранения чисел:
m2 = memory_usage()[0]
income_2 = np.random.randint(100, size=1_000_000)
outcome_2 = np.array([num for order, num in enumerate(income_2) if num > income_2[order-1] and order != 0])
print(memory_usage()[0] - m2)

# Замеры памяти показали: 5.92578125 что в два раза лучше по сравнению с использованием обычных списков.

# 2. Курс основ, урок 2, задание 6

# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# старое решение:

goods = []
item_number = 1
while True:
    item = {}
    item['название'] = input(f'Введите название товара {item_number}:\n')
    item['цена'] = float(input(f'Введите цену товара {item_number}:\n'))
    item['количество'] = float(input(f'Введите количество товара {item_number}:\n'))
    item['единица измерения'] = input(f'Введите единицу измерения товара {item_number}:\n')
    item_enumerated = (item_number, item)
    goods.append(item_enumerated)
    item_number += 1
    next = input('Введите любой символ для ввода следующего предмета или q чтобы закончить\n')
    if next == 'q':
        break

print(asizeof(goods))

# при вводе двух товаров функция asizeof выдает следующие показатели занимаемой памяти: 1384
# Если использовать сериализацию для хранения вместо словаря, то при тех же данных размер в полтора раза меньше - 904:
# Здесь смысла не имеет, но при более масштабных задачах может пригодиться

goods = []
item_number = 1
item = ('')
while True:
    item = {}
    item['название'] = input(f'Введите название товара {item_number}:\n')
    item['цена'] = float(input(f'Введите цену товара {item_number}:\n'))
    item['количество'] = float(input(f'Введите количество товара {item_number}:\n'))
    item['единица измерения'] = input(f'Введите единицу измерения товара {item_number}:\n')
    item_enumerated = (item_number, json.dumps(item))   # используем json для сериализации
    goods.append(item_enumerated)
    item_number += 1
    next = input('Введите любой символ для ввода следующего предмета или q чтобы закончить\n')
    if next == 'q':
        break

print(asizeof(goods))


# 3. Курс основ, урок 6, задание 1

# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}
# . Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


# старое решение:

class Worker:
    def __init__(self, name, surname, position,  money):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = money

class Position(Worker):
    def __init__(self, name, surname, position, money):
        super().__init__(name, surname, position, money)

    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


money = {
    'wage': 10000,
    'bonus': 500,
}

# Запрофилируем функцию, создав 100 тысяч одинаковых работников:

@profile()
def create_100():
    return [Position('Petr', 'Petrov', 'Driver', money) for i in range(100_000)]

create_100()

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    151     30.0 MiB     30.0 MiB           1   @profile()
#    152                                         def create_100():
#    153     47.0 MiB     17.0 MiB      100003       return [Position('Petr', 'Petrov', 'Driver', money) for i in range(100_000)]

# То же самое, но при использовании __slots__ для хранения аттрибутов в списке, а не в словаре, использует
# только 7 мебибайт памяти вместо 17 (меняем только одну строку, добавляя в класс Worker:
# __slots__ = ['name', 'surname', 'position', '_income']):

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    183     32.2 MiB     32.2 MiB           1   @profile()
#    184                                         def create_100():
#    185     39.3 MiB      7.1 MiB      100003   return [Position('Petr', 'Petrov', 'Driver', money) for i
#                                                        in range(100_000)]

# код с исправлением
class Worker:
    __slots__ = ['name', 'surname', 'position', '_income']  # внесенное исправление
    def __init__(self, name, surname, position,  money):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = money

class Position(Worker):
    def __init__(self, name, surname, position, money):
        super().__init__(name, surname, position, money)

    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

@profile()
def create_100():
    return [Position('Petr', 'Petrov', 'Driver', money) for i in range(100_000)]

create_100()