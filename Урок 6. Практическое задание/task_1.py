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
# Задача 1
# Урок 4. Полезные инструменты
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

import random
import memory_profiler
import timeit
from pympler import asizeof
from numpy import array


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = timeit.default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        memory_usage = m2[0] - m1[0]
        run_time = timeit.default_timer() - start_time
        return result, memory_usage, run_time

    return wrapper


@decor
def no_repeat1(my_lst):
    return [elem for elem in my_lst if my_lst.count(elem) == 1]


@decor
def no_repeat2(my_lst):
    for k, x in enumerate(my_lst):
        if x not in my_lst[k + 1:] and x not in my_lst[:k]:
            yield x


my_list = [random.randrange(99) for i in range(10000)]

res, mem_diff, run_time = no_repeat1(my_list)
print(f"Выполнение функции repeat1 по памяти {mem_diff} Mib и {run_time} сек")
my_generator, mem_diff, run_time = no_repeat2(my_list)
print(f"Выполнение функции repeat2 по памяти {mem_diff} Mib и {run_time} сек")


# Функция no_repeat1 (списковое включение) вообще не использует память (или почти не использует), но в скорости
# примерно в 10 раз уступает функции no_repeat2 (yield), и это не очень хорошо. Учитывая что repeat2 немного
# (0.00390625 Mib), но использует память, и все же значительно выигрывает по скорости  (0.10162645799999992 сек
# против 1.269243243 сек), я считаю, что можно и нужно использовать функции, подобные no_repeat2 для дальнейшей работы
# если это возможно.

# Задача 2
# Урок 6. Объектно-ориентированное программирование
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить
# работу метода.


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def method_for_calc(self, thickness, weight):
        return self._length * self._width * thickness * weight


road = Road(20, 5000)
print('Использование объекта класса без __slots__:', asizeof.asizeof(road))


# weight = road.method_for_calc(25, 5) / 1000
# print(f'Масса асфальта: {weight:.0f} тонн')


class Road:
    __slots__ = '_length', '_width'

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def method_for_calc(self, thickness, weight):
        return self._length * self._width * thickness * weight


road = Road(20, 5000)
print('Использование объекта класса c __slots__:  ', asizeof.asizeof(road))
# weight = road.method_for_calc(25, 5) / 1000
# print(f'Масса асфальта: {weight:.0f} тонн')

# Использование слотов (__slots__) уменьшило на 34% количество занимаемой памяти, что и требовалось! Одно условие:
# набор экземпляров атрибутов ограничен. В мое случае '_length' и '_width'

# Задача 3
# Урок 2. Циклы. Рекурсия. Функции.
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
my_list = [0, 0]


@decor
def odd_parity1(n):
    if n == 0:
        return 1
    d = n % 10
    if d % 2 == 0:
        my_list[0] += 1
    else:
        my_list[1] += 1
    odd_parity1(n // 10)


res_1, mem_diff, run_time = odd_parity1(11111111112222222222)
print(f"Выполнение функции odd_parity1 по памяти {mem_diff} Mib и {run_time} сек")
# print(f'Количество четных и нечетных цифр в числе равно: {tuple(my_list)}')
del my_list
my_list = [0, 0]


@decor
def odd_parity2(n):
    for i in str(n):
        if (int(i) % 2) == 0:
            my_list[0] += 1
        else:
            my_list[1] += 1


res_2, mem_diff, run_time = odd_parity2(11111111112222222222)
print(f"Выполнение функции odd_parity2 по памяти {mem_diff} Mib и {run_time} сек")
# print(f'Количество четных и нечетных цифр в числе равно: {tuple(my_list)}')
#
# Здесь я ухожу от рекурсии к циклу, и это сразу стало видно: по времени выполнения odd_parity2 0.10384963000000003 сек,
# а у функции odd_parity1 - 4.213277226 сек! По памяти тоже есть небольшая разница: odd_parity2 - 0.0 Mib,
# а odd_parity1 = 0.0234375 Mib. Таким образом, в моем случае лучше использовать цикл вместо рекурсии, более того,
# строк для этих функций кода практически одинаково.

# Задача 4
# Урок 4. Полезные инструменты
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.

del my_list
my_list = [random.randint(-100, 100) for _ in range(50000)]


@decor
def num1():
    return [el for index, el in enumerate(my_list) if my_list[index - 1] < my_list[index] and index != 0]


@decor
def num2():
    return array([el for index, el in enumerate(my_list) if my_list[index - 1] < my_list[index] and index != 0])


res_3, mem_diff, run_time = num1()
print(f"Выполнение функции num1 по памяти {mem_diff} Mib и {run_time} сек и {asizeof.asizeof(num1())} байт")
res_4, mem_diff, run_time = num2()
print(f"Выполнение функции num2 по памяти {mem_diff} Mib и {run_time} сек и {asizeof.asizeof(num2())} байт")

# Попробовал поработать с библиотекой NumPy. num1 по памяти 0.234375 Mib больше чем 0.03125 Mib num2. Выигрывает num2.
# По времени особой разницы не заметил нет, а вот обработка большого объема чисел заметна: разница в 2 раза .
# Вывод: необходимо изучать NumPy хотя бы на начальном уровне.
