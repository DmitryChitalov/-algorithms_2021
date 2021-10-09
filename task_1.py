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


import time
import memory_profiler
from dataclasses import dataclass


def measurements(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        start_mem = memory_profiler.memory_usage()
        res = function(*args)
        print(time.perf_counter_ns() - start_time, '\n')
        print(memory_profiler.memory_usage()[0] - start_mem[0], '\n')
        return res
    return wrapped


# Я не нашел подхлдящих скриптов из курса основ, поэтому делал свои примеры.


@measurements
def first(input_list):
    def wrapped(some_list, result=[]):
        if len(some_list) == 0:
            return result
        if some_list[-1] % 2 == 0:
            result.append(some_list[-1])
        some_list.pop()
        return wrapped(some_list, result)
    return wrapped(input_list)


@measurements
def first_upgrade(some_list):
    result = []
    for num in some_list:
        if num % 2 == 0:
            result.append(num)
    return result


@measurements
def first_full_upgrade(some_list):
    return [num for num in some_list if num % 2 == 0]


# Выводы:
# Использовать рекурсию для простых операций не лучшая идея, использует много памяти: 0.05859375.
# Обычное решение в лоб показывает себя лучше: 0.00390625.
# Ну и LC еще лучше: 0.0. Хотелось бы поднять значение больше 100, но для этого нужно поднимать количество вызовов
# рекурсии, что я пытался сделать, но код завершается с ошибкой. В общем, не стал я в это лезть.
# Для того, чтобы замерять вес рекурсии сделал обертку для нее.


@measurements
def second():

    class ShopClass:
        def __init__(self, name=""):
            self.name = name
            self.listGoods = []

    @dataclass
    class DataGoods:
        name: str
        price: int
        unit: str

    shop = ShopClass("MyShop")
    for _ in range(200):
        shop.listGoods.extend([
            DataGoods("телефон", 20000, "RUB"),
            DataGoods("телевизор", 45000, "RUB"),
            DataGoods("тостер", 2000, "RUB")
        ])


@measurements
def second_upgrade():

    class ShopClass:
        __slots__ = ("name", "listGoods")

        def __init__(self, name=""):
            self.name = name
            self.listGoods = []

    @dataclass
    class DataGoods:
        __slots__ = ("name", "price", "unit")
        name: str
        price: int
        unit: str

    shop = ShopClass("MyShop")
    for _ in range(200):
        shop.listGoods.extend([
            DataGoods("телефон", 20000, "RUB"),
            DataGoods("телевизор", 45000, "RUB"),
            DataGoods("тостер", 2000, "RUB")
        ])


# Если мы знаем, какие будут атрибуты нашего класса, то можно использовать __slots__, что значительно уменьшит вес.
# Без __slots__: 0.13671875, с __slots__: 0.0.


@measurements
def third(some_list):
    result = []
    for num in some_list:
        if num % 2 == 0:
            result.append(num * num)


@measurements
def third_upgrade(some_list):
    for num in some_list:
        if num % 2 == 0:
            yield num * num


# Из-за использования ленивых вычислений генератор будет занимать меньше памяти.
# Обычный подход: 0.00390625, генератор: 0.0.


if __name__ == '__main__':
    first(list(range(100))), first_upgrade(list(range(100))), first_full_upgrade(list(range(100)))
    second(), second_upgrade()
    third(list(range(100))), third_upgrade(list(range(100)))
