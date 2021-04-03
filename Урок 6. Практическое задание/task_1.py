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

from functools import wraps
from memory_profiler import memory_usage, profile
from pympler import asizeof
import copy


def memory_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper


@memory_decorator
def work_with_list(list_arg):
    new_list = [item ** 2 for item in list_arg]
    return new_list


@memory_decorator
def work_with_generator(list_arg):
    for item in list_arg:
        yield item ** 2


list_to_test = list(range(1000))
print(work_with_list(list_to_test))
print(work_with_generator(list_to_test))

'''
Декоратор memory_decorator считает количество памяти которую использует переданная ему функция.
По результатам видно что функция которая генерирует новый список и возвращает его занимает определенный объем памяти.
Функции которая использует генератор достаточно той памяти которая была выделена при старте скрипта.
То есть функция с генератором с точки зрения потребления памяти более выгодна.
0.0390625
0.0
'''


class RoadOne:
    weight_per_m2 = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calculation(self, thickness):
        weight = self._width * self._length * RoadOne.weight_per_m2 * thickness / 1000
        print(f"Масса асфальта равна: {round(weight,2)} тонн.")


class RoadTwo:
    __slots__ = ['_length', '_width']
    weight_per_m2 = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_calculation(self, thickness):
        weight = self._width * self._length * RoadTwo.weight_per_m2 * thickness / 1000
        print(f"Масса асфальта равна: {round(weight,2)} тонн.")


r1 = RoadOne(20000, 20)
r2 = RoadTwo(20000, 20)

print(f"Объект r1 занимает {asizeof.asizeof(r1)} в пямяти.")
print(f"Объект r2 занимает {asizeof.asizeof(r2)} в пямяти.")

'''
Объект r1 занимает 328 в пямяти.
Объект r2 занимает 112 в пямяти.
При отказе от использования хэш таблиц для хранения атрибутов класса получаем экономию памяти.
Объект r2 где используется __slot__ занимает меньше места в памяти.
'''


@profile
def func_1(list_arg):
    original_list = [item * 2 for item in list_arg]
    new_list = original_list
    del original_list
    return new_list


list_to_test_2 = list(range(100000))
func_1(list_to_test_2)

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   106     23.5 MiB     23.5 MiB           1   @profile
   107                                         def func_1(list_arg):
   108     28.4 MiB  -2626.7 MiB      100003       original_list = [item * 2 for item in list_arg]
   109     28.4 MiB      0.0 MiB           1       new_list = original_list
   110     28.4 MiB      0.0 MiB           1       del original_list
   111     28.4 MiB      0.0 MiB           1       return new_list
'''


@profile
def func_2(list_arg):
    original_list = [item * 2 for item in list_arg]
    new_list = original_list
    del original_list
    del new_list
    new_list = []
    return new_list


func_2(list_to_test_2)

'''
В данном результате видим что при удаленн всех ссылок на один и тот же объект память освобождается.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   129     24.1 MiB     24.1 MiB           1   @profile
   130                                         def func_2(list_arg):
   131     28.1 MiB   -101.3 MiB      100003       original_list = [item * 2 for item in list_arg]
   132     28.1 MiB      0.0 MiB           1       new_list = original_list
   133     28.1 MiB      0.0 MiB           1       del original_list
   134     24.1 MiB     -4.0 MiB           1       del new_list
   135     24.1 MiB      0.0 MiB           1       new_list = []
   136     24.1 MiB      0.0 MiB           1       return new_list
'''