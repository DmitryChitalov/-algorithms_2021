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
import json
from numpy import array
from pympler import asizeof


def decor_time_mem(func):
    def my_func(*args, **kwargs):
        start = default_timer()
        memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Память {memory_usage()[0] - memory[0]}')
        print(f'Время: {default_timer() - start}')
        return result

    return my_func


@decor_time_mem
def func_1():
    dct = {i: i * 2 for i in range(100000)}
    with open("come_file1.json", "w", encoding="utf-8") as file:
        json.dumps(dct)


@decor_time_mem
def func_2():
    dct = {i: i * 2 for i in range(100000)}
    with open("come_file2.json", "w", encoding="utf-8") as file:
        json.dumps(dct)
    del dct


func_1()
func_2()
print("===============================")
"""
Первая фукнция сохраняет словарь в json файл, вторая после сохранения в json файл удаляет словарь, 
освобождая память.
"""


@decor_time_mem
def numpy_arr():
    elem = array([el for el in range(1000000)])
    return elem


@decor_time_mem
def arr():
    elem = list(el for el in range(1000000))
    return elem


numpy_arr()
arr()
print("===============================")
"""
Библиотека NumPy классно оптимизирована для работы с большими массивами, поэтому обычный список
проигрывает array в замерах памяти во много раз. 
"""


class HexNumber:
    def __init__(self, hex_number):
        self.hex_number = list(str(hex_number))

    def __add__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 + el_2))[2:]

    def __mul__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 * el_2))[2:]


class HexNumberSlot:
    __slots__ = ["hex_number"]

    def __init__(self, hex_number):
        self.hex_number = list(str(hex_number))

    def __add__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 + el_2))[2:]

    def __mul__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 * el_2))[2:]


a = "A2"
b = "C4F"
num_1 = HexNumber(a)
num_2 = HexNumber(b)
num_slot_1 = HexNumberSlot(a)
num_slot_2 = HexNumberSlot(b)
print(asizeof.asizeof(num_1.__dict__))
print(asizeof.asizeof(num_slot_1.__slots__))
"""
Магический атрибут Slot действительно позволяет освободить часть памяти при храненни данных класса.
В данном случае Slot позволяет сократить в 2,5 раза объем занимаемой памяти. 
"""
