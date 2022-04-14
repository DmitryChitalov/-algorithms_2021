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

from pympler import asizeof
from timeit import timeit
from random import randint
from numpy import array

#__slots__

class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_asphalt(self, weight=25, thickness=5):
        return f"{self.__length} * {self.__width} * {weight} * {thickness} =" \
               f"{(self.__length * self.__width * weight * thickness) / 1000}"


road = Road(5000, 20)
print(asizeof.asizeof(road))


class Road:
    __slots__ = ['__length', '__width', 'weight', 'thickness']

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_asphalt(self, weight=25, thickness=5):
        return f"{self.__length} * {self.__width} * {weight} * {thickness} =" \
               f"{(self.__length * self.__width * weight * thickness) / 1000}"


road = Road(5000, 20)
print(asizeof.asizeof(road))


"""
В данном скрипте для более эффективного использования памяти мы использовали __slots__. 
По умолчанию данные класса хранятся в словаре(под хэш-таблицу выделяется памяти больше, чем нужно),
 __slots__ помогает изменить тип данных для хранения и использовать вдвое меньше памяти. 
 
asizeof.asizeof = 344 без использования __slots__
asizeof.asizeof = 128 с использования __slots__ 
"""



#NumPy


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = [randint(100, 1000) for number in range(50000)]
print(asizeof.asizeof(num_100))


def recursive_reverse_2(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = array([randint(100, 1000) for number in range(50000)])
print(asizeof.asizeof(num_100))


"""
Для сокращения используемого обьема памяти в данном скрипте использовался модуль array.
Библиотека NumPy эффективно обрабатвает большой обьем данных, при этом занимает меньший обьем данных.

asizeof.asizeof = 1764344 без использования array
asizeof.asizeof = 200120 с использования array

"""


#yield


def func_1(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(asizeof.asizeof(func_1(list(range(1000)))))
print(timeit("func_1(list(range(1000)))", globals=globals(), number=10000))


def func_2(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    yield new_arr


print(asizeof.asizeof(func_2(list(range(1000)))))
print(timeit("func_1(list(range(1000)))", globals=globals(), number=10000))


""" 
asizeof.asizeof = 20208 без использования yield
asizeof.asizeof = 40448 с использования yield

В данном скрипте yield занял в два раза больше памяти.
Но время исполнения с yield меньше:
timeit = 0.6369398 
timeit = 0.6180266999999999 с yield 
"""