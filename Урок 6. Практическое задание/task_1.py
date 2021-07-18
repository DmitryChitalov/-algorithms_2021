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


from memory_profiler import profile, memory_usage
from numpy import array, append, arange
from pympler import asizeof
from sys import getsizeof


def memory_usage_decor(func):
    def wrapper(*args):
        mu_start = memory_usage()
        result = func(*args)
        mu_finish = memory_usage()
        mu_diff = mu_finish[0] - mu_start[0]
        return result, mu_diff
    return wrapper


# ----------------------------------------------------------------------------------------------------------------------
""" 
1. Оптимизация с использованием генератора, вместо итератора. Для примера взят исходник 1 задания, 4 урока данного курса.
Исходная функция была переделана на генератор, вместо итератора, что колоссально снизило количество потребляемой памяти. 
Чем больший список будет попадать на вход, тем больший эффект будет достигнут, т.к. генератор хранит в памяти только
один элемент из получаемого результата.

Размер объекта результата (sys.getsizeof) старой функции: 444376 байт
Размер объекта результата (sys.getsizeof) новой функции: 112 байт

Результат выполнения memory_usage_decor старой функции: 1.9296875 Mib
Результат выполнения memory_usage_decor новой функции: 0.00390625 Mib
"""


@memory_usage_decor
def old_func(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory_usage_decor
def new_func(nums):
    for index in range(len(nums)):
        if nums[index] % 2 == 0:
            yield index
        else:
            continue


nums_list = [i for i in range(0, 100000)]

result_old_func, mu_old_func = old_func(nums_list)
result_new_func, mu_new_func = new_func(nums_list)

# ----------------------------------------------------------------------------------------------------------------------
"""
2. Оптимизация с помощью numPy. Для примера взят исходник 1 задания, 4 урока данного курса.
В результате отказа от обычных массивов в пользу массивов numPy получилось уменьшить расход памяти на операции создания
массива (начального и результирующего) почти в 2.5 раза, но размер итоговых данных оказался всего лишь на 42кб меньше.
Исходя их этого, могу сделать вывод, что оптимизация массивов с использованием numPy больше подходит, когда необходимо 
быстро обработать массивы, а не когда нужно хранить большие объемы данных в памяти.
Пока писал вывод, попробовал замерить на 1000000 элементах. Результаты были намного лучше, чем на 100000

Размер объекта результата (sys.getsizeof) старой функции: 444376 байт
Размер объекта результата (sys.getsizeof) новой функции: 400104 байт

Результат выполнения memory_usage_decor старой функции: 2.53125 Mib
Результат выполнения memory_usage_decor новой функции: 0.90234375 Mib

Результат выполнения memory_usage_decor старой функции: 19.85546875 Mib (1000000 элементов)
Результат выполнения memory_usage_decor новой функции: 3.70703125  Mib (1000000 элементов)
"""


@memory_usage_decor
def old_func_np():
    nums_list = [i for i in range(0, 100000)]

    new_arr = []

    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory_usage_decor
def new_func_np():
    nums_list = arange(100000)

    new_arr = array([])

    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            new_arr = append(new_arr, i)
    return new_arr


result_old_func, mu_old_func = old_func_np()
result_new_func, mu_new_func = new_func_np()

# ----------------------------------------------------------------------------------------------------------------------
"""
3. Оптимизация классов в ООП используя __slots__. Для примера взят класс из 3 задания, 6 урока курса Основ.
В результате использования слотов для классов были получены следующие замеры замеров объекта:

pympler.asizeof() :
Старый объект: 928
Новый объект: 608

sys.getsizeof() :
Старый объект: 48
Новый объект: 64

sys.getsizeof() ведет подсчет класса, без учета данных экземпляра, поэтому, добавляя __slots__, мы увеличиваем вес класса,
но в сумме, получается прирост за счет того, что экземпляр класса становится меньше по объему
"""


class OldWorker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

    def __str__(self):
        return f'{self.name} {self.surname}. Должность: {self.position}'


class NewWorker:
    __slots__ = ['name', 'surname', 'position', '_income']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

    def __str__(self):
        return f'{self.name} {self.surname}. Должность: {self.position}'


old_worker = OldWorker('Alexandr', 'Volkov', None, '75000', '50000')
new_worker = NewWorker('Alexandr', 'Volkov', None, '75000', '50000')
