import time
from colorama import Fore, Back, Style
import memory_profiler
import timeit
import sys
from numpy import array

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
"""Первый пример"""
class Traffic:
    def __init__(self, color):
        self.color = color

    def traf(self):
        print(Fore.RED + self.color)
        time.sleep(7)
        self.color = 'Yellow'
        print(Fore.YELLOW + self.color)
        time.sleep(3)
        self.color = 'Green'
        print(Fore.GREEN + self.color)

class Traffic_opt():
    __slots__ = ('color')

    def __init__(self, color):
        self.color = color

    def traf(self):
        print(Fore.RED + self.color)
        time.sleep(7)
        self.color = 'Yellow'
        print(Fore.YELLOW + self.color)
        time.sleep(3)
        self.color = 'Green'
        print(Fore.GREEN + self.color)
if __name__ == '__main__':
    traffic1 = Traffic('Red')
    traffic2 = Traffic_opt('Red')
    print(sys.getsizeof(traffic1))
    print(sys.getsizeof(traffic2))

""" Для оптимизации использовала __slots__. Это помогло немного изменить объем 
заниманиемой памяти (все из-за небольшого количества атрибутов и впринципе 
цифры сами по себе небольшие).
Вот результаты измерений:
48
40
"""




"""Второй пример. Впринципе основан на том же самом способе уменьшитть объем 
занимаемой памяти"""
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
print(sys.getsizeof(b))
print(sys.getsizeof(b2))
""" Вот какой результат получился: 
328
192
(0.00390625, 0.10726159999999996)
(0.0, 0.10217589999999999)
Можно заметить, что после добавления __slots__ программа стала занимать намного меньше памяти, чем раньше. Улучшение 
почти в 2 раза
Плюс можно заметить прирост производительности (помимо уменьшения использования памяти)
"""


"""Третий варинат"""
def eratosphen(i):
    n = 2
    l = 100000
    a = [j for j in range(l)]
    a[1] = 0
    while n<l:
        if a[n] != 0:
            m = n + n
            while m < l:
                a[m] = 0
                m = m + n
        n += 1
    return [k for k in a if k != 0][i - 1]


def eratosphen1(i):
    n = 0
    l = 100000
    a = array([j for j in range(l)])
    a[1] = 0
    for n in a:
        if n:
            for k in range(n + 2, len(a)):
                if a[k
                ] % n == 0:
                    a[k] = 0
            n += 1
            if n == i:
                return n

print(sys.getsizeof(eratosphen(100)))
print(sys.getsizeof(eratosphen1(100)))
"""Вот результаты измерений:
56
28
Можно заметить, что array помог довольно-таки сильно уменьшить объем занимаемой памяти
Второй способ показывает себя намного эффективней чем просто первый способ где 
простой список
"""