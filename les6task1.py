import memory_profiler
import timeit
from pympler import asizeof
from numpy import array
from random import randint

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
#Старый код
def numbers():
    number = input('Введите натуральное число: ')
    if not number.isdigit() or not int(number):  # После этого остаются только натуральные числа. Последним отсекаем '0'
        print('Вы должны были ввести натуральное число. Попробуйте еще раз.')
        return numbers()
    return even_odd(int(number))


@memory_time
def wrap(number):
    def even_odd(number):
        values = [0, 0]
        if not number // 10:
            if number % 2:
                values[1] += 1
            else:
                values[0] += 1
            return values
        return tuple(x + y for x, y in zip(even_odd(number // 10), even_odd(number % 10)))

    return even_odd(number)


@memory_time
def even_odd1(number):
    values = [0, 0]
    while number:
        if number % 10 % 2:
            values[1] += 1
        else:
            values[0] += 1
        number = number // 10
    return values


a = 1
for i in range(200):
    a *= randint(2, 1000)

print(wrap(a))
print(even_odd1(a))
"""
(0.8046875, 0.1083732)
(0.0, 0.10813709999999999)
Можно заметить, что решение без рекурсии оптимальнее и по памяти и по времени.
Что говорит нам о том, чтобы не использовать ее без 
необходимости. 
"""

"""Второй пример. Впринципе основан на том же самом способе уменьшитть объем 
занимаемой памяти"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        a = self._width * self._length*25*5/1000
        print("Масса асфальта равна ", a, "т")


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

b1 = Road(5000, 20)
b2 = Road2(500, 20)
print(asizeof.asizeof((b1)))
print(asizeof.asizeof((b2)))
""" Вот какой результат получился: 
328
192
Можно заметить, что после добавления __slots__ программа стала занимать намного меньше памяти, чем раньше. Улучшение 
почти в 2 раза. Оптимизация проведена
"""


"""Третий варинат"""
@memory_time
def eratosphen1(i):
    length = 100000
    list_of_numbers = [j for j in range(length)]
    list_of_numbers[1] = 0
    count = 0
    for n in list_of_numbers:
        if n:
            for _ in range(n + 2, len(list_of_numbers)):
                if list_of_numbers[_] % n == 0:
                    list_of_numbers[_] = 0
            count += 1
            if count == i:
                return n

@memory_time
def eratosphen2(i):
    length = 100000
    list_of_numbers = array([j for j in range(length)])
    list_of_numbers[1] = 0
    count = 0
    for n in list_of_numbers:
        if n:
            for _ in range(n + 2, len(list_of_numbers)):
                if list_of_numbers[_] % n == 0:
                    list_of_numbers[_] = 0
            count += 1
            if count == i:
                return n

c1 = eratosphen1(100)
c2 = eratosphen2(100)
print(c1)
print(c2)
"""Вот результаты измерений:
(0.42578125, 0.7440925)
(0.01171875, 2.8448868000000003)
Можно заметить, что array помог уменьшить объем занимаемой памяти
Он показывает себя эффективней по памяти, чем список.
Однако, этот способ работает дольше. Вывод: нужно
выбирать реализацию исходя из наших данных(ресурсов)
"""