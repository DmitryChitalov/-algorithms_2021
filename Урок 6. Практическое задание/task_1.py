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
import timeit
from pympler import asizeof

from memory_profiler import profile, memory_usage


def benchmark(func):

    def wrapper(*args, **kwargs):
        start_timer = timeit.default_timer()
        memory_1 = memory_usage()[0]
        value = func(*args, **kwargs)
        print(f' *** Использовано памяти {func} - {memory_usage()[0] - memory_1} Mib.')
        print(f' *** Время выполнения {func} - {timeit.default_timer() - start_timer} сек.')
        return value
    return wrapper


class HexNumber:
    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __add__(self, other):
        hex_sum = hex(int(''.join(self.hex_number), 16) + int(''.join(other.hex_number), 16))
        return list(str(hex_sum)[2:].upper())

    def __mul__(self, other):
        hex_mul = hex(int(''.join(self.hex_number), 16) * int(''.join(other.hex_number), 16))
        return list(str(hex_mul)[2:].upper())

    def __str__(self):
        return str(self.hex_number)


class HexNumberSlots:
    __slots__ = ['hex_number']

    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __add__(self, other):
        hex_sum = hex(int(''.join(self.hex_number), 16) + int(''.join(other.hex_number), 16))
        return list(str(hex_sum)[2:].upper())

    def __mul__(self, other):
        hex_mul = hex(int(''.join(self.hex_number), 16) * int(''.join(other.hex_number), 16))
        return list(str(hex_mul)[2:].upper())

    def __str__(self):
        return str(self.hex_number)


if __name__ == "__main__":

    num_1 = HexNumber(list('A2'))
    print('num_1 size', asizeof.asizeof(num_1))
    num_2 = HexNumberSlots(list('C4F'))
    print(type(num_2.__slots__))
    print(num_2.__slots__)
    print('num_2 size', asizeof.asizeof(num_2))

    print(f'{num_1} + {num_2} =', num_1 + num_2)
    print(f'{num_1} * {num_2} =', num_1 * num_2)