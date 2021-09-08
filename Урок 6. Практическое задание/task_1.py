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
import random


def check_res(func):
    def wrapper(*args, **kwargs):
        mem_before = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(*args, **kwargs)
        stop_time = default_timer()
        mem_after = memory_profiler.memory_usage()
        print(f'memory: {mem_after[0] - mem_before[0]}, time: {stop_time - start_time}')
        return res

    return wrapper


# Task 1 - old version (для замеров завернул старый код в функцию)
@check_res
def task_1_old():
    SECS_PER_MIN = 60
    MINS_PER_HOUR = 60
    HOURS_PER_DAY = 24

    DURATIONS = [53, 153, 4153, 400153]

    for i in range(len(DURATIONS)):
        seconds = DURATIONS[i] % SECS_PER_MIN
        int_part = DURATIONS[i] // SECS_PER_MIN  # целая часть от деления, переходит на следующий уровень
        result = '{} сек'.format(seconds)

        if int_part:
            minutes = int_part % MINS_PER_HOUR
            int_part //= MINS_PER_HOUR
            result = '{} мин {}'.format(minutes, result)

            if int_part:
                hours = int_part % HOURS_PER_DAY
                days = int_part // HOURS_PER_DAY
                result = '{} час {}'.format(hours, result)

                if days:
                    result = '{} дн {}'.format(days, result)

        print('duration =', DURATIONS[i])
        print(result)


# Task 1 - new version (переменные и константы переопределяю как с чистого листа)
SECS_PER_MIN = 60
MINS_PER_HOUR = 60
HOURS_PER_DAY = 24

DURATIONS = [53, 153, 4153, 400153]


def task_1_new():
    for dur in DURATIONS:  # убрал лишнюю переменную и действия
        seconds = dur % SECS_PER_MIN
        int_part = dur // SECS_PER_MIN  # целая часть от деления, переходит на следующий уровень
        result = f'{seconds} сек'  # использовал f-строку вместо format

        if int_part:
            minutes = int_part % MINS_PER_HOUR
            int_part //= MINS_PER_HOUR
            result = f'{minutes} мин {result}'  # использовал f-строку вместо format

            if int_part:
                hours = int_part % HOURS_PER_DAY
                days = int_part // HOURS_PER_DAY
                result = f'{hours} час {result}'  # использовал f-строку вместо format

                if days:
                    result = f'{days} дн {result}'  # использовал f-строку вместо format

        yield f'duration = {dur} ==> {result}'  # функция-генератор


@check_res
def call_task_1_new():
    res = task_1_new()
    while True:
        try:
            print(next(res))
        except StopIteration:
            break


print('Вызов функций для замеров')
task_1_old()  # memory: 0.015625, time: 0.0002178410000000519
call_task_1_new()  # memory: 0.0,      time: 0.00016122900000004048
#   Вывод:
#   Использование функции-генератора заметно снизило использование памяти и, возможно,
#   повлияло на время выполнения кода в лучшую сторону

# Task 2 - old version (для замеров завернул старый код в функцию)
SRC = [random.randint(1, 100) for _ in range(10000)]


@check_res
def task_2_1_old():
    result_lst = []

    if len(SRC) > 1:
        for idx in range(1, len(SRC)):
            if SRC[idx] > SRC[idx - 1]:
                result_lst.append(SRC[idx])
    return result_lst


@check_res
def task_2_2_old():
    return (SRC[idx] for idx in range(1, len(SRC)) if SRC[idx] > SRC[idx - 1])


# Task 2 - new version (переменные и константы переопределяю как с чистого листа)
@check_res
def task_2_1_new():  # Использование list comprehension дает выигрыш как по памяти, так и по скорости относительно
    return [SRC[idx] for idx in range(1, len(SRC)) if SRC[idx] > SRC[idx - 1]]  # обычного цикла


@check_res
def task_2_2_new():  # Использование генератора дает выигрыш по скорости относительно исходного варианта
    for idx in range(1, len(SRC)):
        if SRC[idx] > SRC[idx - 1]:
            yield SRC[idx]


print('Вызов функций для замеров')

print(task_2_1_old())  # memory: 0.08203125, time: 0.008351309000000029
print(list(task_2_2_old()))  # memory: 0.0, time: 2.8531999999970026e-05

print(task_2_1_new())  # memory: 0.00390625, time: 0.006879413999999917
print(list(task_2_2_new()))  # memory: 0.0, time: 1.0869000000024442e-05


# Task 3 - old version
class HexNumber:
    def __init__(self, val: str):
        self.val = val

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))

    def __repr__(self):
        return str(self.val)[2:]


@check_res
def hex_samples_1(fst_num, sec_num):
    num_1 = HexNumber(fst_num)
    num_2 = HexNumber(sec_num)
    print(f'Сумма введённых чисел равна {list(str(num_1 + num_2))}')
    print(f'Произведение введённых чисел равно {list(str(num_1 * num_2))}')


# Task 3 - new version
class HexNumberSlots:
    __slots__ = ('val',)  # В этом варианте класса используются slots

    def __init__(self, val: str):
        self.val = val

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))

    def __repr__(self):
        return str(self.val)[2:]


@check_res
def hex_samples_2(fst_num, sec_num):
    num_1 = HexNumberSlots(fst_num)
    num_2 = HexNumberSlots(sec_num)
    print(f'Сумма введённых чисел равна {list(str(num_1 + num_2))}')
    print(f'Произведение введённых чисел равно {list(str(num_1 * num_2))}')


print('Вызов функций для замеров')

hex_samples_1('A1', 'B11')  # memory: 0.0, time: 0.00018749699999998093
hex_samples_2('A1', 'B11')  # memory: 0.0, time: 0.00015941799999996675

# Выводы из третьего примера сделать сложно, но использование слотов в классе должно давать экономию по памяти
