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
import memory_profiler
import pickle
from numpy import array


# # скрипт 1
def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_dif = m2[0] - m1[0]
        return res, mem_dif
    return wrapper


@decor
def func_1(nums):
    """Функция создает список индексов четных чисел входящего списка """
    index_nums = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            index_nums.append(i)
    return index_nums


my_generator, mem_diff = func_1(list(range(100000)))
size_object = asizeof.asizeof(func_1(list(range(100000))))
print(f"Выполнение func_1 заняло {mem_diff} Mib, размер объекта {size_object} byte.")


@decor
def func_2(nums):
    index_nums = pickle.dumps([i for i in range(len(nums)) if nums[i] % 2 == 0])
    return index_nums


my_func, mem_diff = func_2(list(range(100000)))
size_object = asizeof.asizeof(func_2(list(range(100000))))
print(f"Выполнение func_2 заняло {mem_diff} Mib, размер объекта {size_object} byte.\n")

"""Профилирование памяти: func_1 - Выполнение заняло 1.671875 Mib, размер объекта 2044448 byte.
                          func_2 - Выполнение заняло 1.929687 Mib, размер объекта 184584 byte.
Аналитика: путем сериализации уменьшил размер объекта index_nums в 11 раз, но немного увеличилась выделенная память
под выполнение функции func_2"""


# скрипт 2
@decor
def check_1(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются."""
    for j in range(len(lst_obj)):
        if lst_obj[j] in lst_obj[j+1:]:
            return False
    return True


func1, mem_size = check_1(list(range(100000)))
print(f"Выполнение check_1 заняло {mem_size} MiB.")


@decor
def check_2(lst_obj):
    for j in range(len(lst_obj)):
        if lst_obj[j] in lst_obj[j+1:]:
            return False
    return True


func2, mem_size2 = check_2(array(range(100000)))
print(f"Выполнение check_2 заняло {mem_size2} MiB.\n")
"""Профилирование памяти: check_1 - Выполнение заняло 2.41015625 MiB.
                          check_2 - Выполнение заняло 0.5703125 MiB.
Аналитика: благадаря библиотеке NumPy удалось снизить затраты на память при выполнениии функции, с увеличением размера
масива разница становится заметно ощутима. Например при длине масива=100000, разница примерно 1.8 раза."""


# скрипт 3
@decor
def gen_num1(num):
    """Функция генерирует список из нечетных чисел"""
    a = []
    for i in range(1, num + 1, 2):
        a.append(i)
    return a


func_1, mem_size_1 = gen_num1(1000000)
print(f"Выполнение gen_num1 заняло {mem_size_1} MiB.")


@decor
def gen_num2(num):
    for i in range(1, num + 1, 2):
        yield i


func_2, mem_size_2 = gen_num2(1000000)
print(f"Выполнение gen_num2 заняло {mem_size_2} MiB.")
"""Профилирование памяти: gen_num1 - Выполнение заняло 11.49609375 MiB.
                          gen_num2 - Выполнение заняло 0.0 MiB.
Аналитика: благадаря генератору снизил расходы по памяти почти полностью. Так как генератору не надо хранить масив
данных, он выдает данные только при запросе"""
