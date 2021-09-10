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

import memory_profiler
from timeit import default_timer
from numpy import array
from pympler import asizeof


def mem_time(func):
    def wrapper(*args, **kwargs):
        m_start = memory_profiler.memory_usage()
        t_start = default_timer()
        res = func(*args, **kwargs)
        t_stop = default_timer()
        m_stop = memory_profiler.memory_usage()
        print(f'Память: {m_stop[0] - m_start[0]} MiB, Время: {format((t_stop - t_start) * 1000000, ".1f")} мкс.')
        return res

    return wrapper


# Задача 1: Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(asizeof.asizeof(src))
unique_nums = set()
repeated_nums = set()
for num in src:
    if num in repeated_nums:
        continue
    if num in unique_nums:
        repeated_nums.add(num)
        unique_nums.discard(num)
        continue
    unique_nums.add(num)
result = [el for el in src if el in unique_nums]
print(result)

# После оптимизации:
src = array([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
print(asizeof.asizeof(src))
unique_nums = set()
repeated_nums = set()
for num in src:
    if num in repeated_nums:
        continue
    if num in unique_nums:
        repeated_nums.add(num)
        unique_nums.discard(num)
        continue
    unique_nums.add(num)
result = [el for el in src if el in unique_nums]
print(result)


# До оптимизации
# 472

# После оптимизации
# 176

# Благодаря использованию numpy и array вместо list, размер списков уменьшился почти в 3 раза.
# ---------------------------------------------------------------------------------------------------------------------

# Задача 2: Написать генератор нечётных чисел от 1 до n (включительно)
@mem_time
def task_2():
    n = 1000000
    odd_to_n = [num for num in range(1, n + 1, 2)]
    return odd_to_n


# После оптимизации:
@mem_time
def task_2_opt():
    n = 1000000
    for num in range(1, n + 1):
        if num % 2 == 1:
            yield num


task_2()
task_2_opt()


# До оптимизации
# Память: 20.0078125 MiB, Время: 28225.3 мкс.

# После оптимизации
# Память: 0.0 MiB, Время: 4.5 мкс.

# Использование генераторов даёт огромный выигрыш по времени и по использованию памяти.
# ---------------------------------------------------------------------------------------------------------------------

# Решение с помощью ООП:
class HexNumber:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))


num_1 = HexNumber('A2')
num_2 = HexNumber('C4F')
print(f'Сумма чисел из примера: {list(str(num_1 + num_2).upper())}')
print(f'Произведение - {list(str(num_1 * num_2).upper())}')

print(asizeof.asizeof(num_1))
print(asizeof.asizeof(num_2))


# После оптимизации:
class HexNumber_opt:
    __slots__ = ('val')

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))


num_3 = HexNumber_opt('A7')
num_4 = HexNumber_opt('C2F')
print(f'Сумма чисел из примера: {list(str(num_3 + num_4).upper())}')
print(f'Произведение - {list(str(num_3 * num_4).upper())}')

print(asizeof.asizeof(num_3))
print(asizeof.asizeof(num_4))

# До оптимизации
# 264
# 264

# После оптимизации
# 40
# 40

# Применение слотов в ООП существенно экономит память
