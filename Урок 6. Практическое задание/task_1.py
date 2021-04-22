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
from numpy import array
from pympler import asizeof
from timeit import default_timer
from memory_profiler import memory_usage


def profile_decorator(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'Time consumed: {end_time - start_time}\r\nMemory consumed: {end_memory[0] - start_memory[0]}')
    return wrapper


@profile_decorator
def fill_list(number_of_items):
    test_list = []
    for iterator in range(number_of_items):
        test_list.append(iterator)
    return test_list


@profile_decorator
def fill_list_yield(number_of_items):
    list_to_use = list(range(number_of_items))
    for i in list_to_use:
        yield i


fill_list(10000000)
fill_list_yield(10000000)

"""
В 3 уроке у меня была функция заполнения списка значениями (fill_list).
Написал оптимизированную функцию fill_list_yield, которая использует генератор.
Провел профилирование. Оптимизированный вариант оказался и быстрее и эффективней по потреблению памяти,
Генератор потребляет мало памяти в ходы своей рабоыт и работает немного быстрее.

Time consumed: 1.2488017
Memory consumed: 0.40625
Time consumed: 0.10036500000000004
Memory consumed: 0.0

"""


class MyDictClass:
    def __init__(self, f_op):
        self.result_val = f_op

    def __add__(self, s_op):
        return list(hex(int(self.result_val, 16) + int(''.join(s_op), 16))[2:].upper())

    def __mul__(self, s_op):
        return list(hex(int(self.result_val, 16) * int(''.join(s_op), 16))[2:].upper())

class MyDictClassWithSlots:
    __slots__ = ('f_op', 's_op', 'result_val')

    def __init__(self, f_op):
        self.result_val = f_op

    def __add__(self, s_op):
        return list(hex(int(self.result_val, 16) + int(''.join(s_op), 16))[2:].upper())

    def __mul__(self, s_op):
        return list(hex(int(self.result_val, 16) * int(''.join(s_op), 16))[2:].upper())


first_op = "A2"
second_op = "C4F"
new_obj = MyDictClass(first_op)
new_obj_with_slots = MyDictClassWithSlots(first_op)
print(f"Sum {new_obj + second_op}")
print(f"Product {new_obj * second_op}")

print(asizeof.asizeof(new_obj))
print(asizeof.asizeof(new_obj_with_slots))

"""
В 5 уроке было задание по сложению шестнадцатеричных чисел. Было 2 варианта (с ООП и без него).
Написал оптимизированный класс с использованем слотов и определил размеры создаваемых экземпляров классов.

176 - размер экземпляра без слотов
72  - размер экземпляра класса с использованием слотов

Слоты сильно уменьшают размеры экземпляров классов, но уменьшают гибкость их использования.
"""


def arr():
    elem = list(el for el in range(10000))
    return elem


def numpy_arr():
    elem = array([el for el in range(10000)])
    return elem


first_array = arr()
second_array = numpy_arr()
print(asizeof.asizeof(first_array))
print(asizeof.asizeof(second_array))

"""
Написал две функции заполнения массива числами. Первый с помощью обычного списка, мторой с помощью numpy.array
Numpy оптимизированна для работы с большими массивами. Numpy.array занимает в памяти намного меньше места.

201560 - list
40064  - numpy
"""