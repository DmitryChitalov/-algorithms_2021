from timeit import default_timer
import memory_profiler


def mem_tm(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        time_diff = default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Заняло памяти: {mem_diff} MiB\nЗаняло времени: {time_diff}\nвыходные данные: {res}'
    return wrapper


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @mem_tm
    def calc_weight(self):
        weight = self._length * self._width * 25 * 5
        return f'{weight}кг'


class Road_s:
    __slots__ = ['length', 'width']
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @mem_tm
    def calc_weight(self):
        weight = self.length * self.width * 25 * 5
        return f'{weight}кг'


a = Road(979879979000000, 900000000798646500)
b = Road_s(979879979000000, 900000000798646500)
print(a.calc_weight())          # 0.00390625 MiB, 1.9899999999961615e-05
print(b.calc_weight())          # 0.0 MiB, 2.3200000000000998e-05

"""
Были использованы слоты в классах. Слоты хранят данные не в словарях,
а списках, что значительно сказывается на памяти. Но в некоторых замерах видно что скорость
может снизиться, т.к в словарях доступ к значениям с константной сложностью.
"""