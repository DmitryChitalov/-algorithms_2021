from pympler import asizeof
from random import randint
from numpy import array
import memory_profiler
import timeit
import json

def memory_time(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = timeit.default_timer()
        func(*args)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = timeit.default_timer() - start_time
        return mem_diff, time_diff
    return wrapper


"""Первая программа. Вначале представлен пример с прошлого дз. Следующий пример - улучшенная версия."""
@memory_time
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        a = self._width * self._length*25*5/1000
        print("Масса асфальта равна ", a, "т")

@memory_time
class Road2:
    __slots__ = ("length2", "width2", "weight2", "thickness2")
    def __init__(self, length2, width2):
        self.length2 = length2
        self.width2 = width2
        self.weight2 = 25
        self.thickness2 = 5
    def mass2(self):
        a2 = self.width2 * self.length2 * self.weight2 * self.thickness2/1000
        print("Масса асфальта равна ", a2, "т")

b = Road(5000, 20)
b2 = Road2(500, 20)
print(b)
print(b2)
print(asizeof.asizeof(b))
print(asizeof.asizeof(b2))
""" Вот какой результат получился: 
328
192
(0.00390625, 0.10726159999999996)
(0.0, 0.10217589999999999)
Можно заметить, что после добавления __slots__ программа стала занимать намного меньше памяти, чем раньше. Улучшение 
почти в 2 раза
Плюс можно заметить прирост производительности (помимо уменьшения использования памяти)
"""


"------------------------------------------------------------------------------------------------------------"


""" Второй пример. Хранение 10 элементов в разных встроенных структурах данных. Это список, кортеж и множество."""
b = set({x for x in range(100)})
b2 = [x for x in range(100)]
b3 = tuple(x for x in range(100))
print(asizeof.asizeof(b))
print(asizeof.asizeof(b2))
print(asizeof.asizeof(b3))
"""Вот результат:
1040
496
432
Можно заметить, что хранение 10 элементов занимает меньше памяти в кортеже
"""


"------------------------------------------------------------------------------------------------------------"


""" Третий вариант. Заполнение рандомными числами 10000 раз"""

num1 = [i + randint(0, 10) for i in range(10000)]
num2 = list(map(int, [i + randint(0, 10) for i in range(10000)]))
num3 = array([el + randint(0, 10) for el in range(10000)])
print(asizeof.asizeof(num1))
print(asizeof.asizeof(num2))
print(asizeof.asizeof(num3))
""" Результаты измерений:
402424
402192
40120
Можно заметить, что метод map помог уменьшить объем памяти, но не так сильно, как это сделал array. Поэтому последний 
прекрасно подходит если поставлена задача снизить объем используемой памяти
"""


"------------------------------------------------------------------------------------------------------------"


"""Четвертый вариант с использование json"""
new_dict = {el: el for el in range(20, 240) if (el % 20) == 0 or (el % 21) == 0}
new_dict2_dumps = json.dumps(new_dict)
print(asizeof.asizeof(new_dict))
print(asizeof.asizeof(new_dict2_dumps))

""" Исходя из следующих замеров можно также заметить, что json помогает значительно уменьшить объем потребляемой памяти. 
Вот результаты: 
1880
304
"""