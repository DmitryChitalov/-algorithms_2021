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
from pympler import asizeof
from sys import getsizeof
from memory_profiler import profile
import gc
from sys import getrefcount
import numpy
import json
from pympler import asizeof
import random

# Пример № 1 (Использование Сериализации)
# Исходный код
my_dict = {}
my_base = []
with open('task5_6.txt', encoding='utf-8') as out_base_object:
    for word in out_base_object:
        word = word.split(':')
        my_base.append(word[0])
        my_dict[word[0]] = None

    out_base_object.seek(0)

    x = 0
    for word in out_base_object:
        digit = [int(i) for i in word.split(' ') if i.isdigit()]
        digit = sum(digit)
        my_dict[my_base[x]] = digit
    x += 1

print(my_dict)
print(asizeof.asizeof(my_dict))

# Оптимизированный код
my_dict = {}
my_base = []
with open('task5_6.txt', encoding='utf-8') as out_base_object:
    for word in out_base_object:
        word = word.split(':')
        my_base.append(word[0])
        my_dict[word[0]] = None

    out_base_object.seek(0)

    x = 0
    for word in out_base_object:
        digit = [int(i) for i in word.split(' ') if i.isdigit()]
        digit = sum(digit)
        my_dict[my_base[x]] = digit
        x += 1

my_dict = json.dumps(my_dict)  # Преобразуем словарь в строку (json)
print(asizeof.asizeof(my_dict))
my_dict = json.loads(my_dict)  # При необходимости возращаем исходное состояние.
print(my_dict)


# Вывод: В итоге мы сократили использование памяти с 608 до 248:
# Словарь это Хеш-таблица, которая занимает большой объем памяти, используя json я "сжимаю" словарь,
# преобразовывая его в строку, а мы знаем, что строки занимают меньше памяти, (тип данных json в Python не существует)
# Так же потом можно восстановить исходный словарь методом json.loads.


# Пример № 2 (Использование слотов в ООП)
# Исходный код
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassRoad(Road):
    def __init__(self, _length, _width, weight, height):
        super().__init__(_length, _width)
        self.weight = weight
        self.height = height

    def MassCount(self):
        return self._length * self._width * self.weight * self.height / 1000


r = MassRoad(200000, 50000000, 250000, 50000)
print(f'Для покрытия всей дороги с толщиной {r.height} см. неободимо {int(r.MassCount())} т. асфальта')
print(r.__dict__)
print(asizeof.asizeof(r))


# Оптимизированный код
class Road:
    __slots__ = ['_length', '_width']  # Сохраниение атрибутов объекта класса в слоте (списке)

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassRoad(Road):
    def __init__(self, _length, _width, weight, height):
        super().__init__(_length, _width)
        self.weight = weight
        self.height = height

    def MassCount(self):
        return self._length * self._width * self.weight * self.height / 1000


r = MassRoad(200000, 50000000, 250000, 50000)
print(f'Для покрытия всей дороги с толщиной {r.height} см. неободимо {int(r.MassCount())} т. асфальта')
print(r.__slots__)
print(asizeof.asizeof(r))  # показывает размер используемой памяти объекта.

# Вывод: В итоге мы сократили использование памяти с 504 до 408:
# Как известно, в ООП стандрартно для хранения атрибутов объекта используется словарь, под него
# выделяется моного памяти, оптимизацией служит использование слотов, то есть другой контейнер для хранения в памяти
# - список, как известно, он будет занимать меньше памяти, но есть минус, что пропадает возможность добавлять атрибуты
# динамически, придется дописывать в слотах их в ручную.


# Пример № 3 (Использование NumPy)
# Исходный код
nums = [i * i for i in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    print(asizeof.asizeof(new_arr))
    return new_arr


print(func_1(nums))


# Оптимизированный код
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    new_arr = numpy.array(new_arr)  # преобразуем список в объект класса 'numpy.ndarray'
    print(asizeof.asizeof(new_arr))
    return new_arr


print(func_1(nums))

# Вывод: В итоге мы сократили использование памяти с 2112 до 320:
# Библиотека NumPy очень эффективна в использовании памяти, я передал список (массив) фунции array библиотеки NumPy,
# для сжятия, в итоге получаем объект класса 'numpy.ndarray'
#
#
# Пример № 4 (Использование Функции MAP )
# Исходный код
nums = [random.randint(100, 999) for i in range(100)]


#
def recursive_reverse(number):
    if number != 0:
        return str(number % 10) + str(recursive_reverse(number // 10))
    else:
        return ('')


nums = list(map(recursive_reverse, nums))
print(nums)

nums = [random.randint(100, 999) for i in range(100)]


# Оптимизированный код
def recursive_reverse(list, new_list=[]):
    for i in list:
        new_list.append(hex(i))
    print(asizeof.asizeof(new_list))
    return new_list


recursive_reverse(nums)


def recursive_reverse2(list):
    new_list = map(hex, list)
    print(asizeof.asizeof(new_list))
    return new_list


recursive_reverse2(nums)

# Вывод: В итоге мы сократили использование памяти с 6504 до 48:
# Использование map (встроенная функция) существенно сокращает использование объема памяти
